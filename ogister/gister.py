import argparse
import rdflib
from owl2diagram.main import get_class_diagram, get_object_diagram
from owl2diagram.main import save_diagram
from collections import Counter
from datetime import datetime

from ogister import fetcher
from ogister import util
from nltk.corpus import stopwords
stopwords = stopwords.words('english')


def get_meta_text(input_path, title, desc, abstract, lang=None, max_options=0):
    """
    Get all the meta text from the given ontology
    """
    g = rdflib.Graph()
    print("\n\n\t\t==============\n\t Parsing: %s (format: %s)" % (input_path, rdflib.util.guess_format(input_path)))
    g.parse(input_path, format=rdflib.util.guess_format(input_path))
    meta = []
    if title:
        titles = fetcher.get_titles(g, lang=lang)
        if max_options > 0:
            print("%d of titles out of %d" % (min(max_options, len(titles)), len(titles)))
            titles = titles[:max_options]
        meta += titles
        print("titles: ")
        # print(len(titles))
        print(titles)
    if desc:
        descs = fetcher.get_descriptions(g, lang=lang)
        if max_options > 0:
            print("%d of descriptions out of %d" % (min(max_options, len(descs)), len(descs)))
            descs = descs[:max_options]
        meta += descs
        print("descriptions: ")
        # print(len(descs))
        print(descs)
    if abstract:
        absts = fetcher.get_abstracts(g, lang=lang)
        if max_options > 0:
            print("%d of abstracts out of %d" % (min(max_options, len(absts)), len(absts)))
            absts = absts[:max_options]
        meta += absts
        print("abstracts")
        print(absts)
    return meta, g


def keyword_in_ontology(keyword, g, only_object_property=True):
    classes = fetcher.get_classes_with_keyword(g, keyword)
    properties = fetcher.get_properties_with_keyword(g, keyword, only_object_property)
    return classes, properties


def all_stop_words(tokens):
    for t in tokens:
        if t.lower() not in stopwords:
            return False
    return True


def get_matched_per_text(m, max_num_tok, g, only_object_property):
    tokens = util.split_text(m)
    i = 0
    matched = []
    matched_classes = []
    matched_properties = []
    while i < len(tokens):
        token_added = False
        for l in range(max_num_tok, 0, -1):
            tks = tokens[i:i+l]
            if tks[0] in [',', '.']:
                continue
            kw = " ".join(tks)
            if all_stop_words(tks):
                # print("skip: %s" % kw)
                continue
            classes, properties = keyword_in_ontology(kw, g, only_object_property)
            matched_classes += classes
            matched_properties += properties
            if len(classes+properties) > 0:
                matched.append(kw)
                i += l
                token_added = True
                break
        if not token_added:
            i += 1
    print("Matched keyword: ")
    print(matched)
    print("matched classes: ")
    print(matched_classes)
    print("matched properties: ")
    print(matched_properties)
    return matched, matched_classes, matched_properties


def get_matched(meta, max_num_tok, g, only_object_property):
    mkeywords = []
    mclasses = []
    mproperties = []
    for m in meta:
        keywords, classes, properties = get_matched_per_text(m, max_num_tok, g,
                                                             only_object_property=only_object_property)
        mkeywords += keywords
        mclasses += classes
        mproperties += properties

    mkeywords = list(set(mkeywords))  # to remove duplicates
    mclasses = list(set(mclasses))
    mproperties = list(set(mproperties))
    return mkeywords, mclasses, mproperties


def get_primary_classes_and_relations(input_path, title, desc, abstract, only_object_property, lang=None, max_options=0):
    """
    Get relations, classes and properties related to the meta.
    """

    meta, g = get_meta_text(input_path=input_path, title=title, desc=desc, abstract=abstract, lang=lang,
                            max_options=max_options)
    keywords, classes, properties = get_matched(meta=meta, max_num_tok=5, g=g,
                                                only_object_property=only_object_property)
    class_relations = fetcher.get_relations(g, classes)
    property_relations = fetcher.get_properties_relations(g, properties)
    constraints = fetcher.get_classes_constraints(g, classes)
    class_relations += constraints

    return class_relations, property_relations, classes, properties


def draw_diagrams(classes, relations, out_path):
    """
    classes: shorten classes
    relations: a list
    out_path: the path for the markdown file
    return None
    """
    diagram = get_class_diagram(classes)
    diagram += get_object_diagram(relations)
    save_diagram(diagram, out_path)


def shorten_uris(uris):
    shortened_uris = [fetcher.shorten_url(u) for u in uris]
    return shortened_uris


def shorten_relations(rels):
    shortented_rels = [(fetcher.shorten_url(r[0]), fetcher.shorten_url(r[1]), fetcher.shorten_url(r[2])) for r in rels]
    return shortented_rels


def workflow(input_path, title, desc, abstract, only_object_property, out_path=None, lang=None, max_options=0):
    """
    meta: either "title", "description", or "abstract". It is only used for the json files
    """
    class_relations, property_relations, classes, properties = get_primary_classes_and_relations(input_path, title, desc, abstract, lang=lang,
                                                   max_options=max_options, only_object_property=only_object_property)
    relations = list(set(class_relations + property_relations))

    top_relations = shorten_relations(relations)
    top_classes = shorten_uris(classes)
    # classes_top, relations_top = get_top(topn=topn, classes=classes, relations=relations)
    if out_path:
        draw_diagrams(classes=top_classes, relations=top_relations, out_path=out_path)
    print(top_relations)
    return top_classes, top_relations


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', required=True, help="Ontology file.")
    parser.add_argument('-o', '--output', help="Output file.")
    parser.add_argument('-t', '--title', action="store_true", help="To look into titles.")
    parser.add_argument('-d', '--description', action="store_true", help="To look into description.")
    parser.add_argument('-a', '--abstract', action="store_true", help="To look into abstract.")
    parser.add_argument('-n', '--topn', default=0,  help="The maximum number of relevant classes.")
    parser.add_argument('-l', '--lang', default=None, help="language tag. e.g., en")
    parser.add_argument('--object-property', action="store_true", help="Whether to only use object property for getting the relevant properties relenvant to the given meta")
    parser.add_argument('-m', '--maxoptions', default=0, help="Maximum number of meta literal for each meta type (e.g., title)")
    # parser.add_argument('-y', '--charlimit', default=0, help="Maximum number of characters per literal property.")
    args = parser.parse_args()
    return args.input, args.output, args.title, args.description, args.abstract, int(args.topn), args.lang, int(args.maxoptions), args.object_property


def main():
    a = datetime.now()
    input_path, out_path, title, desc, abstract, topn, lang, max_options, only_object_property = parse_arguments()
    workflow(input_path=input_path, out_path=out_path, title=title, desc=desc, abstract=abstract, topn=topn,
             lang=lang, max_options=max_options, only_object_property=only_object_property)
    b = datetime.now()
    print("\n\nTime it took: %.1f minutes\n\n" % ((b - a).total_seconds() / 60.0))


if __name__ == "__main__":
    main()
