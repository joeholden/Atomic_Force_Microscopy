from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import pandas as pd
import numpy as np


def one_way_anova(data):
    data = data.iloc[:-5]
    anova_f, anova_p = stats.f_oneway(data['BASELINE'], data['CMP'], data['MMP'])
    tukey_results = pairwise_tukeyhsd(data.values.flatten(), data.columns.repeat(len(data)))

    tukey_results = pd.DataFrame(data=tukey_results._results_table.data[1:],
                                 columns=tukey_results._results_table.data[0])
    return anova_f, anova_p, tukey_results