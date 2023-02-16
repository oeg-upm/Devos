import os
import json
import argparse
import pandas as pd
from datetime import datetime
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt
from .analysis import get_rating_df

SHOW_FIG = False

METHODS = ["OntMet",'ClaFreq', "LabLen"]

def get_ontology_data(jpath):
    with open(jpath) as f:
        s = f.read()
        j = json.loads(s)

    ontology = jpath.split(os.sep)[-1].split("-")[0]
    j["ontology"] = ontology
    j["name"] = ontology[:-4].lower()
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


def is_blanknode(node):
    if len(node) > 20 and node.lower() == node:
        if node[0] == "n":
            for ch in node[1:]:
                if not ch.isdigit() and not (ch <="f" and ch >= "a"):
                    return False
            return True
    return False


def get_blanknodes(nodes):
    """
    Return the list of blanknodes from the provided list of nodes
    """

    blanknodes = []
    for node in nodes:
        if is_blanknode(node):
            blanknodes.append(node)
        #     print("**: %s" % node)
        # else:
        #     print("node: %s" % node)
    return blanknodes


def save_aggregate_data(data, output_path):
    output_file = os.path.join(output_path, "class_stats.csv")
    with open(output_file, "w") as f:
        line = "%s,%s,%s,%s,%s\n" % ("ontology", "method", "num_classes", "num_blanknodes", "num_relations")
        # print(line)
        f.write(line)
        for d in data:
            # print(type(d))
            d["blanknodes"] = get_blanknodes(d["classes"])
            d["num_classes"] = len(d["classes"])
            d["num_relations"] = len(d["relations"])
            d["num_blanknodes"] = len(d["blanknodes"])
            line = "%s,%s,%d,%d,%d\n" % (d["ontology"], d["meta"], len(d["classes"]), len(d["blanknodes"]), len(d["relations"]))
            # print(line)
            f.write(line)


def get_df_from_data(data):
    df = pd.DataFrame.from_records(data)
    df[['meta']] = df[['meta']].replace("freq", "ClaFreq")
    df[['meta']] = df[['meta']].replace("abstract", "OntMet")
    df[['meta']] = df[['meta']].replace("leng", "LabLen")
    df.rename(columns={"meta": "Technique"}, inplace=True)

    # df[df.meta=="freq"].meta="ClaFreq"
    # df[df.meta=="abstract"].meta="OntMet"
    # df[df.meta=="leng"].meta="LabLen"
    print(df)
    print(df['name'])
    # print(df["Technique"])
    return df


def attr_corr(df, attr):
    print("\n\n\n======================= %s Correlation ======================" % attr)
    for tech in METHODS:
        df_tech = df[df.Technique==tech]
        print("Pearson Correlation for %s: %f" % (tech, pearsonr(df_tech['Rating'], df_tech[attr]).statistic))
        # print("Pearson Correlation for %s: " % (tech))
        # print(pearsonr(df_tech['Rating'], df_tech[attr]))

    ax = sns.scatterplot(data=df, x=attr, y="Rating", hue="Technique", style="Technique")
    # ax = sns.lmplot(data=df, x="Length", y="Rating", hue="agg", markers=["o", "+", "x", "s"], line_kws={'ls':":"})

    ax.figure.savefig(os.path.join("userstudy", "%s_corr.svg" % attr))
    ax.figure.savefig(os.path.join("userstudy", "%s_corr.eps" % attr))

    if SHOW_FIG:
        plt.show()
    plt.clf()


def model_rating_atts(df):
    for tech in METHODS:
        print("\n------------------- Linear Regression %s Technique --------------" % tech)
        df_tech = df[df.Technique == tech]
        X, y = df_tech[['num_classes', 'num_relations', "num_blanknodes"]], df_tech[['Rating']]
        reg = LinearRegression().fit(X, y)
        print("R^2: %f" % reg.score(X, y))
        print("MSE: %f " % mean_squared_error(y, reg.predict(X)))

    # The model score for the different combination. Doesn't add much info.
    # for tech in METHODS:
    #     print("\n------------------- Linear Regression with num classes and num relations %s Technique --------------" % tech)
    #     df_tech = df[df.Technique == tech]
    #     X, y = df_tech[['num_classes', 'num_relations']], df_tech[['Rating']]
    #     reg = LinearRegression().fit(X, y)
    #     print("R^2: %f" % reg.score(X, y))
    #     print("MSE: %f " % reg.score(X, y))
    #
    #     print(mean_squared_error(y, reg.predict(X)))
    #
    # for tech in METHODS:
    #     print("\n------------------- Linear Regression with num blanknodes and num relations %s Technique --------------" % tech)
    #     df_tech = df[df.Technique == tech]
    #     X, y = df_tech[['num_relations', "num_blanknodes"]], df_tech[['Rating']]
    #     reg = LinearRegression().fit(X, y)
    #     print(reg.score(X, y))
    #     print(mean_squared_error(y, reg.predict(X)))
    #
    # for tech in METHODS:
    #     print("\n------------------- Linear Regression with num blanknodes and num classes %s Technique --------------" % tech)
    #     df_tech = df[df.Technique == tech]
    #     X, y = df_tech[['num_classes', "num_blanknodes"]], df_tech[['Rating']]
    #     reg = LinearRegression().fit(X, y)
    #     print(reg.score(X, y))
    #     print(mean_squared_error(y, reg.predict(X)))


def draw_corr(data):
    """
    Call different functions to draw different correlations
    """
    df = pd.read_csv(os.path.join("userstudy", "results.csv"))
    rating_df = get_rating_df(df)
    class_df = get_df_from_data(data)

    df = rating_df.merge(class_df, left_on=["Ontology", "Technique"], right_on=["name", "Technique"])
    model_rating_atts(df)

    attr_corr(df, "num_classes")
    attr_corr(df, "num_relations")
    attr_corr(df, "num_blanknodes")


def stat_workflow(input_path, output_path):
    """
    Workflow to generate the stats
    """
    data = get_data(input_path)
    save_aggregate_data(data, output_path)
    draw_corr(data)


def main(input_path, output_path):
    """
    Main workflow
    """
    a = datetime.now()
    stat_workflow(output_path=output_path, input_path=input_path)
    b = datetime.now()
    print("\n\nTime it took: %.1f minutes\n\n" % ((b - a).total_seconds() / 60.0))


if __name__ == "__main__":
    output_path="userstudy"
    input_path=os.path.join(".", "output")
    main(input_path, output_path)



