from locale import normalize
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

plot_path = 'plots/'
# colors = ('#e5e1ee', '#dffdff', '#90bede', '#68edc6', '#90f3ff') # Noemi's palette
colors = ('#5386E4', '#757396', '#949396', '#ABA8B2', '#C3C3C3')

# General functions
def error_msg(arg_name, *args):
    return f"Invalid value for argument '{arg_name}'. Valid values are: {*args,}."

def plot_bar(s, filename, orientation='v', bar_label=True, sort='index', **kwargs):
    # Check arguments
    if sort == 'index':
        s_sorted = s.value_counts().sort_index()
    elif sort == 'values':
        s_sorted = s.value_counts().sort_values()
    else:
        raise ValueError(error_msg('sort', 'index', 'values'))

    plt.rcParams.update({'figure.autolayout': True}) # Automatically make all the labels fit
    kwargs['color'] = colors[0]
    if orientation == 'v':
        ax = s_sorted.plot.bar(**kwargs)
    elif orientation == 'h':
        ax = s_sorted.plot.barh(**kwargs)
    else:
        raise ValueError(error_msg('orientation', 'h', 'v'))

    # Plot the plot 
    if bar_label: ax.bar_label(ax.containers[0])      # Add number on top of bars
    ax.spines.right.set_visible(False)  # Hide right spine
    ax.spines.top.set_visible(False)    # Hide top spine
    plt.savefig(plot_path + filename)
    plt.clf()
    plt.close()

def plot_hist(s, filename, bar_label=True, bins=4, **kwargs):
    kwargs['color'] = colors[0]
    ax = s.plot.hist(bins=bins, **kwargs)
    ax.set_ylabel('')
    if bar_label: ax.bar_label(ax.containers[0])      # Add number on top of bars
    ax.spines.right.set_visible(False)  # Hide right spine
    ax.spines.top.set_visible(False)    # Hide top spine
    plt.savefig(plot_path + filename)
    plt.clf()
    plt.close()

def plot_pie(s, filename, legend=False, **kwargs):
    kwargs['colors'] = colors
    kwargs['wedgeprops'] = {"edgecolor":"white",'linewidth': 0.5}
    if legend:
        kwargs['labels'] = None
    
    s.value_counts().plot.pie(**kwargs)
    if legend: plt.legend(labels=s.value_counts().index, bbox_to_anchor=(0.8,0.8), loc='lower left')
    plt.savefig(plot_path + filename)
    plt.clf()
    plt.close()

# Specific functions
def purchase_location(s, filename):
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

    plt.savefig(plot_path + filename)
    plt.clf()
    plt.close()
