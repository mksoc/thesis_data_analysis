import data_preparation
import single_var_analysis

# single_var_analysis.response_rate(data_preparation.df_all['Customer'])
single_var_analysis.plot_bar(data_preparation.df_yes['Frequency'], 's02_frequency.pdf', bottom_buffer=0.3)
# single_var_analysis.purchase_location(data_preparation.df_yes['PurchaseLocation'])
single_var_analysis.plot_bar(data_preparation.df_yes['BrandKnownFor'], 's04_brand_known_for.pdf', tight=True)
# single_var_analysis.receipt(data_preparation.df_yes)
