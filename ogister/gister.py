import argparse
import sys
import rdflib

from owl2diagram.main import get_class_diagram, get_class_hierarchy_diagram, get_object_diagram, get_data_diagram, get_data_prop
from owl2diagram.main import get_classes, get_class_hierarchy, get_object_prop, save_diagram, get_name


try:
    import prefixes
except:
    from ogister import prefixes


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


def get_prop_vals(g, properties):
    """
    Get values about the graph itself
    :param g: rdf Graph
    :param properties:
    :return: return values
    """
    vals = []
    t = "select ?val where {?s <%s> ?val}"
    for p in properties:
        results = g.query(t % p)
        for res in results:
            vals.append(str(res["val"]))
    return vals


def get_titles(g):
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
    return get_prop_vals(g, props)


def get_descriptions(g):
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
    return get_prop_vals(g, props)


def get_abstracts(g):
    """
    According to https://dgarijo.github.io/Widoco/doc/bestPractices/index-en.html#abs
    :param g: rdf Graph
    :return: a list of abstracts
    """
    props = [
        prefixes.DC+"abstract",
        prefixes.DCTERMS+"abstract"
    ]
    return get_prop_vals(g, props)


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

    args = parser.parse_args()
    return args.input, args.output, args.title, args.description, args.abstract


def workflow(input_path, out_path, title, desc, abstract):
    """

    """
    g = rdflib.Graph()
    g.parse(input_path, format=rdflib.util.guess_format(input_path))
    meta = []
    if title:
        meta += get_titles(g)
        print(get_titles(g))
    if desc:
        meta += get_descriptions(g)
        print(get_descriptions(g))
    if abstract:
        meta += get_abstracts(g)
        print(get_abstracts(g))
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
    print(related_classes)
    all_classes = classes+related_classes
    all_classes = list(set(all_classes))
    relations = get_relations(g, all_classes)
    constraints = get_classes_constraints(g, all_classes)
    constraints = [(shorten_url(c[0]), shorten_url(c[1]), shorten_url(c[2])) for c in constraints]
    shortened_classes = [shorten_url(c) for c in classes+related_classes]
    diagram = get_class_diagram(shortened_classes)
    diagram += get_object_diagram(relations)
    diagram += get_object_diagram(constraints)
    save_diagram(diagram, out_path)


def main():
    input_path, out_path, title, desc, abstract = parse_arguments()
    workflow(input_path=input_path, out_path=out_path, title=title, desc=desc, abstract=abstract)


if __name__ == "__main__":
    main()
