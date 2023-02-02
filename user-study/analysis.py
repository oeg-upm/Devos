import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import itertools
import os
from scipy.stats import pearsonr
from devos.gister import get_meta_text
from devos import fetcher
import rdflib
import numpy as np
from collections import Counter

SHOW_FIG = False
# sns.set_theme(style="whitegrid", font_scale=1.2)


def methods_comparison_mean(df):
    ontologies = list(set(df['Ontology']))
    df_balanced = pd.DataFrame(columns=['Ontology','M', 'F', 'L'])
    for ont in ontologies:
        dfo = df[df.Ontology == ont]
        dfo_mean = dfo.mean(numeric_only=True).to_frame().T
        dfo_mean['Ontology'] = ont
        print(dfo_mean)
        df_balanced = pd.concat([df_balanced, dfo_mean], ignore_index=True)
    print(df_balanced)
    df_balanced_mean = df_balanced.mean(numeric_only=True).to_frame().T
    print("And the normalized mean is: ")
    print(df_balanced_mean)

    df = pd.DataFrame(columns=['Ontology', 'Technique', 'Rating'])
    for id, row in df_balanced.iterrows():
        df_row1 = pd.DataFrame([[row['Ontology'], 'Meta' , row['M']]],columns=['Ontology', 'Technique', 'Rating'])
        df_row2 = pd.DataFrame([[row['Ontology'], 'Freq' , row['F']]],columns=['Ontology', 'Technique', 'Rating'])
        df_row3 = pd.DataFrame([[row['Ontology'], 'Leng' , row['L']]],columns=['Ontology', 'Technique', 'Rating'])
        df = pd.concat([df, df_row1, df_row2, df_row3], ignore_index=True)
    print(df)

    df = pd.DataFrame(columns=['Ontology', 'Technique', 'Rating'])
    for id, row in df_balanced.iterrows():
        df_row1 = pd.DataFrame([[row['Ontology'], 'OntMet' , row['M']]],columns=['Ontology', 'Technique', 'Rating'])
        df_row2 = pd.DataFrame([[row['Ontology'], 'ClaFreq' , row['F']]],columns=['Ontology', 'Technique', 'Rating'])
        df_row3 = pd.DataFrame([[row['Ontology'], 'LabLen' , row['L']]],columns=['Ontology', 'Technique', 'Rating'])
        df = pd.concat([df, df_row1, df_row2, df_row3], ignore_index=True)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax = sns.barplot(
        data=df,
        x="Ontology", y="Rating", hue="Technique",
        # palette="dark",
        # palette="mako",
        palette="mako",
        ax=ax,
        # pallette="Spectral"
    )

    df_avg_per_ont = df

    hatches = ["-", "\\\\", "++"]
    # Loop over the bars
    for bars, hatch in zip(ax.containers, hatches):
        # Set a different hatch for each group of bars
        for bar in bars:
            bar.set_hatch(hatch)
            bar.set_edgecolor([1, 1, 1])

    plt.ylabel("Avg. Rating")
    fig.tight_layout()
    ax.legend(loc='lower left', fancybox=True)

    ax.figure.savefig(os.path.join("user-study", "per-ontology.svg"))
    ax.figure.savefig(os.path.join("user-study", "per-ontology.eps"))

    # ax.figure.savefig("per-ontology.svg")
    # ax.figure.savefig("per-ontology.eps")
    if SHOW_FIG:
        plt.show()

    plt.clf()
    draw_mean(df)
    return df_avg_per_ont

def draw_mean(df):
    """
    Draw the mean for each technique
    """
    fig, ax = plt.subplots(figsize=(5, 5))
    ax = sns.barplot(
        data=df,
        y="Technique", x="Rating", #Shue="Technique",
        # palette="dark",
        # palette="mako",
        palette="mako",
        errorbar=None,
        ax=ax,
        # pallette="Spectral"
    )
    # hatches = ["-", "\\", "+"]
    hatches = ["--", "\\\\", "++"]
    # Loop over the bars
    for bars, hatch_ in zip(ax.containers, hatches):
        # Set a different hatch for each group of bars
        for bar, hatch in zip(bars, hatches):
            bar.set_hatch(hatch)
            bar.set_edgecolor([1, 1, 1])
    plt.ylabel("Avg. Rating")
    fig.tight_layout()
    plt.legend(loc='lower left',handles=ax.containers[0], labels=["OntMet", "ClaFreq", "LabLen"])

    ax.figure.savefig(os.path.join("user-study", "mean.svg"))
    ax.figure.savefig(os.path.join("user-study", "mean.eps"))
    # ax.figure.savefig("mean.svg")
    # ax.figure.savefig("mean.eps")
    if SHOW_FIG:
        plt.show()
    plt.clf()


def methods_comparison_median(df):
    ontologies = list(set(df['Ontology']))
    df_balanced = pd.DataFrame(columns=['Ontology','M', 'F', 'L'])
    for ont in ontologies:
        dfo = df[df.Ontology == ont]
        dfo_median = dfo.median(numeric_only=True).to_frame().T
        dfo_median['Ontology'] = ont
        print(dfo_median)
        df_balanced = pd.concat([df_balanced, dfo_median], ignore_index=True)
    print(df_balanced)
    print("And the normalized median is: ")
    print(df_balanced.median(numeric_only=True).to_frame().T)


