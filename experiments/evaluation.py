import argparse
import os
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


from ogister.gister import shorten_url
try:
    from .generate_diagrams import meta_srcs, top_ns
except:
    from experiments.generate_diagrams import meta_srcs, top_ns


def eval_file(inpf, classes):
    """
        inpf: json
                {
            "classes": classes,
            "relations": relations,
            "meta": meta,
            "topn": topn
        }
        classes: list of gs shortened classes
    """
    corr = incorr = notf = 0
    with open(inpf) as f:
        jstr = json.load(f)
        j = json.loads(jstr)
    gs = classes
    pred = j["classes"]
    top_n = j["topn"]
    if top_n > 0:
        gs = gs[:top_n]
        pred = pred[:top_n]

    for g in gs:
        if g in pred:
            corr += 1
        else:
            notf += 1
            print("g not in pred")
            print("%s\t--\t%s" % (g, str(pred)))

    for p in pred:
        if p not in gs:
            incorr += 1

    res = {
        'corr': corr,
        'incorr': incorr,
        'notf': notf,
        'meta': j['meta'],
        'topn': top_n,
        'ontology': inpf.split(os.sep)[-1]
    }
    print(res)
    return res


def parse_gs(gs_file):
    d = dict()
    df = pd.read_csv(gs_file)
    """ontology,class,ranking"""
    ontologies = list(set(df['ontology']))
    for o in ontologies:
        dfo = df[df['ontology'] == o]
        dfo.sort_values(by=['ranking'])
        d[o] = [shorten_url(c) for c in dfo['class']]
    # print("parsed GS: ")
    # print(d)
    return d


def get_df_results(evs):
    """
    :param evs: list of dict {
        'corr': corr,
        'incorr': incorr,
        'notf': notf,
        'meta': j['meta'],
        'topn': top_n,
        'ontology':
    }
    return df
    """
    rows = []
    for ev in evs:
        r = [ev['ontology'], ev['corr'], ev['incorr'], ev['notf'], ev['meta'], ev['topn']]
        rows.append(r)
    return pd.DataFrame(rows, columns=['ontology', 'corr', 'incorr', 'notf', 'meta', 'topn'])


def evaluate(input_files, output_path, gs_path):
    evs = []
    gs = parse_gs(gs_path)
    for inp in input_files:
        fname = inp.split(os.sep)[-1]
        ontology = fname.split('-')[0]
        if ontology not in gs:
            print("ignoring: %s (%s)" % (ontology, fname))
            continue
        ev = eval_file(inp, gs[ontology])
        evs.append(ev)

    df = get_df_results(evs)
    generate_diagram(df, output_path)


def generate_diagram(df, output_path):
    """
    results df

    :return: None
    """
    # # JUST for testing
    # meta_srcs = ["description"]
    # # top_ns = [5]

    scores = []
    print("df: ")
    print(df)
    for m in meta_srcs:
        dfm = df[df.meta == m]
        print("dfm: %s" % m)
        print(dfm)
        for n in top_ns:
            dfn = dfm[dfm.topn == n]
            print("dfn: %s\t%d" % (m, n))
            print(dfn)
            corr = sum(dfn['corr'])
            incorr = sum(dfn['incorr'])
            notf = sum(dfn['notf'])
            prec = rec = f1 = 0
            if (corr + incorr) > 0:
                prec = corr / (corr + incorr)
            if (corr + notf) > 0:
                rec = corr / (corr + notf)
            if (prec + rec) > 0:
                f1 = 2 * prec * rec / (prec + rec)
            row = [m, n, prec, 'Precision']
            scores.append(row)
            row = [m, n, rec, 'Recall']
            scores.append(row)
            row = [m, n, f1, 'F1']
            scores.append(row)
            # row = [m, n, prec, rec, f1]
            # scores.append(row)
        # for row in dfm.iterrows():
        #     sum(list)

    # scores_titles = ["Precision", "Recall", "F1"]
    df_scores = pd.DataFrame(scores, columns=['Meta', 'Top-n', 'Score', 'Metric'])

    print("\n\nScores:\n=========\n ")
    print(df_scores)

    # for k in scores:
    #     for idx, sc in enumerate(scores_titles):
    #         row = [str(k), scores[k][idx], scores_titles[idx]]
    #         rows.append(row)
    #     # row = [k, scores[k][0], scores[k][1], scores[k][2]]
    #     # rows.append(row)
    # df = pd.DataFrame(rows, columns=['Cutoff', 'Score', 'Metric'])
    # df['Cutoff'] = df['Cutoff'].astype('category')
    # linestyles = ["--", ":", "dashdot"]

    # # DRAW for each meta
    # for m in meta_srcs:
    #     dfm = df_scores[df_scores["Meta"] == m]
    #     ax = sns.lineplot(x="Top-n", y="Score", hue="Metric", data=dfm, linewidth=2, style="Metric",
    #                      # palette="colorblind",
    #                      # palette="Spectral",
    #                      # palette="pastel",
    #                      # palette="ch:start=.2,rot=-.3",
    #                      # palette="YlOrBr",
    #                      # palette="Paired",
    #                      # palette="Set2",
    #                      # orient="h"
    #                       )
    #
    #     ax.legend(loc=2, fontsize='x-small')
    #     # ax.figure.savefig('%s.svg' % fpath, bbox_inches="tight")
    #     plt.show()

    ax = sns.lineplot(x="Top-n", y="Score", hue="Meta", data=df_scores, linewidth=2, style="Metric",
                      # palette="colorblind",
                      # palette="Spectral",
                      # palette="pastel",
                      # palette="ch:start=.2,rot=-.3",
                      # palette="YlOrBr",
                      # palette="Paired",
                      # palette="Set2",
                      # orient="h"
                      )

    ax.legend(loc=2, fontsize='x-small')
    fpath = os.path.join(output_path, 'results')
    ax.figure.savefig('%s.svg' % fpath, bbox_inches="tight")
    # plt.show()


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Evaluate the generate graphs')
    parser.add_argument('-i', '--input', nargs="+", required=True, help="json files")
    parser.add_argument('-o', '--output', default="output", help="Output path")
    parser.add_argument('-g', '--gs', required=True, help="Path to the gs csv file")
    args = parser.parse_args()
    return args.output, args.input, args.gs


def main():
    """
    Parse Arguments
    """
    output_path, input_files, gs = parse_arguments()
    evaluate(input_files, output_path, gs)


if __name__ == "__main__":
    main()
