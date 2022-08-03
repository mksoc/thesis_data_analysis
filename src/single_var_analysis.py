import matplotlib.pyplot as plt
from matplotlib_venn import venn3

plot_path = '../plots/'

def response_rate(df):
    # Calculate the ratio of yes
    number_of_customers = len(df[df['Customer'] == 'Si'].index)
    total_answers = len(df.index)

    customer_percentage = 100 * (number_of_customers / total_answers)
    print(f'Number of customers: {number_of_customers}/{total_answers} ({customer_percentage:.1f} %)')

    df['Customer'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, labels=['No', 'Yes'], ylabel='')
    plt.savefig(plot_path + 's01_response_rate.pdf')
    plt.clf()

def frequency(df):
    categories = [
        "da 1 a 2 volte l'anno",
        "da 3 a 4 volte l'anno",
        "da 5 a 6 volte l'anno",
        "da 7 a 8 volte l'anno",
        "più di 9 volte l'anno",
    ]

    s = df['Frequency'].astype('category')
    counts = s.value_counts().reindex(categories).fillna(0)
    ax = counts.plot.bar(rot=45)
    ax.bar_label(ax.containers[0])
    plt.tight_layout()
    plt.savefig(plot_path + 's02_frequency.pdf')
    plt.clf()

def purchase_location(df):
    # Plot Venn diagrams
    value_counts_dict = df['PurchaseLocation'].value_counts().to_dict()
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

    plt.savefig(plot_path + 's03_purchase_location.pdf')
    plt.clf()

def brand_known_for(df):
    counts = df['BrandKnownFor'].value_counts()[
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
    plt.savefig(plot_path + 's04_brand_known_for.pdf')
    plt.clf()

def receipt(df):
    s = df['AvgReceipt']
    s.plot.hist(bins=6)
    plt.savefig(plot_path + 's05_receipt.pdf')
    plt.clf()
