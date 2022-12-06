import argparse
import traceback
from ogister import gister
# from ogister.gister import meta_workflow, draw_diagrams, freq_workflow, leng_workflow
import os
import json
from datetime import datetime
import rdflib

# meta_srcs = ["title", "description", "abstract"]
meta_srcs = ["abstract"]


def save_json(json_path, classes, relations, meta):
    """
        Generate a json file of the gist. This is mainly used for evaluation purposes
    """
    j = {
        "classes": classes,
        "relations": relations,
        "meta": meta,
    }

    # json_string = json.dumps(j)
    with open(json_path, 'w') as outfile:
        json.dump(j, outfile)
        # json.dump(json_string, outfile)


def save_label_len(d, out_path):
    with open(out_path, 'w') as f:
        for k in d:
            f.write("%s,%d\n" % (k, d[k]))


def experiment(input_files, output_path, only_object_property, freq, topn, topr, leng, lang=None, max_options=0,
               soft=False):
    """
    Experiment
    """
    global meta_srcs

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    if freq:
        # meta_srcs = ["freq-%d" % topn]
        meta_srcs = ["freq"]
    elif leng:
        # meta_srcs = ["leng-%d" % topn]
        meta_srcs = ["leng"]

    for inp in input_files:
        if os.path.isdir(inp):
            print("skip: %s" % inp)
            continue
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
            elif m.startswith("leng"):
                pass
            else:
                raise Exception("invalid meta src")

            graph_fname_base = inp.split(os.sep)[-1] + "-" + m + "-%d-%d" % (topn, topr)
            if soft:
                graph_fname_base += "-soft"
            else:
                graph_fname_base += "-hard"
            check_diagram_fpath = os.path.join(output_path, graph_fname_base + ".md")
            if os.path.exists(check_diagram_fpath):
                print("\n%s already exists" % check_diagram_fpath)
                continue
            try:
                print("\n\n===== Ontology: %s =====" % inp)
                if freq:
                    classes, relations = gister.freq_workflow(input_path=inp, out_path=None, topr=topr, soft=soft,
                                                       only_object_property=only_object_property, topn=topn)
                elif leng:
                    classes, relations, class_leng_dict = gister.leng_workflow(input_path=inp, out_path=None, topn=topn,
                                                                        soft=soft,topr=topr)
                    label_len_path = os.path.join(output_path, graph_fname_base + ".csv")
                    save_label_len(class_leng_dict, label_len_path)
                else:
                    classes, relations = gister.meta_workflow(input_path=inp, out_path=None, lang=lang, soft=soft,
                                                       max_options=max_options, title=titl, desc=desc, abstract=abst,
                                                       topr=topr, topn=topn, only_object_property=only_object_property)
                gister.clear_cache()
            except Exception as e:
                print("Error processing: %s" % inp)
                print("Exception: %s" % str(e))
                traceback.print_exc()
                continue
            graph_fname = graph_fname_base
            opath = os.path.join(output_path, graph_fname + ".md")
            json_path = os.path.join(output_path, graph_fname + ".json")
            # label_path = os.path.join(output_path, graph_fname + ".csv")
            gister.draw_diagrams(classes=classes, relations=relations, out_path=opath)
            save_json(json_path, classes=classes, relations=relations, meta=m)
            # save_label_len(label_path, classes=classes)


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', nargs="+", required=True, help="ontology files")
    parser.add_argument('-o', '--output', default="output", help="Output path")
    parser.add_argument('-l', '--lang', default=None, help="language tag. e.g., en")
    parser.add_argument('-m', '--maxoptions', default=0,
                        help="Maximum number of meta literal for each meta type (e.g., title)")
    parser.add_argument('--object-property', action="store_true",
                        help="Whether to only use object property for getting the relevant properties relenvant to the given meta")
    parser.add_argument('-f', '--freq', action="store_true",
                        help="Use frequency to fetch the most relative classes and properties")
    parser.add_argument('-g', '--leng', action="store_true",
                        help="Use the length to fetch the most relevant classes and properties")
    parser.add_argument('-n', '--topn', default=0, type=int, help="The maximum number of relevant classes.")
    parser.add_argument('-r', '--topr', default=0, type=int, help="The maximum number of relations.")
    parser.add_argument('--soft', action="store_true", help="Also include classes related to the important classes")
    args = parser.parse_args()
    parsed_args = {
        "output": args.output, "input": args.input, "lang": args.lang,
        "maxoptions": int(args.maxoptions), "object_property": args.object_property,
        "freq": args.freq, "leng": args.leng,
        "topn": args.topn, "topr": args.topr,
        "soft": args.soft
    }
    return parsed_args
    # return args.output, args.input, args.lang, int(args.maxoptions), args.object_property, args.freq, args.topn, args.leng


def main():
    """
    Parse Arguments
    """
    a = datetime.now()
    # output_path, input_files, lang, max_options, only_object_property, freq, topn, leng = parse_arguments()
    args = parse_arguments()
    experiment(args["input"], args["output"], lang=args["lang"], max_options=args["maxoptions"], soft=args["soft"],
               only_object_property=args["object_property"], freq=args["freq"], topn=args["topn"], topr=args["topr"],
               leng=args["leng"])
    # experiment(input_files, output_path, lang=lang, max_options=max_options, only_object_property=only_object_property,
    #            freq=freq, topn=topn, leng=leng)
    b = datetime.now()
    print("\n\nTime it took: %.1f minutes\n\n" % ((b - a).total_seconds() / 60.0))


if __name__ == "__main__":
    main()
