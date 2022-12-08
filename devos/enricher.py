from ogister import fetcher
from ogister import gister
import rdflib
from rdflib.namespace import RDFS
import argparse


DEBUG = False


def class_name_to_label(class_name):
    """
    Given a class name (e.g., UnitedKingdom), this function will generate a more natural
    label (e.g., United Kingdom) with spaces appropriately added.
    """
    if class_name.isupper():
        return class_name
    tokens = []
    start = 0
    for i in range(1, len(class_name)):
        if class_name[i].isupper():
            t = class_name[start:i]
            tokens.append(t)
            start = i
    t = class_name[start:len(class_name)]
    tokens.append(t)
    label = " ".join(tokens)
    return label


def add_label_to_class(g, class_uri):
    """
    Add labels for the given class
    """
    if not fetcher.get_labels(g, class_uri):
        class_name = class_uri.split('/')[-1].split('#')[-1]
        label = class_name_to_label(class_name)
        if DEBUG:
            print("%s => %s" % (class_name, label))
        g.add((rdflib.URIRef(class_uri), rdflib.URIRef(RDFS.label), rdflib.Literal(label)))
    else:
        if DEBUG:
            print("a label already exists for %s" % class_uri)


def add_labels_to_classes(g, classes):
    """
    Add labels to all the given classes
    """
    for c in classes:
        add_label_to_class(g, str(c))


def enrichment_workflow(input_ont, output_ont):
    print("input_ont: %s" % input_ont)
    g = gister.parse_ontology(input_ont)
    classes = fetcher.get_all_classes(g)
    add_labels_to_classes(g, classes)
    if output_ont:
        if DEBUG:
            print("output path: %s" % output_ont)
        g.serialize(destination=output_ont, format=rdflib.util.guess_format(input_ont))


def parse_arguments():
    """
    Parse command line arguments
    """
    global DEBUG
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', required=True, help="Ontology file.")
    parser.add_argument('-o', '--output', help="Output file.")
    parser.add_argument('--debug', action="store_true", help="To print debug information")
    args = parser.parse_args()
    parsed_args = {"input": args.input, "output": args.output}
    if args.debug:
        DEBUG = True
    fetcher.DEBUG = DEBUG
    gister.DEBUG = DEBUG
    return parsed_args


def main():
    args = parse_arguments()
    enrichment_workflow(args["input"], args["output"])


if __name__ == "__main__":
    main()