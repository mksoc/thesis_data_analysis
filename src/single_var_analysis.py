import matplotlib.pyplot as plt
from matplotlib_venn import venn3

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

    s = answers['Frequency'].astype('category')
    counts = s.value_counts().reindex(categories).fillna(0)
    ax = counts.plot.bar(rot=45)
    ax.bar_label(ax.containers[0])
    plt.tight_layout()
    plt.show()

def purchase_location(answers):
    # Plot Venn diagrams
    value_counts_dict = answers['PurchaseLocation'].value_counts().to_dict()
    venn3([
        value_counts_dict['E-commerce'],
        value_counts_dict['PopUp Store'],
        value_counts_dict['E-commerce, PopUp Store'],
        value_counts_dict['ClioMakeUp Experience Store'],
        value_counts_dict['E-commerce, ClioMakeUp Experience Store'],
        value_counts_dict['ClioMakeUp Experience Store, PopUp Store'],
        value_counts_dict['E-commerce, ClioMakeUp Experience Store, PopUp Store']
        ],
        set_labels = ('E-commerce', 'PopUp Store', 'Experience Store'))

    plt.show()

def brand_known_for(answers):
    counts = answers['BrandKnownFor'].value_counts()[
        ['Meno di un anno',
        '1 anno',
        '2 anni',
        '3 anni',
        '4 anni',
        '5 anni (dal lancio dei primi rossetti)']
    ]
    ax = counts.plot.bar(rot=45)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.bar_label(ax.containers[0])
    ax.set_xticks(ax.get_xticks(), ['Meno di un anno',
        '1 anno',
        '2 anni',
        '3 anni',
        '4 anni',
        '5 anni'])
    plt.tight_layout()
    plt.show()

def receipt(answers):
    s = answers['AvgReceipt']
    s.plot.hist(bins=6)
    plt.show()