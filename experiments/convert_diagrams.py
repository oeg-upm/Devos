import argparse
import os


def convert_diagram(input_path, out_format=".png"):
    mmd_input = ".".join(input_path.split(".")[:-1])+".mmd"
    with open(input_path) as f:
        m_diagram = f.read()
    m_diagram = m_diagram.replace("```mermaid", "").replace("```", "")
    with open(mmd_input, "w") as f:
        f.write(m_diagram)
    out_path = ".".join(input_path.split(".")[:-1])+out_format
    comm = "mmdc -i %s -o %s" % (mmd_input, out_path)
    print(comm)
    os.system(comm)


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Get a Gist of the ontology')
    parser.add_argument('-i', '--input', nargs="+", required=True, help="md files")
    parser.add_argument('-f', '--format', default="png", help="output file format (e.g., png, svg)")
    args = parser.parse_args()
    return args.input, args.format


def main():
    input_files, out_format = parse_arguments()
    if out_format[0] != ".":
        out_format = "."+out_format
    for inp in input_files:
        convert_diagram(inp, out_format)


if __name__ == "__main__":
    main()