def get_lengths(input_dir):
    rows = []
    for f in os.listdir(input_dir):
        if f.endswith(".csv"):
            fpath = os.path.join(input_dir, f)
            if os.stat(fpath).st_size == 0:
                print("ignore: %s" % fpath)
                continue
            print("parsing: %s" % fpath)
            df = pd.read_csv(fpath, header=None)
            print(df)
            med = df.median(numeric_only=True)
            mea = df.mean(numeric_only=True)
            ma = df.max(numeric_only=True)
            mi = df.min(numeric_only=True)
            k = f.split(".")[0]
            # l[k] = int(m)
            # rows.append([k, int(med), int(mea)])
            rows.append([k, int(med), "median"])
            rows.append([k, int(mea), "mean"])
            rows.append([k, int(ma), "max"])
            rows.append([k, int(mi), "min"])
    return rows


def leng_corr(df):
    df = df[df.Technique == "LabLen"]
    # rows = get_lengths(os.path.join("..","output", "ieswc_leng"))
    rows = get_lengths(os.path.join("output", "ieswc_leng"))


    # df_leng = pd.DataFrame(rows, columns=['Ontology', 'length_median', 'length_mean'])
    df_leng = pd.DataFrame(rows, columns=['Ontology', 'Length', 'agg'])

    df = pd.merge(df, df_leng, on="Ontology")
    print(df)

    print(df["agg"])
    print(df[df["agg"] == "mean"])
    # print(df[df.Length==15])

    for attr in ["median", "mean", "max", "min"]:
        # print("for attr: %s")
        df_attr = df[df["agg"]==attr]
        # print(df_attr)
        print("Pearson Correlation for %s: " % (attr))
        print(pearsonr(df_attr['Rating'], df_attr['Length']))
        # print("Pearson Correlation for %s: %f" % (attr, pearsonr(df_attr['Rating'], df_attr['Length'])))

    ax = sns.scatterplot(data=df, x="Length", y="Rating", hue="agg", style="agg")
    #ax = sns.lmplot(data=df, x="Length", y="Rating", hue="agg", markers=["o", "+", "x", "s"], line_kws={'ls':":"})

    ax.figure.savefig(os.path.join("user-study", "leng_corr.svg"))
    ax.figure.savefig(os.path.join("user-study", "leng_corr.eps"))

    # ax.figure.savefig("leng_corr.svg")
    # ax.figure.savefig("leng_corr.eps")
    if SHOW_FIG:
        plt.show()
    plt.clf()


def meta_leng(input_dir):
    rows = []
    for f in os.listdir(input_dir):
        fpath = os.path.join(input_dir, f)
        if os.path.isfile(fpath) and f[-3:] in ['ttl', 'xml', 'owl', 'rdf']:
            print("parsing: %s" % fpath)
            for m in ["title", "desc", "abstract"]:
                title = desc = abstract = False
                if m == "title":
                    title = True
                elif m == "desc":
                    desc = True
                elif m == "abstract":
                    abstract = True

                meta, g = get_meta_text(input_path=fpath, title=title, desc=desc, abstract=abstract, lang=None,
                                        max_options=0)
                leng = 0
                for meta_text in meta:
                    leng = max(leng, len(meta_text.split(' ')))
                print("meta: ")
                print(meta)
                k = f.split(".")[0]
                rows.append([k, leng, m])
        else:
            print("Excluded: %s (%s)" % (f, f[-3:]))
    return rows

def meta_corr(df):
    print("\n\nMeta Corr:")

    df = df[df.Technique == "OntMet"]
    rows = meta_leng(os.path.join("data", "ieswc_enriched"))
    rows += meta_leng(os.path.join("data", "ieswc_enriched", "devops"))
    df_meta = pd.DataFrame(rows, columns=['Ontology', 'Length', 'Level'])

    df = pd.merge(df, df_meta, on="Ontology")
    print(df)

    for attr in ["title", "desc", "abstract"]:
        print("for attr: %s" % attr)
        df_attr = df[df["Level"]==attr]
        print(df_attr)
        print("Pearson Correlation for %s: " % (attr))
        print(pearsonr(df_attr['Rating'], df_attr['Length']))
        # print("Pearson Correlation for %s: %f" % (attr, pearsonr(df_attr['Rating'], df_attr['Length'])))

    ax = sns.scatterplot(data=df, x="Length", y="Rating", hue="Level", style="Level")
    #ax = sns.lmplot(data=df, x="Length", y="Rating", hue="agg", markers=["o", "+", "x", "s"], line_kws={'ls':":"})

    ax.figure.savefig(os.path.join("user-study", "meta_corr.svg"))
    ax.figure.savefig(os.path.join("user-study", "meta_corr.eps"))
    # ax.figure.savefig("meta_corr.eps")
    if SHOW_FIG:
        plt.show()
    plt.clf()


