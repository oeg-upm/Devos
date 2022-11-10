from ogister import prefixes
import rdflib
from rdflib import Literal
from owl2diagram.main import get_classes, get_class_hierarchy, get_object_prop, save_diagram, get_name


def shorten_url(url):
    for pref in prefixes.prefs:
        if url.startswith(prefixes.prefs[pref]):
            return url.replace(prefixes.prefs[pref], pref)
    return get_name(url)


def remove_datatypes(uris):
    filtered = []
    for u in uris:
        if prefixes.XSD not in u and prefixes.SKOS not in u:
            filtered.append(u)
        else:
            print("ignore: %s" % u)
    return filtered


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


def get_class_freq(g, only_object_property):
    if only_object_property:
        t = "select ?class (COUNT(?property) as ?num ) where { ?property rdf:type owl:ObjectProperty.  %s } group by ?class"
    else:
        t = "select ?class (COUNT(?property) as ?num )  where { ?a ?property ?b.  %s } group by ?class"
    # Domain
    q = t % """ {?property rdfs:domain ?class.}"""

    # q = """select (count(?s) as ?c) ?p where {?s ?p ?o}"""
    results = g.query(q)
    d = dict()
    for res in results:
        class_uri = str(res["class"])
        num = int(str(res["num"]))
        if class_uri not in d:
            d[class_uri] = 0
        d[class_uri] += num
    # range
    q = t % """ {?property rdfs:range ?class.}"""
    results = g.query(q)
    d = dict()
    for res in results:
        class_uri = str(res["class"])
        num = int(str(res["num"]))
        if class_uri not in d:
            d[class_uri] = 0
        d[class_uri] += num
    return d


def get_class_leng(g, label_uris=["rdfs:label", "rdfs:comment", "%sdefinition" % prefixes.SKOS]):
    """
    """
    label_uris_formatted = []
    for uri in label_uris:
        if uri.startswith('http'):
            label_uris_formatted.append("<"+uri+">")
        else:
            label_uris_formatted.append(uri)

    label_uris_sparql = ", ".join(label for label in label_uris_formatted)
    # q = "select ?class ?label where { [] a ?class. FILTER (?class IN ( %s )) }" % label_uris_sparql
    q = "select ?class ?label where { [] a ?class. ?class ?p ?label. FILTER (?p IN ( %s )) }" % label_uris_sparql
    print("query: %s" % q)
    results = g.query(q)
    d = dict()
    for res in results:
        class_uri = str(res["class"])
        num = len(res["label"].split(' '))
        if class_uri not in d:
            d[class_uri] = 0
        d[class_uri] = max(d[class_uri], num)

    return d


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
    t = "select ?class where {[] a ?class .  %s }"
    # t = "select ?class where { ?class a owl:Class.  %s }"

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


def get_properties_with_keyword(g, keyword, only_object_property=True):
    """
    Get existing labels from a given uri.
    This follows the recommendation https://dgarijo.github.io/Widoco/doc/bestPractices/index-en.html#title
    :param g: rdf Graph
    :param keyword:
    :param only_object_property:
    :return:
    """
    props = [
        prefixes.RDFS+"label",
        prefixes.SKOS+"prefLabel",
        prefixes.OBO+"IAO_0000118"
    ]
    vals = []
    if only_object_property:
        t = "select ?property where { ?property rdf:type owl:ObjectProperty.  %s }"
    else:
        t = "select ?property where { ?a ?property ?b.  %s }"
    label_query_template = "{?property <%s> ?label. FILTER CONTAINS(lcase(?label), \"%s\") }"
    label_query = ""
    for p in props[:-1]:
        label_query += label_query_template % (p, keyword)
        label_query += " UNION "
    label_query += label_query_template % (props[-1], keyword)
    q = t % label_query
    results = g.query(q)
    for res in results:
        vals.append(str(res["property"]))

    return vals


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
                    continue
            vals.append(str(res["val"]))
    return vals


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


def get_relations(g, classes):
    relations = []
    for class_uri in classes:
        relations += get_class_relation(g, class_uri)
    relations = list(set(relations))
    return relations


def get_properties_relations(g, properties):
    relations = []
    for property_uri in properties:
        relations += get_property_relation(g, property_uri)
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


def get_property_relation(g, property_uri):
    relations = []
    class_as_domain = """ select ?domain ?range where { 
      <%s> rdfs:domain ?domain.
      <%s> rdfs:range ?range.
    }"""
    q = class_as_domain % (property_uri, property_uri)
    results = g.query(q)
    for r in results:
        rel = (shorten_url(r["domain"]), property_uri, shorten_url(r["range"]))
        relations.append(rel)
    return relations