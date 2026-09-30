import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from scipy.optimize import curve_fit

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

def fit_second_task(x, y):
    """Аппроксимация I(ΔX) = A + B·cos(4πΔX/λ + φ)."""
    def model(x, A, B, lam, phi):
        return A + B * np.cos(4 * np.pi * x / lam + phi)

    p0 = [np.mean(y), (max(y) - min(y)) / 2, 34.0, 0.0]
    popt, _ = curve_fit(model, x, y, p0=p0, maxfev=10000)
    A, B, lam, phi = popt
    return A, B, lam, phi, model

x = [i for i in range(30, 70, 3)]
y = [49, 50, 50, 48, 47, 48, 50, 51, 49, 47, 47, 47, 51, 50]

x = np.array(x, dtype=float)
y = np.array(y, dtype=float)

A, B, lam, phi, model = fit_second_task(x, y)

fig, ax = plt.subplots()
latex_plot(ax)

ax.plot(x, y, color='red', label='эксперимент')
ax.scatter(x, y, color='red', alpha=1)

xs = np.linspace(x.min(), x.max(), 500)
ax.plot(xs, model(xs, A, B, lam, phi), color='black', linewidth=1.2, label='аппроксимация')

ax.set_xlabel(r"$\Delta X$, мм")
ax.set_ylabel(r"$|E|^2$, мВ")
# ax.legend()

print(f"A = {A:.3f}, B = {B:.3f}, λ = {lam:.3f} мм, φ = {phi:.3f}")

plt.show()