import argparse
import math
import os
import subprocess

import rdflib
from owl2diagram.main import get_class_diagram, get_object_diagram
from owl2diagram.main import save_diagram
from collections import Counter
from operator import itemgetter
from datetime import datetime

from devos import fetcher
from devos import util
from nltk.corpus import stopwords
from string import punctuation

META_INCLUDE_PROP = False  # Whether to look for the property labels.
IMPORTANT_CLASS_REF = True  # Whether to prefer relations between important classes

DEBUG = True

stopwords = stopwords.words('english')
special_chars = set(punctuation.replace('.', ''))

labels_cache = dict()


def escape_spaces_in_class(item):
    return "`"+item.strip()+"`"


def escape_spaces_in_classes(classes):
    return [escape_spaces_in_class(c) for c in classes]


def escape_spaces_in_relations(relations):
    rels = []
    for r in relations:
        t = (escape_spaces_in_class(r[0]), r[1], escape_spaces_in_class(r[2]))
        rels.append(t)
    return rels


def to_string_relations(relations):
    rels = []
    for r in relations:
        t = (str(r[0]), str(r[1]), str(r[2]))
        rels.append(t)
    return rels


def to_string_items(items):
    print(items)
    return [str(item) for item in items]


def print_classes(classes):
    for c in classes:
        print(c)


def print_relations(relations, short=False):
    for c1, r, c2 in relations:
        if short:
            c1 = c1.split('/')[-1].split('#')[-1]
            c2 = c2.split('/')[-1].split('#')[-1]
            r = r.split('/')[-1].split('#')[-1]

        print("%s\t==(%s)==>\t%s" % (c1, r, c2))


def print_results(classes, relations):
    print("\n\n============================\nSelected Classes: ")
    print_classes(classes)
    print("\nSelected Relations: ")
    print_relations(relations)


def debug_classes(g):
    """
    Print the labels for the classes
    """
    classes = fetcher.get_all_classes(g)
    print("\nClasses Labels: %d" % len(classes))
    for c in classes:
        labels = fetcher.get_labels(g, c)
        print("%s:\t%s" % (c, str(labels)))
    print("\n\n")


def clear_cache():
    global labels_cache
    labels_cache = dict()


def parse_ontology(input_path):
    g = rdflib.Graph()
    if DEBUG:
        print("\n\n\t\t==============\n\t Parsing: %s (format: %s)" % (input_path, rdflib.util.guess_format(input_path)))
    g.parse(input_path, format=rdflib.util.guess_format(input_path))
    return g


def get_top_relations_hard(classes, relations, topr, topn=0):
    """
    Get the top relations between the important classes only
    """
    if len(classes) == 0:
        return relations

    per_class = dict()
    top_relations = []

    if len(classes) < topn or topn==0:
        classes_list = []
        for r in relations:
            if r[0] not in classes:
                classes_list.append(r[0])
            if r[2] not in classes:
                classes_list.append(r[2])
        c = Counter(classes_list)
        if topn==0:
            for p in c:
                if p not in classes:
                    classes.append(p)
        else:
            num_rem = topn - len(classes)
            pairs = c.most_common(num_rem)

            print(pairs)
            for p in pairs:
                print(p)
                classes.append(p[0])

    print("number of classes: %d" % len(classes))

    for c in classes:
        per_class[c] = 0

    if topr > 0:
        rmax = math.ceil(topr/len(classes))
        for r in relations:
            if r[0] in per_class and r[2] in per_class:
                if per_class[r[0]] < rmax and per_class[r[2]] < rmax:
                    per_class[r[0]] += 1
                    per_class[r[2]] += 1
                    top_relations.append(r)

    else:
        print(per_class)
        for r in relations:

            if r[0] in per_class and r[2] in per_class:
                top_relations.append(r)
            else:
                if r[0] not in per_class:
                    sk = r[0]
                elif r[2] not in per_class:
                    sk = r[2]
                else:
                    print("strange: ")
                    print(r)
                # print("Eliminating: <%s>" % sk)

    if DEBUG:
        print("important relations: ")
        print(top_relations)

    return top_relations


