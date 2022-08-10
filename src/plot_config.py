import seaborn
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import random
import numpy as np

# Where to save plots
plot_path = '../plots/'

# Global plot settings 
plt.rcParams.update({
    'figure.autolayout':    True,
    'font.family':          'Arial', 
})

# Colors
# colors = ('#e5e1ee', '#dffdff', '#90bede', '#68edc6', '#90f3ff') # Noemi's palette
colors = ('#ffcdb2', '#ffb4a2', '#e5989b', '#b5838d', '#6d6875')
colormap = ('#E8E8E8', '#D4D4D4', '#BFBFBF', '#ABA9AD', '#96939B', '#766B79', '#564256')
extra_line_color = 'royalblue'
cmap = ListedColormap(colormap) # Custom colormap

class RandomColor:
    def __init__(self, colors):
        self.colors = colors

    def __call__(self):
        return random.choice(self.colors)

random_color = RandomColor(colors)

# Default arguments per plot type
pie_kwargs = {
    'autopct':      lambda pct: '{:1.0f}%'.format(pct) if pct > 2.5 else '',
    'startangle':   90,
    'ylabel':       '',
    'colors':       colors,
}

bar_kwargs = {
    'rot':      0,
}


hline_kwargs = {
    'color':        extra_line_color,
    'linewidth':    0.6,
    'linestyle':    '--',
}

# Save figure function
def save_fig(filename, path=plot_path, ext='.pdf'):
    plt.savefig(path + filename + ext)
    plt.clf()
    plt.close()

# Hide spines
def hide_spines(ax):
    ax.spines.right.set_visible(False)  # Hide right spine
    ax.spines.top.set_visible(False)    # Hide top spine

# Plot heatmap
def make_heatmap(df, filename, **kwargs):
    _, ax = plt.subplots()
    im, _ = heatmap(data=df, row_labels=df.index, col_labels=df.columns, ax=ax, cmap='Blues')
    annotate_heatmap(im=im, data=df, valfmt='{x:.1f}%')
    # plt.xlabel(xlabel)
    # plt.ylabel(ylabel)

    # ax.imshow(df, cmap=cmap, **kwargs)

    # x = df.columns
    # y = df.index

    # # Show all ticks and label them with the respective list entries
    # ax.set_xticks(np.arange(len(x)), labels=x)
    # ax.set_yticks(np.arange(len(y)), labels=y)

    # # Hide spines
    # ax.spines[:].set_visible(False)

    # Loop over data dimensions and create text annotations.
    # for i in range(len(x)):
    #     for j in range(len(y)):
    #         item = df.iat[j, i]
    #         # r, g, b, _ = colormap(item)
    #         # if (r*0.299 + g*0.587 + b*0.114) > 186:
    #         #     text_color = 'w'
    #         # else:
    #         #     text_color = 'k'
    #         ax.text(i, j, f'{100*df.iat[j, i]:.1f}%', ha="center", va="center", color='k')

    # Save plot
    save_fig(filename)

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, interpolation='nearest', **kwargs)

    # Create colorbar
    cbar = None
    # cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    # cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(100*data[i, j], None), **kw)
            texts.append(text)

    return texts









# x, y = np.ogrid[-5:5:.1, -5:5:.1]
# dd = np.exp(-(x*2 + y*2))
# dd[dd < .1] = np.nan

# fig, ax = plt.subplots()
# ax.imshow(dd, interpolation='nearest', cmap='gray_r')
# plt.savefig('plots/test.pdf')