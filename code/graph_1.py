import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

plt.rcParams.update({
    "font.family": "CMU Serif",
    "font.size": 12,
    "mathtext.fontset": "cm",
    "axes.linewidth": 0.8,
    "axes.grid": True,
    "grid.linewidth": 0.4,
    "grid.alpha": 0.5,
    "xtick.direction": "in",
    "ytick.direction": "in",
    "xtick.minor.visible": True,
    "ytick.minor.visible": True,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "xtick.minor.width": 0.4,
    "ytick.minor.width": 0.4,
    "figure.figsize": (6, 4),
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

def latex_plot(ax):
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.grid(which="major", linewidth=0.5, alpha=0.65)
    ax.grid(which="minor", linewidth=0.25, alpha=0.4)
    ax.tick_params(which="both", top=True, right=True)
    return ax

fig, ax = plt.subplots()
latex_plot(ax)

x = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]
y = [54, 52, 49, 46, 45, 46, 49, 51, 52, 51, 48, 46, 45, 46, 49, 51, 53, 52]

ax.scatter(x, y)
ax.set_xlabel(r"$x$, мм")
ax.set_ylabel(r"$I_\text{д}$, мА")


plt.show()