def get_top_relations_soft(classes, relations, topr):
    """
    Get the top relations
    """

    if len(classes) == 0 or topr <= 0:
        return relations

    per_class = dict()

    rmax = math.ceil(topr/len(classes))

    for c in classes:
        per_class[c] = 0

    rem_relations = []
    top_relations = []
    if IMPORTANT_CLASS_REF:
        for r in relations:
            if r[0] in per_class and r[2] in per_class:
                if per_class[r[0]] < rmax:
                    per_class[r[0]] += 1
                    top_relations.append(r)
                elif per_class[r[2]] < rmax:
                    per_class[r[2]] += 1
                    top_relations.append(r)
                else:
                    rem_relations.append(r)
            else:
                rem_relations.append(r)
        if DEBUG:
            print("important relations: ")
            print(top_relations)
    else:
        rem_relations = relations

    for r in rem_relations:
        if r[0] in per_class:
            c = r[0]
        elif r[2] in per_class:
            c = r[2]
        else:
            print("Relation %s is not in the top classes" % str(r))
            raise Exception("unrelated relation is discovered")

        if per_class[c] < rmax:
            per_class[c] += 1
            top_relations.append(r)

    return top_relations


def get_meta_text(input_path, title, desc, abstract, lang=None, max_options=0):
    """
    Get all the meta text from the given ontology
    """
    g = parse_ontology(input_path)
    meta = []
    if title:
        titles = fetcher.get_titles(g, lang=lang)
        if max_options > 0:
            if DEBUG:
                print("%d of titles out of %d" % (min(max_options, len(titles)), len(titles)))
            titles = titles[:max_options]
        meta += titles
        if DEBUG:
            print("titles: ")
            print(len(titles))
            print(titles)
    if desc:
        descs = fetcher.get_descriptions(g, lang=lang)
        if max_options > 0:
            if DEBUG:
                print("%d of descriptions out of %d" % (min(max_options, len(descs)), len(descs)))
            descs = descs[:max_options]
        meta += descs
        if DEBUG:
            print("descriptions: ")
            print(len(descs))
            print(descs)
    if abstract:
        absts = fetcher.get_abstracts(g, lang=lang)
        if max_options > 0:
            if DEBUG:
                print("%d of abstracts out of %d" % (min(max_options, len(absts)), len(absts)))
            absts = absts[:max_options]
        meta += absts
        if DEBUG:
            print("abstracts")
            print(absts)
    return meta, g


def keyword_in_ontology(keyword, g, only_object_property=True):
    classes = fetcher.get_classes_with_keyword(g, keyword)
    properties = []
    if META_INCLUDE_PROP:
        properties = fetcher.get_properties_with_keyword(g, keyword, only_object_property)
    return classes, properties


def all_stop_words(tokens):
    for t in tokens:
        if t.lower() not in stopwords:
            return False
    return True


