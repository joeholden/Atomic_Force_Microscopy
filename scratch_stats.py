from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd


def one_way_anova(data):
    data = data.iloc[:-5]
    anova_f, anova_p = stats.f_oneway(data['BASELINE'], data['CMP'], data['MMP'])
    tukey_results = pairwise_tukeyhsd(data.values.flatten(), data.columns.repeat(len(data)))
    return anova_p, tukey_results


