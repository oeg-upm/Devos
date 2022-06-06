import argparse
from ogister.gister import workflow
import os


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', nargs="+", required=True, help="ontology files")
    parser.add_argument('-o', '--output', default="output", help="Output path")
    args = parser.parse_args()
    return args.output, args.input


def experiment(input_files, output_path):
    """
    Experiment
    """
    meta_srcs = ["title", "description", "abstract"]
    for inp in input_files:
        for m in meta_srcs:
            titl = desc = abst = False
            # desc = False
            # abst = False
            if m == "title":
                titl = True
            elif m == "description":
                titl = desc = True
            elif m == "abstract":
                titl = desc = abst = True
            else:
                raise Exception("invalid meta src")

            workflow(input_path=inp, out_path=os.path.join(output_path, inp.split(os.sep)[-1]+"-"+m+".md"),
                     title=titl, desc=desc, abstract=abst)


def main():
    """
    Parse Arguments
    """
    output_path, input_files = parse_arguments()
    experiment(input_files, output_path)


if __name__ == "__main__":
    main()