def get_matched_per_text(m, max_num_tok, g, only_object_property, lower=True):
    tokens = util.split_text(m.strip())

    if DEBUG:
        print("\nTokens: ")
        print(tokens)

    # max_num_tok = min(max_num_tok, len(tokens))
    i = 0
    matched = []
    matched_classes = []
    matched_properties = []
    while i < len(tokens):
        token_added = False
        max_num_tok = min(max_num_tok, len(tokens)-i)
        for l in range(max_num_tok, 0, -1):
            tks = tokens[i:i + l]
            # print("----- [%d, %d]" % (i, l))
            # print(tks)
            if tks[0][0] in special_chars:
                # print("\nskip special char: %s" % kw)
                break
            kw = " ".join(tks)
            if all_stop_words(tks):
                # print("\nskip stopword: %s" % kw)
                continue
            kw_processed = kw
            if lower:
                kw_processed = kw.lower()
            classes, properties = keyword_in_ontology(kw_processed, g, only_object_property)
            matched_classes += classes
            matched_properties += properties
            if len(classes + properties) > 0:
                matched.append(kw)
                i += l
                token_added = True
                break
        if not token_added:
            i += 1

    matched = list(set(matched))
    matched_classes = list(set(matched_classes))
    matched_properties = list(set(matched_properties))

    if DEBUG:
        print("\nmatched keyword: ")
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
    if DEBUG:
        print("\nget_matched> ")
        print(meta)
    for m in meta:
        keywords, classes, properties = get_matched_per_text(m, max_num_tok, g,
                                                             only_object_property=only_object_property)
        mkeywords += keywords
        mclasses += classes
        mproperties += properties

    mkeywords = list(set(mkeywords))  # to remove duplicates
    # mclasses = list(set(mclasses))
    mclasses = util.ordered_unique_list(mclasses)
    mproperties = list(set(mproperties))
    return mkeywords, mclasses, mproperties


def get_classes_and_relations(input_path, title, desc, abstract, only_object_property, topn=0, lang=None,
                              max_options=0):
    """
    Get relations, classes related from the meta properties.
    """
    meta, g = get_meta_text(input_path=input_path, title=title, desc=desc, abstract=abstract, lang=lang,
                            max_options=max_options)
    keywords, classes, properties = get_matched(meta=meta, max_num_tok=5, g=g,
                                                only_object_property=only_object_property)

    classes = to_string_items(classes)
    properties = to_string_items(properties)

    classes = util.ordered_unique_list(classes)
    properties = util.ordered_unique_list(properties)

    if topn > 0:
        classes = classes[:topn]
        # properties = properties[:topn]
    class_relations = fetcher.get_relations(g, classes)
    class_relations = to_string_relations(class_relations)

    if DEBUG:
        print("class relations: ")
        print(class_relations)

    property_relations = fetcher.get_properties_relations(g, properties)
    property_relations = to_string_relations(property_relations)

    if DEBUG:
        print("property relations: ")
        print(property_relations)
    constraints = fetcher.get_classes_constraints(g, classes)
    constraints = to_string_relations(constraints)

    if DEBUG:
        print("constraints: ")
        print(constraints)
    class_relations += constraints

    relations = list(set(class_relations + property_relations))

    return relations, classes, g


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
    # out_path = out_path[:-2]+"mmd"
    # with open(out_path, "w") as f:
    #     f.write(diagram)
    png_input = out_path
    # png_output = out_path[:-3]+"png"
    png_output = out_path[:-2]+"png"
    generate_png(png_input, png_output)


def generate_png(input_path, output_path, scale=7):
    try:
        comm = "mmdc -i %s -o %s -s %d" % (input_path, output_path, scale)
        print(comm)
        ret = subprocess.call(comm, shell=True)
    except Exception as e:
        print(e)
        print("unable to generate png for: %s" % input_path)


def get_label(g, uri, lang=None):
    global labels_cache

    if uri not in labels_cache:
        labels_cache[uri] = fetcher.get_print_label(g, uri, lang)
        # print("get_label> %s =>\t %s" % (uri, labels_cache[uri]))
    # else:
    #     print("cached: %s =>\t %s" % (uri, labels_cache[uri]))
    return labels_cache[uri]


def shorten_uris(uris):
    shortened_uris = [fetcher.shorten_url(u) for u in uris]
    return shortened_uris


def label_uris(g, uris, lang=None):
    labeled_uris = [get_label(g, u, lang) for u in uris]
    labels = [str(l) for l in labeled_uris]
    return labels


def shorten_relations(rels):
    shortented_rels = [(fetcher.shorten_url(r[0]), fetcher.shorten_url(r[1]), fetcher.shorten_url(r[2])) for r in rels]
    return shortented_rels


