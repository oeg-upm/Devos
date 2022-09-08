# import argparse
# from ogister.gister import workflow, draw_diagrams, get_top, get_relations, get_classes_constraints
# import os
# import json
# from datetime import datetime
# import rdflib
#
# meta_srcs = ["title", "description", "abstract"]
# top_ns = [0, 3, 4, 5]
#
#
# def save_json(json_path, classes, relations, meta, topn):
#     """
#         Generate a json file of the gist. This is mainly used for evaluation purposes
#     """
#     j = {
#         "classes": classes,
#         "relations": relations,
#         "meta": meta,
#         "topn": topn
#     }
#
#     json_string = json.dumps(j)
#     with open(json_path, 'w') as outfile:
#         json.dump(json_string, outfile)
#
#
# def experiment(input_files, output_path, lang=None, max_options=0):
#     """
#     Experiment
#     """
#     for inp in input_files:
#         for m in meta_srcs:
#             titl = desc = abst = False
#             if m == "title":
#                 titl = True
#             elif m == "description":
#                 titl = desc = True
#             elif m == "abstract":
#                 titl = desc = abst = True
#             else:
#                 raise Exception("invalid meta src")
#
#             graph_fname_base = inp.split(os.sep)[-1]+"-"+m
#             check_diagram_fpath = os.path.join(output_path, graph_fname_base + ".md")
#             if os.path.exists(check_diagram_fpath):
#                 print("\n%s already exists" % check_diagram_fpath)
#                 continue
#             classes, relations = workflow(input_path=inp, out_path=None, lang=lang, max_options=max_options,
#                      title=titl, desc=desc, abstract=abst, topn=0)
#             for n in top_ns:
#                 graph_fname = graph_fname_base
#                 if n > 0:
#                     graph_fname = graph_fname_base + "-meta" + "-%d" % n
#
#                 top_classes, top_relations = get_top(topn=n, classes=classes, relations=relations)
#                 opath = os.path.join(output_path, graph_fname + ".md")
#                 json_path = os.path.join(output_path, graph_fname + ".json")
#                 draw_diagrams(classes=top_classes, relations=top_relations, out_path=opath)
#                 save_json(json_path, classes=top_classes, relations=top_relations, topn=n, meta=m)
#
#
# def high_freq_experiment(input_files, output_path):
#     """
#     Experiment to include only classes with the highest connections
#     """
#
#     def get_all_relations(g):
#         """
#         Get all relations
#         :param g: rdf Graph
#         :return:
#             relations
#         """
#         classes = []
#         t = """select ?class where {?class a owl:Class}"""
#         results = g.query(t)
#         for res in results:
#             classes.append(str(res["class"]))
#         classes = list(set(classes))
#         constraints = get_classes_constraints(g, classes)
#         rels = get_relations(g, classes)
#         return rels+constraints
#
#     for inp in input_files:
#         g = rdflib.Graph()
#         print(
#             "\n\n\t\t==============\n\t Rel Parsing: %s (format: %s)" % (inp, rdflib.util.guess_format(inp)))
#         g.parse(inp, format=rdflib.util.guess_format(inp))
#
#         graph_fname_base = inp.split(os.sep)[-1]+"-freq"
#         check_diagram_fpath = os.path.join(output_path, graph_fname_base + ".md")
#         if os.path.exists(check_diagram_fpath):
#             print("\n%s already exists" % check_diagram_fpath)
#             continue
#
#         relations = get_all_relations(g)
#         classes = []
#         for n in top_ns:
#             if n > 0:
#                 graph_fname = graph_fname_base + "-%d" % n
#                 top_classes, top_relations = get_top(topn=n, classes=classes, relations=relations)
#                 opath = os.path.join(output_path, graph_fname + ".md")
#                 json_path = os.path.join(output_path, graph_fname + ".json")
#                 draw_diagrams(classes=top_classes, relations=top_relations, out_path=opath)
#                 save_json(json_path, classes=top_classes, relations=top_relations, topn=n, meta="freq")
#
#
# def parse_arguments():
#     """
#     Parse command line arguments
#     """
#     parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
#     parser.add_argument('-i', '--input', nargs="+", required=True, help="ontology files")
#     parser.add_argument('-o', '--output', default="output", help="Output path")
#     parser.add_argument('-l', '--lang', default=None, help="language tag. e.g., en")
#     parser.add_argument('-m', '--maxoptions', default=0, help="Maximum number of meta literal for each meta type (e.g., title)")
#     parser.add_argument('-f', '--freq', action="store_true", help="Whether to use high frequency and ignore meta")
#     args = parser.parse_args()
#     return args.output, args.input, args.lang, int(args.maxoptions), args.freq
#
#
# def main():
#     """
#     Parse Arguments
#     """
#     a = datetime.now()
#     output_path, input_files, lang, max_options, freq = parse_arguments()
#     if freq:
#         high_freq_experiment(input_files, output_path)
#     else:
#         experiment(input_files, output_path, lang=lang, max_options=max_options)
#     b = datetime.now()
#     print("\n\nTime it took: %.1f minutes\n\n" % ((b - a).total_seconds() / 60.0))
#
#
# if __name__ == "__main__":
#     main()
#
