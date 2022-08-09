import argparse
from ogister.gister import workflow, draw_diagrams, freq_workflow
import os
import json
from datetime import datetime
import rdflib

meta_srcs = ["title", "description", "abstract"]


def save_json(json_path, classes, relations, meta):
    """
        Generate a json file of the gist. This is mainly used for evaluation purposes
    """
    j = {
        "classes": classes,
        "relations": relations,
        "meta": meta,
    }

    json_string = json.dumps(j)
    with open(json_path, 'w') as outfile:
        json.dump(json_string, outfile)


def experiment(input_files, output_path, only_object_property, freq, topn, lang=None, max_options=0):
    """
    Experiment
    """
    if freq:
        meta_srcs = ["freq-%d" % topn]
    for inp in input_files:
        for m in meta_srcs:
            titl = desc = abst = False
            if m == "title":
                titl = True
            elif m == "description":
                titl = desc = True
            elif m == "abstract":
                titl = desc = abst = True
            elif m.startswith("freq"):
                pass
            else:
                raise Exception("invalid meta src")

            graph_fname_base = inp.split(os.sep)[-1]+"-"+m
            check_diagram_fpath = os.path.join(output_path, graph_fname_base + ".md")
            if os.path.exists(check_diagram_fpath):
                print("\n%s already exists" % check_diagram_fpath)
                continue
            if freq:
                classes, relations = freq_workflow(input_path=inp, out_path=None,
                                                   only_object_property=only_object_property, topn=topn)
            else:
                classes, relations = workflow(input_path=inp, out_path=None, lang=lang, max_options=max_options,
                                              title=titl, desc=desc, abstract=abst,
                                              only_object_property=only_object_property)

            graph_fname = graph_fname_base
            opath = os.path.join(output_path, graph_fname + ".md")
            json_path = os.path.join(output_path, graph_fname + ".json")
            draw_diagrams(classes=classes, relations=relations, out_path=opath)
            save_json(json_path, classes=classes, relations=relations, meta=m)


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', nargs="+", required=True, help="ontology files")
    parser.add_argument('-o', '--output', default="output", help="Output path")
    parser.add_argument('-l', '--lang', default=None, help="language tag. e.g., en")
    parser.add_argument('-m', '--maxoptions', default=0, help="Maximum number of meta literal for each meta type (e.g., title)")
    parser.add_argument('--object-property', action="store_true", help="Whether to only use object property for getting the relevant properties relenvant to the given meta")
    parser.add_argument('-f', '--freq', action="store_true", help="Use frequency to fetch the most relative classes and properties")
    parser.add_argument('-n', '--topn', default=0, type=int, help="The maximum number of relevant classes.")
    args = parser.parse_args()
    return args.output, args.input, args.lang, int(args.maxoptions), args.object_property, args.freq, args.topn


def main():
    """
    Parse Arguments
    """
    a = datetime.now()
    output_path, input_files, lang, max_options, only_object_property, freq, topn = parse_arguments()
    experiment(input_files, output_path, lang=lang, max_options=max_options, only_object_property=only_object_property, freq=freq, topn=topn)
    b = datetime.now()
    print("\n\nTime it took: %.1f minutes\n\n" % ((b - a).total_seconds() / 60.0))


if __name__ == "__main__":
    main()

