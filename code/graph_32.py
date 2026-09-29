import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np


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


X = np.array([0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45,
              48, 51, 54, 57, 60, 63, 66, 69, 72, 75], dtype=float)
E_MAX = np.array([54, 51, 51, 53, 54, 54, 52, 50, 52, 54, 54, 53, 50, 51,
                  54, 54, 53, 51, 50, 52, 54, 53, 50, 51, 52, 54], dtype=float)
E_MIN = np.array([45, 46, 45, 43, 43, 44, 45, 47, 44, 43, 43, 45, 47, 46,
                  43, 43, 45, 47, 50, 44, 42, 44, 47, 46, 44, 43], dtype=float)

kappa = np.sqrt(E_MIN / E_MAX)
gamma_tilde = (1.0 - kappa) / (1.0 + kappa)

x = X
y = gamma_tilde

ax.scatter(x, y, color='red')
ax.plot(x, y)
ax.set_xlabel(r"$x$, мм")
ax.set_ylabel(r"$\tilde{\Gamma}$")

plt.show()