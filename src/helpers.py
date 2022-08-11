import pandas as pd
import scipy.stats as stats

def chi2test(crosstab, alpha=0.05):
    rows = crosstab.index
    columns = crosstab.columns

    # Add total row/column
    crosstab.loc['Total', :] = crosstab.sum(axis='index')
    crosstab.loc[:, 'Total'] = crosstab.sum(axis='columns')

    # significance level
    alpha = 0.05

    # Calcualtion of Chisquare
    chi_square = 0
    ddof = (len(rows) - 1) * (len(columns) - 1)

    for i in rows:
        for j in columns:
            O = crosstab.at[i, j]
            E = crosstab.at[i, 'Total'] * crosstab.at['Total', j] / crosstab.at['Total', 'Total']
            chi_square += ((O - E) ** 2) / E

    p_value = 1 - stats.chi2.cdf(chi_square, ddof)

    h0 = True
    sign = '>'
    conclusion = "Failed to reject the null hypothesis => No significant association between these variables"
    if p_value <= alpha:
        h0 = False
        sign = '<'
        conclusion = "Null hypothesis is rejected => Significant association between these two variables"
            
    print("Chi2 score = ", chi_square)
    print(f"p-value = {p_value} {sign} {alpha}")
    print(conclusion)

    return h0