def property_domain_range(ont_path):
    g = rdflib.Graph()
    g.parse(ont_path)
    q = """ select ?prop where { 
      ?prop rdf:type owl:ObjectProperty.
      ?prop rdfs:domain ?domain.
      ?prop rdfs:range ?range
    }"""
    results = g.query(q)
    props = [str(r["prop"]) for r in results]
    return props


def domain_range_leng(input_dir, tech):
    rows = []
    for f in os.listdir(input_dir):
        fpath = os.path.join(input_dir, f)
        if os.path.isfile(fpath) and f[-3:] in ['ttl', 'xml', 'owl', 'rdf']:
            print("parsing: %s" % fpath)

            props = property_domain_range(fpath)
            pcounter = Counter(props)
            print(pcounter)
            nums = [pcounter[k] for k in pcounter]
            k = f.split(".")[0]
            if nums:
                rows.append([k, tech, np.mean(nums), "mean"])
                rows.append([k, tech, np.median(nums), "median"])
                rows.append([k, tech, np.max(nums), "max"])
                rows.append([k, tech, np.min(nums), "min"])
                rows.append([k, tech, sum(nums), "total"])
            else:
                rows.append([k, tech, 0, "mean"])
                rows.append([k, tech, 0, "median"])
                rows.append([k, tech, 0, "max"])
                rows.append([k, tech, 0, "min"])
                rows.append([k, tech, 0, "total"])


        else:
            print("Excluded: %s (%s)" % (f, f[-3:]))
    return rows

def domain_range_corr(df):
    print("\n\nDomain and Range Corr:")
    methods = ["OntMet", "ClaFreq", "LabLen"]
    rows = []
    for tech in methods:
        df_tech = df[df.Technique == tech]
        rows += domain_range_leng(os.path.join("data", "ieswc_enriched"), tech)
        rows += domain_range_leng(os.path.join("data", "ieswc_enriched", "devops"), tech)

    df_tech = pd.DataFrame(rows, columns=['Ontology', 'Technique', 'Count', "Agg"])

    print("\n\n===============\ndf: ")
    print(df)
    print("\n===============\ndf_tech: ")
    print(df_tech)


    df = pd.merge(df, df_tech, on=["Ontology", "Technique"])
    print(df)

    for attr in methods:
        print("for attr: %s" % attr)
        df_attr = df[df["Technique"]==attr]
        # print(df_attr)
        for agg in ["mean", "median", "min", "max", "total"]:
            df_agg = df_attr[df_attr["Agg"]==agg]
            print("Pearson Correlation for technique %s and agg %s: %f " % (attr, agg, pearsonr(df_agg['Rating'], df_agg['Count']).statistic))
            # print(df_agg)
            print(pearsonr(df_agg['Rating'], df_agg['Count']))
        # print("Pearson Correlation for %s: %f" % (attr, pearsonr(df_attr['Rating'], df_attr['Length'])))

    ax = sns.scatterplot(data=df, x="Count", y="Rating", hue="Agg", style="Technique")
    #ax = sns.lmplot(data=df, x="Length", y="Rating", hue="agg", markers=["o", "+", "x", "s"], line_kws={'ls':":"})

    ax.figure.savefig(os.path.join("user-study", "domain-range_corr.svg"))
    ax.figure.savefig(os.path.join("user-study", "domain-range_corr.eps"))
    # ax.figure.savefig("meta_corr.eps")
    if SHOW_FIG:
        plt.show()
    plt.clf()


# def test():
#     """
#     This is used just used for testing how the figures are generated. This is not used for other purposes.
#     """
#     df = pd.DataFrame([["T1",4], ["T2",8], ["T3", 7]], columns=["Technique", "Rating"])
#     fig, ax = plt.subplots(figsize=(5, 5))
#     ax = sns.barplot(
#         data=df,
#         y="Technique", x="Rating",
#         palette="mako",
#         errorbar=None,
#         ax=ax,
#         # pallette="Spectral"
#     )
#     hatches = ["-", "\\", "+"]
#     # Loop over the bars
#     for bars, hatch_ in zip(ax.containers, hatches):
#         # Set a different hatch for each group of bars
#         for bar, hatch in zip(bars, hatches):
#             bar.set_hatch(hatch)
#             bar.set_edgecolor([1, 1, 1])
#     plt.ylabel("Avg. Rating")
#     fig.tight_layout()
#     plt.legend(loc='lower left', handles=ax.containers[0], labels=["OntMet", "ClaFreq", "LabLen"])
#
#     ax.figure.savefig(os.path.join("user-study", "mean.svg"))
#     ax.figure.savefig(os.path.join("user-study", "mean.eps"))
#     # ax.figure.savefig("mean.svg")
#     # ax.figure.savefig("mean.eps")
#     if SHOW_FIG:
#         plt.show()
#     plt.clf()
#     return df_avg_per_ont


if __name__ == "__main__":
    df = pd.read_csv(os.path.join("user-study", "results.csv"))
    df = methods_comparison_mean(df)
    # leng_corr(df)
    # meta_corr(df)
    domain_range_corr(df)
