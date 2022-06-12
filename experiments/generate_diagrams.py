import argparse
from ogister.gister import workflow
import os
import json


meta_srcs = ["title", "description", "abstract"]
top_ns = [0, 3, 4, 5]


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', nargs="+", required=True, help="ontology files")
    parser.add_argument('-o', '--output', default="output", help="Output path")
    args = parser.parse_args()
    return args.output, args.input


def save_json(json_path, classes, relations, meta, topn):
    """
        Generate a json file of the gist. This is mainly used for evaluation purposes
    """
    j = {
        "classes": classes,
        "relations": relations,
        "meta": meta,
        "topn": topn
    }

    json_string = json.dumps(j)
    with open(json_path, 'w') as outfile:
        json.dump(json_string, outfile)


def experiment(input_files, output_path):
    """
    Experiment
    """
    for inp in input_files:
        for m in meta_srcs:
            for n in top_ns:
                titl = desc = abst = False
                if m == "title":
                    titl = True
                elif m == "description":
                    titl = desc = True
                elif m == "abstract":
                    titl = desc = abst = True
                else:
                    raise Exception("invalid meta src")

                graph_fname = inp.split(os.sep)[-1]+"-"+m
                if n > 0:
                    graph_fname += "-%d" % n
                classes, relations = workflow(input_path=inp, out_path=os.path.join(output_path, graph_fname+".md"),
                                              title=titl, desc=desc, abstract=abst, topn=n)
                save_json(os.path.join(output_path, graph_fname+".json"), classes=classes, relations=relations,
                          topn=n, meta=m)


def main():
    """
    Parse Arguments
    """
    output_path, input_files = parse_arguments()
    experiment(input_files, output_path)


if __name__ == "__main__":
    main()

