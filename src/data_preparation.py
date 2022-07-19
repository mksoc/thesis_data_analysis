import pandas as pd

# Read response file
response_file = '../data/risposte.xlsx'
responses_df = pd.read_excel(response_file)

# Remove timestamps
responses_df = responses_df.drop(responses_df.columns[0], axis=1)

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
           'SelfOrOthers']
responses_df = responses_df.set_axis(headers, axis=1)

# Change spurious 'On-line' to 'E-commerce'
index = responses_df[responses_df['PurchaseLocation'] == 'On-line'].index[0]
responses_df.at[index, 'PurchaseLocation'] = 'E-commerce'

# Change spurious 'Da molto più di 5 anni' to '5 anni (dal lancio dei primi rossetti)'
index = responses_df[responses_df['BrandKnownFor'] == 'Da molto più di 5 anni'].index[0]
responses_df.at[index, 'BrandKnownFor'] = '5 anni (dal lancio dei primi rossetti)'

# Extract only 'yes' responses
responses_yes_df = responses_df[responses_df['Customer'] == 'Si']

# Calculate expenditure from last purchase
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

s = responses_yes_df['LastPurchase']
s = s.apply(lambda item: sum([prices_dict[i.strip()] for i in item.split(',') if i.strip() in prices_dict]))
responses_yes_df['AvgReceipt'] = s
