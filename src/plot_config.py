import matplotlib.pyplot as plt
import random

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
extra_line_color = 'royalblue'

class RandomColor:
    def __init__(self, colors) -> None:
        self.colors = colors

    def __str__(self) -> str:
        # return str(random.choice(self.colors))
        return 'Ciao'

# Default arguments per plot type
pie_kwargs = {
    'autopct':      lambda pct: '{:1.0f}%'.format(pct) if pct > 2.5 else '',
    'startangle':   90,
    'ylabel':       '',
    'colors':       colors,
}

bar_kwargs = {
    'rot':      0,
    'color':    RandomColor(colors),
}
print(bar_kwargs['color'])
print(bar_kwargs['color'])
print(bar_kwargs['color'])

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