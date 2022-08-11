import pandas as pd
import scipy.stats as stats

def chi2test(crosstab, alpha=0.05):
    _, p_value, _, expected = stats.chi2_contingency(crosstab)

    # Reject null hypotesis if p-value is smaller than significance level
    h0 = True
    if p_value <= alpha:
        h0 = False

    return (h0, p_value, expected)
