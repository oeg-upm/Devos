import argparse
import sys
import rdflib
from rdflib import Literal
import json
from owl2diagram.main import get_class_diagram, get_class_hierarchy_diagram, get_object_diagram, get_data_diagram, get_data_prop
from owl2diagram.main import get_classes, get_class_hierarchy, get_object_prop, save_diagram, get_name
from collections import Counter
from datetime import datetime

try:
    import prefixes
except:
    from ogister import prefixes


MAX_CHARS = 300


def remove_datatypes(uris):
    filtered = []
    for u in uris:
        if prefixes.XSD not in u and prefixes.SKOS not in u:
            filtered.append(u)
        else:
            print("ignore: %s" % u)
    return filtered


def remove_quotes(keywords):
    return [k.replace('"', '') for k in keywords]


def shorten_url(url):
    for pref in prefixes.prefs:
        if url.startswith(prefixes.prefs[pref]):
            return url.replace(prefixes.prefs[pref], pref)
    return get_name(url)


def gather_keywords(meta, max_tok_len):
    """
    get_possible_keywords from a list
    meta: list of meta texts. Each text represent a meta data string
    Return a list of keywords
    """
    keywords = []
    for m in meta:
        keywords += get_possible_keywords(m, max_tok_len=max_tok_len)
    return keywords


def get_possible_keywords(txt, max_tok_len):
    """
    Return possible combinations of keywords based on
    """
    tokens = txt.split(' ')
    tokens = [t.strip() for t in tokens if t.strip()!= '']
    keywords = []
    for i in range(len(tokens)):
        kw_i = get_possible_combinations(tokens[i:max_tok_len+i], max_tok_len)
        keywords += kw_i
    return keywords


def get_possible_combinations(tokens, max_tok_len):
    combs = []
    new_tok_max_len = min(len(tokens), max_tok_len)
    for i in range(new_tok_max_len, 0, -1):
        c = get_possible_joins(tokens[:i])
        combs += c
    return combs


# def get_possible_joins(tokens, joiners=[" ", "", "."]):
def get_possible_joins(tokens, joiners=[" "]):

    """
    Different characters to join the tokens
    """
    if len(tokens) == 1:
        return tokens

    poss = []  # possibilities
    for merged_tokens in get_possible_joins(tokens[1:], joiners=joiners):
        for j in joiners:
            t = tokens[0] + j + merged_tokens
            poss.append(t)
    return poss


def get_prop_vals(g, properties, lang=None):
    """
    Get values about the graph itself
    :param g: rdf Graph
    :param properties:
    :param lang:
    :return: return values
    """
    vals = []
    t = "select ?val where {?s <%s> ?val. ?s rdf:type owl:Ontology}"
    for p in properties:
        results = g.query(t % p)
        for res in results:
            if lang:
                if not res["val"].language or (type(res["val"]) == Literal and res["val"].language.lower() != lang.lower()):
                # if type(res["val"]) == Literal and res["val"].language.lower() != lang.lower():
                    continue
            # literal = res["val"]
            # if litera
            # print(res)
            # print(res[1])
            # print(res['val']["lang"])
            vals.append(str(res["val"]))
    return vals


def get_titles(g, lang=None):
    """
    According to https://dgarijo.github.io/Widoco/doc/bestPractices/index-en.html#title
    :param g: rdf Graph
    :return: a list of titles
    """
    props = [
        prefixes.DC+"title",
        prefixes.DCTERMS+"title",
        prefixes.SCHEMA+"name"
    ]
    return get_prop_vals(g, props, lang=lang)


def get_descriptions(g, lang=None):
    """
    According to https://dgarijo.github.io/Widoco/doc/bestPractices/index-en.html#description
    :param g: rdf Graph
    :return: a list of descriptions
    """
    props = [
        prefixes.DC+"description",
        prefixes.DCTERMS+"description",
        prefixes.SCHEMA+"description",
        prefixes.RDFS+"comment",
        prefixes.SKOS+"note"
    ]
    return get_prop_vals(g, props, lang=lang)


