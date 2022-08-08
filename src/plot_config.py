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
colormap = ('#E8E8E8', '#D4D4D4', '#BFBFBF', '#ABA9AD', '#96939B', '#766B79', '#564256', '#805253', '#A96250', '#FC814A')
extra_line_color = 'royalblue'
cmap = ListedColormap(colors) # Custom colormap

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

def heatmap(df, filename, xlabel='', ylabel='', **kwargs):
    _, ax = plt.subplots()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    ax.imshow(df, cmap=cmap, **kwargs)

    x = df.columns
    y = df.index
    print(len(x),len(y))

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(x)), labels=x)
    ax.set_yticks(np.arange(len(y)), labels=y)

    # Hide spines
    ax.spines[:].set_visible(False)

    # Loop over data dimensions and create text annotations.
    for i in range(len(x)):
        for j in range(len(y)):
            ax.text(i, j, f'{100*df.iat[j, i]:.1f}%', ha="center", va="center", color="w")

    # Save plot
    save_fig(filename)
