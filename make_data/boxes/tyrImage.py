# Class encapsulating a fake rainfall data image - single box

import os
import math
import random
import pickle
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D


class tyrImage:
    def __init__(self, opdir, docn, **kwargs):
        self.opdir = opdir
        self.docn = docn

        # Parameters defining the image geometry
        self.pageWidth = 48
        self.pageHeight = 36
        self.bgcolour = (1.0, 1.0, 1.0)
        self.fgcolour = (0.0, 0.0, 0.0)
        self.fontSize = 10
        self.fontFamily = "Arial"
        self.fontStyle = "normal"
        self.fontWeight = "normal"

        # Noise parameters
        self.jitterFontSize = 0.0
        self.jitterFontRotate = 0.0
        self.jitterGridPoints = 0.0
        self.jitterLineWidth = 0.0

        self.generateNumbers()

        for key, value in kwargs.items():
            if hasattr(self, key):
                if value is not None:
                    setattr(self, key, value)
            else:
                raise ValueError("No parameter %s" % key)

    def dumpState(self):
        if not os.path.isdir("%s/meta" % self.opdir):
            os.makedirs("%s/meta" % self.opdir)
        with open("%s/meta/%s.pkl" % (self.opdir, self.docn), "wb") as pf:
            pickle.dump(vars(self), pf)

    def makeImage(self):
        fig = Figure(
            figsize=(self.pageWidth / 100, self.pageHeight / 100),
            dpi=100,
            facecolor="white",
            edgecolor="black",
            linewidth=0.0,
            frameon=False,
            subplotpars=None,
            tight_layout=None,
        )
        canvas = FigureCanvas(fig)
        ax_full = fig.add_axes([0, 0, 1, 1])
        ax_full.set_xlim([0, 1])
        ax_full.set_ylim([0, 1])
        ax_full.set_axis_off()

        # Paint the background
        ax_full.add_patch(
            matplotlib.patches.Rectangle(
                (0, 0), 1, 1, fill=True, facecolor=self.bgcolour
            )
        )

        # Draw the figure
        self.drawNumbers(ax_full)
        if not os.path.isdir("%s/images" % self.opdir):
            os.makedirs("%s/images" % self.opdir)
        fig.savefig("%s/images/%s.png" % (self.opdir, self.docn))

    # Must call makeImage before calling this
    #  (bad design but not worth fixing).
    def makeNumbers(self):
        if not os.path.isdir("%s/numbers" % self.opdir):
            os.makedirs("%s/numbers" % self.opdir)
        with open("%s/numbers/%s.pkl" % (self.opdir, self.docn), "wb") as pf:
            pickle.dump(self.rdata, pf)

    # Everything below this is an internal function you should not have to call directly

    # Apply a perturbation to positions
    def jitterPos(self):
        if self.jitterGridPoints == 0:
            return 0
        return random.normalvariate(0, self.jitterGridPoints)

    def jitterLW(self):
        if self.jitterLineWidth == 0:
            return 0
        return random.normalvariate(0, self.jitterLineWidth)

    def jitterFS(self):
        if self.jitterFontSize == 0:
            return 0
        return random.normalvariate(0, self.jitterFontSize)

    def jitterFR(self):
        if self.jitterFontRotate == 0:
            return 0
        return random.normalvariate(0, self.jitterFontRotate)

    # Generate random numbers to fill out the data table
    #  3 integers (0-9) - x, y, and z
    #  where the accumulated rainfall for that month is x.yz inches.
    def generateNumbers(self):
        self.rdata = []
        for pni in range(3):
            self.rdata.append(random.randint(0, 9))

    # Fill out the table with the random numbers
    def drawNumbers(self, ax):
        x = 0.5
        y = 0.5
        inr = self.rdata[0] + self.rdata[1] / 10 + self.rdata[2] / 100
        strv = "%4.2f" % inr
        ax.text(
            x + self.jitterPos(),
            y + self.jitterPos(),
            strv,
            fontdict={
                "family": self.fontFamily,
                "size": self.fontSize + self.jitterFS(),
                "style": self.fontStyle,
                "weight": self.fontWeight,
            },
            horizontalalignment="center",
            verticalalignment="center",
            rotation=self.jitterFR(),
        )
        # Make certain numbers are identical to printed version
        self.rdata[0] = int(strv[0])
        self.rdata[1] = int(strv[2])
        self.rdata[2] = int(strv[3])
