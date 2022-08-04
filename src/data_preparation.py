from audioop import mul
import pandas as pd
from pyparsing import col

def fill_rename_categories(s, categories):
    # Set categorical dtype
    s = s.astype('category')

    # Set categories, define unused and define order
    s = s.cat.set_categories(list(categories.keys()), ordered=True)

    # Translate to English
    s = s.cat.rename_categories(categories)

    return s

def check_spurious_values(s, value_list, multiple=False):
    # If an entry can contain multiple values, split them
    if multiple:
        s = s.str.split(',').map(lambda item: [i.strip() for i in item], na_action='ignore')
        s = s.explode(column)
    
    # Compare values in the column with valid values
    vc = s.value_counts()
    column_values = vc.index
    max_padding = max([len(i) for i in column_values])
    invalid_count = 0
    print(f'Checking values for series "{s.name}":')
    print(f'  {"Value":{max_padding}}    {"Valid":10}    Occurrences')
    print('  ' + '-' * (max_padding + 4 + 10 + 4 + 11))
    for value in column_values:
        comment = 'OK'
        if value not in value_list:
            invalid_count += 1
            comment = 'INVALID'
        print(f'  {value:{max_padding}}    {comment:10}    {vc.loc[value]}')
    
    if invalid_count == 0:
        print(f'No invalid values for series "{s.name}"')
    else:
        print(f'Total: {invalid_count} invalid values were found in series "{s.name}"')
    print()

# Read response file
response_file = '../data/risposte.xlsx'
df = pd.read_excel(response_file)

# Remove timestamps
df = df.drop(df.columns[0], axis=1)

# Rename headers
headers = ['Customer',
           'Frequency',
           'PurchaseLocation',
           'BrandKnownFor',
           'LastPurchase',
           'AllPurchases',
           'Satisfaction',
           'Gender',
           'Age',
           'Education',
           'Profession',
           'PlaceOfResidence',
           'Province',
           'SelfOrOthers'
]
df = df.set_axis(headers, axis='columns')

# Column 'Customer'
column = 'Customer'
# Set categories
categories = {
    'Si': 'Yes',
    'No': 'No',
}
df[column] = fill_rename_categories(df[column], categories)

# Column 'Frequency'
column = 'Frequency'
# Define categories
categories = {
    "da 1 a 2 volte l'anno": "1-2 times a year",
    "da 3 a 4 volte l'anno": "3-4 times a year",
    "da 5 a 6 volte l'anno": "5-6 times a year",
    "da 7 a 8 volte l'anno": "7-8 times a year",
    "più di 9 volte l'anno": "> 9 times a year",
}
# Set categories
df[column] = fill_rename_categories(df[column], categories)

# Column 'PurchaseLocation'
column = 'PurchaseLocation'
# Define categories
categories = ['E-commerce', 'PopUp Store', 'ClioMakeUp Experience Store']
# Clean data (change spurious 'On-line' to 'E-commerce')
df[column] = df[column].str.replace('On-line', 'E-commerce')

# Column 'BrandKnownFor'
column = 'BrandKnownFor'
# Define categories
categories = {
    'Meno di un anno':                          'less than 1 year',
    '1 anno':                                   '1 year',
    '2 anni':                                   '2 years',
    '3 anni':                                   '3 years',
    '4 anni':                                   '4 years',
    '5 anni (dal lancio dei primi rossetti)':   '5 years (first lipstick launch)',
}
# Clean data
df[column] = df[column].str.replace('Da molto più di 5 anni', '5 anni (dal lancio dei primi rossetti)')
# Set categories
df[column] = fill_rename_categories(df[column], categories)

# Column 'LastPurchase'
column = 'LastPurchase'
# Define valid values
prices_dict = {
    'WonderMousse (Mousse viso detergente e struccante)':   15.50,
    'SuperStrucco (Balsamo detergente e struccante)':       24.50,
    'Kit doppia detersione (WonderMousse + SuperStrucco)':  35.00,
    'Paciocchi (Maschera occhi)':                           6.50,
    'Kit Paciocchi 5+1':                                    32.50,
    'Fondotinta OhMyLove':                                  28.50,
    'Correttore OhMyLove':                                  17.50,
    'Blush CuteLove':                                       15.50,
    'Illuminante CosmicLove':                               16.50,
    'Matite Sopracciglia AllDayLov Brow':                   12.50,
    'Ombretti liquidi SweetieLove':                         14.50,
    'Ombretti cremosi SweetieLove':                         14.50,
    'Mascara DarkLove':                                     14.50,
    'Eyeliner DeepLove':                                    14.50,
    'Matita occhi AllDayLove':                              10.50,
    'Palette BeautyLove':                                   57.50,
    'Palette FirstLove':                                    32.50,
    'Palette MyFirstLove ( 4 ombretti)':                    5.50,
    'Ombretti ClioMakeUp Eyeshadow':                        6.50,
    'Ultrabalm Passion (Limited Edition)':                  15.50,
    'Ultrabalm CoccoLove':                                  15.50,
    'Lip balm colorati CoccoLove':                          12.50,
    'Rossetti liquidi LiquidLove':                          13.50,
    'Rossetti cremosi CreamyLove':                          12.50,
    'Pennelli':                                             22.00,
}
# Create new column with receipt amount
new_column = 'ReceiptAmount'
df[new_column] = df[column].map(lambda item: sum([prices_dict[i.strip()] for i in item.split(',') if i.strip() in prices_dict]), na_action='ignore')

# Column 'AllPurchases'
column = 'AllPurchases'
# Clean data
df[column] = df[column].str.replace('passion', 'Passion')
# Turn single strings into list of strings
df[column] = df[column].str.split(',').map(lambda item: [i.strip() for i in item], na_action='ignore')