def label_relations(g, rels):
    labeled_rels = [(get_label(g, r[0]), get_label(g, r[1]), get_label(g, r[2])) for r in rels]
    rels = [(str(a), str(b), str(c)) for a, b, c in labeled_rels]
    return rels


def meta_workflow(input_path, title, desc, abstract, only_object_property, out_path=None, lang=None, max_options=0,
                  topn=0, topr=0, soft=False):
    """
    meta: either "title", "description", or "abstract". It is only used for the json files
    """
    relations, classes, g = get_classes_and_relations(input_path, title, desc, abstract, topn=topn, lang=lang,
                                                      max_options=max_options, only_object_property=only_object_property)

    if soft:
        top_relations = get_top_relations_soft(classes, relations, topr)
    else:
        top_relations = get_top_relations_hard(classes, relations, topr, topn)

    top_classes = label_uris(g, classes)
    top_relations = label_relations(g, top_relations)

    if out_path:
        draw_diagrams(classes=escape_spaces_in_classes(top_classes), relations=escape_spaces_in_relations(top_relations), out_path=out_path)

    if DEBUG:
        debug_classes(g)

    print_results(top_classes, top_relations)

    return top_classes, top_relations


def get_freq_classes(g, topn, only_object_property):
    d = fetcher.get_class_freq(g, only_object_property=only_object_property)
    freq_cls_pairs = []
    for k in d:
        p = (d[k], k)
        freq_cls_pairs.append(p)
    freq_cls_pairs.sort(reverse=True, key=itemgetter(0))

    if DEBUG:
        print("\nClasses Frequency")
        for p in freq_cls_pairs:
            print("%3d -- %s" % (p[0], p[1]))
    if topn > 0:
        freq_cls_pairs = freq_cls_pairs[:topn]
    top_classes = [p[1] for p in freq_cls_pairs]
    if DEBUG:
        print(freq_cls_pairs)
    return top_classes


def get_leng_classes(g, topn):
    d = fetcher.get_class_leng(g)

    freq_cls_pairs = []
    for k in d:
        p = (d[k], k)
        freq_cls_pairs.append(p)

    freq_cls_pairs.sort(reverse=True, key=itemgetter(0))

    if topn > 0:
        freq_cls_pairs = freq_cls_pairs[:topn]

    top_classes = [p[1] for p in freq_cls_pairs]

    d_top_classes = dict()
    for c in top_classes:
        d_top_classes[c] = d[c]

    return top_classes, d_top_classes


def freq_workflow(input_path, out_path, topn, only_object_property, topr=0, soft=False):
    """
    Use frequency as the importance signal
    """
    g = parse_ontology(input_path)
    top_classes = get_freq_classes(g, topn=topn, only_object_property=only_object_property)
    class_relations = fetcher.get_relations(g, top_classes)
    class_relations = to_string_relations(class_relations)
    constraints = fetcher.get_classes_constraints(g, top_classes)
    constraints = to_string_relations(constraints)
    class_relations += constraints

    if soft:
        top_relations = get_top_relations_soft(top_classes, class_relations, topr)
    else:
        top_relations = get_top_relations_hard(top_classes, class_relations, topr, topn)
    top_relations = label_relations(g, top_relations)
    top_classes = label_uris(g, top_classes)

    if DEBUG:
        print("\nTop classes: ")
        for c in top_classes:
            print("\t%s" % c)
        print("\nrelations: ")
        print(top_relations)
    util.print_relations(top_relations)
    if DEBUG:
        print("\nconstraints: ")
        for c in constraints:
            print(c)

    if out_path:
        draw_diagrams(classes=escape_spaces_in_classes(top_classes), relations=escape_spaces_in_relations(top_relations), out_path=out_path)

    if DEBUG:
        debug_classes(g)

    print_results(top_classes, top_relations)

    return top_classes, top_relations