def get_abstracts(g, lang=None):
    """
    According to https://dgarijo.github.io/Widoco/doc/bestPractices/index-en.html#abs
    :param g: rdf Graph
    :return: a list of abstracts
    """
    props = [
        prefixes.DC+"abstract",
        prefixes.DCTERMS+"abstract"
    ]
    return get_prop_vals(g, props, lang=lang)


def classes_with_keywords(g, keywords):
    """
    Get classes matches any of the provided keywords
    """
    classes = []
    for k in keywords:
        classes += get_classes_with_keyword(g, k)
    return classes


def classes_related_to_properties_with_keywords(g, keywords):
    """
    Get classes related to properties which is relevant to the provided keywords
    """
    classes = []
    for k in keywords:
        classes += get_classes_related_to_properties_with_keyword(g, k)
    return classes


def get_classes_related_to_properties_with_keyword(g, keyword):
    """
    Get classes related to properties relevant to the given keyword
    This follows the recommendation https://dgarijo.github.io/Widoco/doc/bestPractices/index-en.html#title
    :param g: rdf Graph
    :param keyword:
    :return:
    """
    props = [
        prefixes.RDFS+"label",
        prefixes.SKOS+"prefLabel",
        prefixes.OBO+"IAO_0000118"
    ]
    vals = []
    t = "select ?class where { ?class a owl:Class. { {?prop rdfs:domain ?class} UNION {?prop rdfs:range ?class} }  %s }"
    label_query_template = "{?prop <%s> ?label. FILTER CONTAINS(lcase(?label), \"%s\") }"
    label_query = ""
    for p in props[:-1]:
        label_query += label_query_template % (p, keyword)
        label_query += " UNION "
    label_query += label_query_template % (props[-1], keyword)
    results = g.query(t % label_query)
    for res in results:
        vals.append(str(res["class"]))

    return vals


def get_classes_with_keyword(g, keyword):
    """
    Get existing labels from a given uri.
    This follows the recommendation https://dgarijo.github.io/Widoco/doc/bestPractices/index-en.html#title
    :param g: rdf Graph
    :param keyword:
    :return:
    """
    props = [
        prefixes.RDFS+"label",
        prefixes.SKOS+"prefLabel",
        prefixes.OBO+"IAO_0000118"
    ]
    vals = []
    t = "select ?class where { ?class a owl:Class.  %s }"

    label_query_template = "{?class <%s> ?label. FILTER CONTAINS(lcase(?label), \"%s\") }"
    label_query = ""
    for p in props[:-1]:
        label_query += label_query_template % (p, keyword)
        label_query += " UNION "
    label_query += label_query_template % (props[-1], keyword)
    q = t % label_query
    results = g.query(q)
    for res in results:
        vals.append(str(res["class"]))

    return vals


def get_relations(g, classes):
    relations = []
    for class_uri in classes:
        relations += get_class_relation(g, class_uri)
    relations = list(set(relations))
    return relations


def get_classes_constraints(g, classes):
    """
    Return constraints which is kind of a relation
    """
    consts = []
    print("\n\nget_classes_constraints> classes: ")
    print(classes)
    for class_uri in classes:
        print("\t%s" % str(class_uri))
        consts += get_class_constraints(g, class_uri)
    consts = list(set(consts))
    return consts


