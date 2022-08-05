import data_preparation
import single_var_analysis

# Customer yes/no
single_var_analysis.plot_pie(data_preparation.df_all['Customer'], 's01_response_rate.pdf', autopct='%1.1f%%', startangle=90, ylabel='')

# Buying frequency
single_var_analysis.plot_bar(data_preparation.df_yes['Frequency'], 's02_frequency.pdf', rot=45)

# Purchase channel
single_var_analysis.purchase_location(data_preparation.df_yes['PurchaseLocation'], 's03_purchase_location.pdf')

# Brand known for how long
single_var_analysis.plot_bar(data_preparation.df_yes['BrandKnownFor'], 's04_brand_known_for.pdf', rot=45)

# Average receipt amount
single_var_analysis.plot_hist(data_preparation.df_yes['ReceiptAmount'], 's05_receipt.pdf', bins=8)

# Total purchases
single_var_analysis.plot_bar(data_preparation.df_yes['AllPurchases'].explode(), 's06_all_purchases.pdf',
    orientation='h', bar_label=False, sort='values', width=0.8, figsize=(10, 8))

# Satisfaction
single_var_analysis.plot_pie(data_preparation.df_yes['Satisfaction'], 's07_satisfaction.pdf',
    autopct=lambda pct: '{:1.0f}%'.format(pct) if pct > 2.5 else '',    # Don't show values < 2.5%
    startangle=90, ylabel='', legend=True)

