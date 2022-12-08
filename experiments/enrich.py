import argparse
from datetime import datetime
import os
from devos import enricher


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', nargs="+", required=True, help="ontology files")
    parser.add_argument('-o', '--output', default="output", help="Output path")

    args = parser.parse_args()
    parsed_args = {
        "output": args.output, "input": args.input,
    }
    return parsed_args


def enrich_ontologies(input_files, output_dir):
    for inp in input_files:
        out_file_dir = os.path.join(output_dir, inp.split(os.sep)[-1])
        if os.path.exists(out_file_dir):
            print("%s already exists" % out_file_dir)
            continue

        if os.path.isfile(inp) and out_file_dir.split('.')[-1].lower() in ['xml', 'owl', 'rdf', 'ttl']:
            try:
                print("Processing: %s" % inp)
                enricher.enrichment_workflow(inp, out_file_dir)
                print("Saving the enriched ontology: %s" % out_file_dir)
            except Exception as e:
                print("Error processing: %s" % inp)
                print(str(e))


def main():
    """
    Parse Arguments
    """
    a = datetime.now()
    args = parse_arguments()
    enrich_ontologies(args["input"], args["output"])
    b = datetime.now()
    print("\n\nTime it took: %.1f minutes\n\n" % ((b - a).total_seconds() / 60.0))


if __name__ == "__main__":
    main()
