import matplotlib.pyplot as plt
from matplotlib_venn import venn3

plot_path = 'plots/'

def plot_bar(s, filename, bottom_buffer=0.0, tight=False):
    ax = s.value_counts().sort_index().plot.bar(rot=45)
    ax.bar_label(ax.containers[0])      # Add number on top of bars
    ax.spines.right.set_visible(False)  # Hide right spine
    ax.spines.top.set_visible(False)    # Hide top spine
    if tight: plt.tight_layout()
    if bottom_buffer: plt.subplots_adjust(bottom=bottom_buffer)     # Give bottom space for labels
    plt.savefig(plot_path + filename)
    plt.clf()

def response_rate(s):
    # Calculate the ratio of yes
    number_of_customers = len(s[s == 'Yes'].index)
    total_answers = len(s.index)

    customer_percentage = 100 * (number_of_customers / total_answers)
    print(f'Number of customers: {number_of_customers}/{total_answers} ({customer_percentage:.1f} %)')

    s.value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ylabel='')
    plt.savefig(plot_path + 's01_response_rate.pdf')
    plt.clf()

def purchase_location(s):
    # Plot Venn diagrams
    vc_dict = s.value_counts().to_dict()
    venn3([
        vc_dict['E-commerce'],
        vc_dict['PopUp Store'],
        vc_dict['E-commerce, PopUp Store'],
        vc_dict['ClioMakeUp Experience Store'],
        vc_dict['E-commerce, ClioMakeUp Experience Store'],
        vc_dict['ClioMakeUp Experience Store, PopUp Store'],
        vc_dict['E-commerce, ClioMakeUp Experience Store, PopUp Store']
        ],
        set_labels = ('E-commerce', 'PopUp Store', 'Experience Store'))

    plt.savefig(plot_path + 's03_purchase_location.pdf')
    plt.clf()

def receipt(df):
    s = df['AvgReceipt']
    s.plot.hist(bins=6)
    plt.savefig(plot_path + 's05_receipt.pdf')
    plt.clf()
