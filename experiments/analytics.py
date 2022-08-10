import os
import json
import argparse
from datetime import datetime


def get_ontology_data(jpath):
    with open(jpath) as f:
        s = f.read()
        # print("< %s >" % s)
        j = json.loads(s)
        # print(j)
        # print(type(j))



    # f = open(jpath)
    # j = json.load(f)
    # f.close()
    # print(j)
    # print(type(j))
    # print(j["meta"])
    ontology = jpath.split(os.sep)[-1].split("-")[0]
    # print("ontology: ")
    # print(ontology)
    j["ontology"] = ontology
    # print(j)
    # ".".join(jpath.split('.')[:-1])
    return j


def get_folder_data(folder_path):
    data = []
    for fname in os.listdir(folder_path):
        if fname.endswith("json"):
            data.append(get_ontology_data(os.path.join(folder_path, fname)))
    return data


def get_data(output_dir):
    data = []
    for folder_name in os.listdir(output_dir):
        folder_path = os.path.join(output_dir, folder_name)
        if os.path.isdir(folder_path):
            data += get_folder_data(folder_path)
    return data


def save_aggregate_data(data, output_path):
    output_file = os.path.join(output_path, "stats.csv")
    with open(output_file, "w") as f:
        line = "%s,%s,%s,%s\n" % ("ontology", "method", "num_classes", "num_relations")
        print(line)
        f.write(line)
        for d in data:
            print(type(d))
            line = "%s,%s,%d,%d\n" % (d["ontology"], d["meta"], len(d["classes"]), len(d["relations"]))
            print(line)
            f.write(line)


def workflow(input_path, output_path):
    data = get_data(input_path)
    save_aggregate_data(data, output_path)


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', default="output", help="The the results path")
    parser.add_argument('-o', '--output', default="output", help="The output path")
    args = parser.parse_args()
    return args.output, args.input


def main():
    """
    Parse Arguments
    """
    a = datetime.now()
    output_path, input_path = parse_arguments()
    workflow(output_path=output_path, input_path=input_path)
    b = datetime.now()
    print("\n\nTime it took: %.1f minutes\n\n" % ((b - a).total_seconds() / 60.0))


if __name__ == "__main__":
    main()