def leng_workflow(input_path, out_path, topn, topr, soft=False):
    """
    Workflow using the comments length as the signal for importance
    """
    g = parse_ontology(input_path)
    top_classes, class_leng_dict = get_leng_classes(g, topn=topn)

    class_relations = fetcher.get_relations(g, top_classes)
    class_relations = to_string_relations(class_relations)
    constraints = fetcher.get_classes_constraints(g, top_classes)
    constraints = to_string_relations(constraints)
    class_relations += constraints

    if soft:
        top_relations = get_top_relations_soft(top_classes, class_relations, topr)
    else:
        top_relations = get_top_relations_hard(top_classes, class_relations, topr, topn)
    top_relations = label_relations(g, top_relations)
    top_classes = label_uris(g, top_classes)

    if out_path:
        draw_diagrams(classes=escape_spaces_in_classes(top_classes), relations=escape_spaces_in_relations(top_relations), out_path=out_path)

    if DEBUG:
        debug_classes(g)

    print_results(top_classes, top_relations)

    return top_classes, top_relations, class_leng_dict


def parse_arguments():
    """
    Parse command line arguments
    """
    global DEBUG
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', required=True, help="Ontology file.")
    parser.add_argument('-o', '--output', help="Output file.")
    parser.add_argument('-t', '--title', action="store_true", help="To look into titles.")
    parser.add_argument('-d', '--description', action="store_true", help="To look into description.")
    parser.add_argument('-a', '--abstract', action="store_true", help="To look into abstract.")
    parser.add_argument('-n', '--topn', default=0, type=int, help="The maximum number of relevant classes.")
    parser.add_argument('-l', '--lang', default=None, help="language tag. e.g., en")
    parser.add_argument('--object-property', action="store_true",
                        help="Whether to only use object property for getting the relevant properties relenvant to the given meta")
    parser.add_argument('-m', '--maxoptions', default=0, type=int,
                        help="Maximum number of meta literal for each meta type (e.g., title)")
    parser.add_argument('-f', '--freq', action="store_true",
                        help="Use frequency to fetch the most relevant classes and properties")
    parser.add_argument('-g', '--leng', action="store_true",
                        help="Use the length to fetch the most relevant classes and properties")
    parser.add_argument('-r', '--topr', type=int, default=0, help="The maximum number of relations")
    parser.add_argument('--soft', action="store_true", help="Also include classes related to the important classes")
    parser.add_argument('--debug', action="store_true", help="To print debug information")
    args = parser.parse_args()
    parsed_args = {
        "input": args.input, "output": args.output,
        "title": args.title, "description": args.description, "abstract": args.abstract,
        "topn": args.topn, "topr": args.topr,
        "lang": args.lang, "maxoptions": args.maxoptions, "object_property": args.object_property,
        "freq": args.freq, "leng": args.leng,
        "soft": args.soft,
    }
    if args.debug:
        DEBUG = True
    fetcher.DEBUG = DEBUG
    return parsed_args


def main():
    a = datetime.now()
    args = parse_arguments()
    if args["freq"]:
        freq_workflow(input_path=args["input"], out_path=args["output"], topn=args["topn"], topr=args["topr"],
                      only_object_property=args["object_property"], soft=args["soft"])
    elif args["leng"]:
        leng_workflow(input_path=args["input"], out_path=args["output"], topn=args["topn"], topr=args["topr"],
                      soft=args["soft"])
    else:
        meta_workflow(input_path=args["input"], out_path=args["output"], topn=args["topn"], topr=args["topr"],
                      title=args["title"], desc=args["description"], abstract=args["abstract"], soft=args["soft"],
                      lang=args["lang"], max_options=args["maxoptions"], only_object_property=args["object_property"])
    b = datetime.now()
    print("\n\nTime it took: %.1f minutes\n\n" % ((b - a).total_seconds() / 60.0))


if __name__ == "__main__":
    main()
