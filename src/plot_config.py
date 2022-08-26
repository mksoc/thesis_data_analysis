import seaborn as sns
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
    'rot':      0
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
diverging_cmap = sns.diverging_palette(20, 230, as_cmap=True)
light_cmap = sns.light_palette("#2ecc71", as_cmap=True)

def heatmap(data, filename, cmap=light_cmap, fmt='.2g'):
    sns.set_theme(style="white")
    ax = sns.heatmap(data, cmap=cmap, annot=True, fmt=fmt, cbar=False, linewidths=.5)
    
    # Hide axis labels
    ax.set_xlabel('')
    ax.set_ylabel('')

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")
    plt.setp(ax.get_yticklabels(), rotation=0)

    save_fig(filename)