def get_class_constraints(g, class_uri):
    """

    A compact query of
        SELECT ?domain ?prop ?range WHERE{
        ?domain rdf:type owl:Class.
        ?range rdf:type owl:Class.
        ?domain rdfs:subClassOf ?blank.
        ?blank rdf:type owl:Restriction.
        ?blank owl:onProperty ?prop.
        ?blank owl:allValuesFrom ?range  .
        }

        with the domain and range substituted. And also tested with owl:equivalentClass
    """
    data = dict()
    for restr in ["owl:allValuesFrom", "owl:someValuesFrom"]:
        q_domain = """ SELECT ?prop ?range WHERE{
                {
                ?range rdf:type owl:Class.
                <%s> rdfs:subClassOf [ rdf:type owl:Restriction ;
                owl:onProperty ?prop ;
                %s ?range ] .
                } UNION
                {
                ?range rdf:type owl:Class.
                <%s> owl:equivalentClass [ rdf:type owl:Restriction ;
                owl:onProperty ?prop ;
                owl:allValuesFrom ?range ] .
                }
            }
            """ % (class_uri, restr, class_uri)

        q_range = """ SELECT ?domain ?prop WHERE{
                {
                ?domain rdf:type owl:Class.
                ?domain rdfs:subClassOf [ rdf:type owl:Restriction ;
                owl:onProperty ?prop ;
                %s <%s> ] .
                } UNION
                {
                ?domain rdf:type owl:Class.
                ?domain owl:equivalentClass [ rdf:type owl:Restriction ;
                owl:onProperty ?prop ;
                owl:allValuesFrom <%s> ] .
                }
            }
            """ % (restr, class_uri, class_uri)
        # print(q_domain)
        results = g.query(q_domain)
        for r in results:
            data.setdefault(shorten_url(r["prop"]), []).append(shorten_url(class_uri))
            data.setdefault(shorten_url(r["prop"]), []).append(shorten_url(r["range"]))

        results = g.query(q_range)
        for r in results:
            data.setdefault(shorten_url(r["prop"]), []).append(shorten_url(r["domain"]))
            data.setdefault(shorten_url(r["prop"]), []).append(shorten_url(class_uri))
    return data


def get_class_relation(g, class_uri):
    relations = []
    class_as_domain = """ select ?prop ?range where { 
      ?prop rdf:type owl:ObjectProperty.
      ?prop rdfs:domain <%s>.
      ?prop rdfs:range ?range
    }"""
    results = g.query(class_as_domain % class_uri)
    for r in results:
        rel = (shorten_url(class_uri), shorten_url(r["prop"]), shorten_url(r["range"]))
        relations.append(rel)
        # data.setdefault(shorten_url(r["prop"]), []).append(shorten_url(class_uri))
        # data.setdefault(shorten_url(r["prop"]), []).append(shorten_url(r["range"]))

    class_as_range = """ select ?prop ?domain where { 
      ?prop rdf:type owl:ObjectProperty.
      ?prop rdfs:domain ?domain.
      ?prop rdfs:range <%s>.
    }"""
    results = g.query(class_as_range % class_uri)
    for r in results:
        rel = (shorten_url(r["domain"]), shorten_url(r["prop"]), shorten_url(class_uri))
        relations.append(rel)
    return relations


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', required=True, help="Ontology file.")
    parser.add_argument('-o', '--output', required=True, help="Output file.")
    parser.add_argument('-t', '--title', action="store_true", help="To look into titles.")
    parser.add_argument('-d', '--description', action="store_true", help="To look into description.")
    parser.add_argument('-a', '--abstract', action="store_true", help="To look into abstract.")
    parser.add_argument('-n', '--topn', default=0,  help="The maximum number of relevant classes.")
    parser.add_argument('-l', '--lang', default=None, help="language tag. e.g., en")
    parser.add_argument('-m', '--maxoptions', default=0, help="Maximum number of meta literal for each meta type (e.g., title)")
    # parser.add_argument('-y', '--charlimit', default=0, help="Maximum number of characters per literal property.")
    args = parser.parse_args()
    return args.input, args.output, args.title, args.description, args.abstract, int(args.topn), args.lang, int(args.maxoptions)


