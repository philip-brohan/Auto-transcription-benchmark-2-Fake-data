#!/usr/bin/env python

# Show examples of digits in all available fonts

import matplotlib.font_manager

import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

# Get the names of all the installed font families
names = [f.name for f in matplotlib.font_manager.fontManager.ttflist]
# Prune the duplicates
names = sorted(list(set(names)))

# figure to draw in
fig = Figure(
    figsize=(30, 18),
    dpi=100,
    facecolor="white",
    edgecolor="black",
    linewidth=0.0,
    frameon=False,
    subplotpars=None,
    tight_layout=None,
)
canvas = FigureCanvas(fig)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_axis_off()

# Paint the background
ax.add_patch(matplotlib.patches.Rectangle((0, 0), 1, 1, fill=True, facecolor="white"))

for fi in range(len(names)):
    x = int(fi / 50) * 0.25 + 0.02
    y = 0.99 - (fi % 50) / 52
    ax.text(
        x,
        y,
        names[fi],
        fontdict={"family": "sans", "size": 22},
        horizontalalignment="left",
        verticalalignment="top",
    )
    ax.text(
        x + 0.14,
        y,
        "0.123456789",
        fontdict={
            "family": names[fi],
            "size": 22,
            "style": "oblique",
            "weight": "light",
        },
        horizontalalignment="left",
        verticalalignment="top",
    )

fig.savefig("fonts.png")
