import matplotlib.pyplot as plt
import numpy as np
import statistics as stats
from collections import defaultdict
import pandas as pd


def make_plots(dataframe, title, show=True):
    bar_plot_dictionary = defaultdict()
    groups = dataframe.columns
    if {'cmp', 'mmp', 'baseline'} == set([i.lower() for i in groups]):
        groups = ['BASELINE', 'MMP', 'CMP']
    for group in groups:
        bar_plot_dictionary[group] = stats.mean(dataframe[group])
    means = bar_plot_dictionary.values()

    max_value = dataframe.to_numpy().max()
    bar_colors = ['#440154', '#21918c', '#5ec962']

    x = np.arange(len(dataframe.columns))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots(layout='constrained', figsize=(7, 9))
    ax.bar(groups, means, color=bar_colors)

    ax.set_title(title, fontsize=36)
    ax.set_ylabel("Young's Modulus kPa", fontsize=28)
    ax.set_xticklabels(groups, fontsize=24)
    plt.yticks(fontsize=24)

    try:
        ax.set_ylim(0, max_value * 1.05)
    except ValueError:
        pass

    for index, value in enumerate(groups):
        x = np.random.normal(index, 0.1, size=len(dataframe[value]))
        plt.scatter(x, dataframe[value], alpha=0.75, color='black')

    if show:
        plt.show()


# make_plots(dataframe=pd.read_excel("test_sns.xlsx"), title='test')