def get_classes_and_relations(input_path, title, desc, abstract, lang=None, max_options=0):
    """

    """
    g = rdflib.Graph()
    print("\n\n\t\t==============\n\t Parsing: %s (format: %s)" % (input_path, rdflib.util.guess_format(input_path)))
    g.parse(input_path, format=rdflib.util.guess_format(input_path))
    meta = []
    if title:
        titles = get_titles(g, lang=lang)
        if max_options > 0:
            print("%d of titles out of %d" % (min(max_options, len(titles)), len(titles)))
            titles = titles[:max_options]
        meta += titles
        print("titles: ")
        # print(len(titles))
        print(titles)
    if desc:
        descs = get_descriptions(g, lang=lang)
        if max_options > 0:
            print("%d of descriptions out of %d" % (min(max_options, len(descs)), len(descs)))
            descs = descs[:max_options]
        meta += descs
        print("descriptions: ")
        # print(len(descs))
        print(descs)
    if abstract:
        absts = get_abstracts(g, lang=lang)
        if max_options > 0:
            print("%d of abstracts out of %d" % (min(max_options, len(absts)), len(absts)))
            absts = absts[:max_options]
        meta += absts
        print("abstracts")
        print(absts)

    keywords = gather_keywords(meta, max_tok_len=3)
    print("Keywords: ")
    print(keywords)

    keywords = remove_datatypes(keywords)
    keywords = remove_quotes(keywords)
    keywords = [k.lower() for k in keywords]
    keywords = [k.replace('\n', ' ').replace('\t', ' ') for k in keywords]
    keywords = list(set(keywords))
    # print("Lowercased: ")
    # print(keywords)
    classes = classes_with_keywords(g, keywords)
    classes = list(set(classes))
    classes = remove_datatypes(classes)
    print("classes: ")
    print(classes)
    related_classes = classes_related_to_properties_with_keywords(g, keywords)
    related_classes = list(set(related_classes))
    related_classes = remove_datatypes(related_classes)
    print("classes related to relevant properties: ")

    all_classes = classes+related_classes
    all_classes = list(set(all_classes))
    relations = get_relations(g, all_classes)
    constraints = get_classes_constraints(g, all_classes)
    constraints = [(shorten_url(c[0]), shorten_url(c[1]), shorten_url(c[2])) for c in constraints]
    shortened_classes = [shorten_url(c) for c in all_classes]

    # if topn > 0:
    #     from_classes = [elem[0] for elem in relations]
    #     to_classes = [elem[2] for elem in relations]
    #     to_from_classes = from_classes + to_classes
    #     myslist = Counter(to_from_classes)
    #     myslist = myslist.most_common()
    #     myslist = myslist[:topn]
    #     print("\n top %d: " % topn)
    #     print(myslist)  # Class ordered by ObjectProp relations
    #     top_classes = []
    #     for key, value in myslist:
    #         top_classes.append(key)
    #     shortened_classes = top_classes
    #     relations = [rel for rel in relations if ((rel[0] in shortened_classes) and (rel[2] in shortened_classes))]
    #     constraints = [rel for rel in constraints if ((rel[0] in shortened_classes) and (rel[2] in shortened_classes))]

    # diagram = get_class_diagram(shortened_classes)
    # diagram += get_object_diagram(relations)
    # diagram += get_object_diagram(constraints)
    # save_diagram(diagram, out_path)

    return shortened_classes, relations+constraints


def get_top(topn, classes, relations):
    """
    topn: int
    classes: shorten classes
    relations: a list of [cls1, rel, cls2]

    return topn classes and properties

    """
    if topn > 0:
        from_classes = [elem[0] for elem in relations]
        to_classes = [elem[2] for elem in relations]
        to_from_classes = from_classes + to_classes
        myslist = Counter(to_from_classes)
        myslist = myslist.most_common()
        myslist = myslist[:topn]
        print("\n top %d: " % topn)
        print(myslist)  # Class ordered by ObjectProp relations
        top_classes = []
        for key, value in myslist:
            top_classes.append(key)
        classes = top_classes
        relations = [rel for rel in relations if ((rel[0] in classes) and (rel[2] in classes))]

    return classes, relations


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


def workflow(input_path, title, desc, abstract, topn, out_path=None, lang=None, max_options=0):
    """
    meta: either "title", "description", or "abstract". It is only used for the json files
    """
    classes, relations = get_classes_and_relations(input_path, title, desc, abstract, lang=lang,
                                                   max_options=max_options)

    classes_top, relations_top = get_top(topn=topn, classes=classes, relations=relations)
    if out_path:
        draw_diagrams(classes=classes_top, relations=relations_top, out_path=out_path)
    return classes_top, relations_top


def main():
    a = datetime.now()
    input_path, out_path, title, desc, abstract, topn, lang, max_options = parse_arguments()
    workflow(input_path=input_path, out_path=out_path, title=title, desc=desc, abstract=abstract, topn=topn,
             lang=lang, max_options=max_options)
    b = datetime.now()
    print("\n\nTime it took: %.1f minutes\n\n" % ((b - a).total_seconds() / 60.0))



if __name__ == "__main__":
    main()
