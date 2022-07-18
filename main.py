import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles

def response_rate(answers):
    # Calculate the ratio of yes
    number_of_customers = len(answers[answers['Customer'] == 'Si'].index)
    total_answers = len(answers.index)

    customer_percentage = 100 * (number_of_customers / total_answers)
    print(f'Number of customers: {number_of_customers}/{total_answers} ({customer_percentage:.1f} %)')

    answers['Customer'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ylabel='')
    plt.show()

def frequency(answers):
    categories = [
        "da 1 a 2 volte l'anno",
        "da 3 a 4 volte l'anno",
        "da 5 a 6 volte l'anno",
        "da 7 a 8 volte l'anno",
        "più di 9 volte l'anno",
    ]

    answers['Frequency'] = answers['Frequency'].astype('category')
    counts = answers['Frequency'].value_counts().reindex(categories).fillna(0)
    ax = counts.plot.bar(rot=45)
    ax.bar_label(ax.containers[0])
    plt.tight_layout()
    plt.show()

def purchase_location(answers):
    # Change spurious 'On-line' to 'E-commerce'
    index = answers[answers['PurchaseLocation'] == 'On-line'].index[0]
    answers.at[index, 'PurchaseLocation'] = 'E-commerce'

    # Plot Venn diagrams
    value_counts_df = answers['PurchaseLocation'].value_counts().to_frame()
    venn3([
        value_counts_df.loc['E-commerce', 'PurchaseLocation'],
        value_counts_df.loc['PopUp Store', 'PurchaseLocation'],
        value_counts_df.loc['E-commerce, PopUp Store', 'PurchaseLocation'],
        value_counts_df.loc['ClioMakeUp Experience Store', 'PurchaseLocation'],
        value_counts_df.loc['E-commerce, ClioMakeUp Experience Store', 'PurchaseLocation'],
        value_counts_df.loc['ClioMakeUp Experience Store, PopUp Store', 'PurchaseLocation'],
        value_counts_df.loc['E-commerce, ClioMakeUp Experience Store, PopUp Store', 'PurchaseLocation']
        ],
        set_labels = ('E-commerce', 'PopUp Store', 'ClioMakeUp Experience Store'))

    plt.show()

total_answers = pd.read_excel('risposte.xlsx')

# Remove timestamps
total_answers = total_answers.drop(total_answers.columns[0], axis=1)

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
total_answers = total_answers.set_axis(headers, axis=1)

yes_answers = total_answers[total_answers['Customer'] == 'Si']

# response_rate(total_answers)
purchase_location(yes_answers)