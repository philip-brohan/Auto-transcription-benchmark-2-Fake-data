# Class encapsulating a fake rainfall data image

import os
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
        self.pageWidth = 768
        self.pageHeight = 1024
        self.xscale = 1.0
        self.yscale = 1.0
        self.xshift = 0.0  # pixels, +ve right
        self.yshift = 0.0  # pixels, +ve up
        self.rotate = 0.0  # degrees clockwise (not yet implemented)
        self.linewidth = 1.0
        self.bgcolour = (1.0, 1.0, 1.0)
        self.fgcolour = (0.0, 0.0, 0.0)
        self.yearHeight = 0.066  # Fractional height of year row
        self.totalsHeight = 0.105  # Fractional height of totals row
        self.monthsWidth = 0.137  # Fractional width of months row
        self.meansWidth = 0.107  # Fractional width of means row
        self.fontSize = 10
        self.year = 1941

        self.generateNumbers()

        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key)
            else:
                raise ValueError("No parameter %s" % key)

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
        self.drawBox(ax_full)
        self.drawGrid(ax_full)
        self.drawFixedText(ax_full)
        self.drawNumbers(ax_full)
        self.drawMeans(ax_full)
        self.drawTotals(ax_full)
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

    # Calculate the grid geometry
    #   currently ignores rotating
    def topLeft(self):
        return (
            0.07 + self.xshift / self.pageWidth,
            0.725 + self.yshift / self.pageHeight,
        )

    def topRight(self):
        return (
            0.93 + self.xshift / self.pageWidth + (self.xscale - 1) * 0.86,
            0.725 + self.yshift / self.pageHeight,
        )

    def bottomLeft(self):
        return (
            0.07 + self.xshift / self.pageWidth,
            0.325 + self.yshift / self.pageHeight - (self.yscale - 1) * 0.4,
        )

    def bottomRight(self):
        return (
            0.93 + self.xshift / self.pageWidth + (self.xscale - 1) * 0.86,
            0.325 + self.yshift / self.pageHeight - (self.yscale - 1) * 0.4,
        )

    # Point fraction x along top of grid
    def topAt(self, x):
        return (
            self.topRight()[0] * x + self.topLeft()[0] * (1 - x),
            self.topRight()[1] * x + self.topLeft()[1] * (1 - x),
        )

    # Fraction x along bottom of grid
    def bottomAt(self, x):
        return (
            self.bottomRight()[0] * x + self.bottomLeft()[0] * (1 - x),
            self.bottomRight()[1] * x + self.bottomLeft()[1] * (1 - x),
        )

    # Fraction y of way up left side
    def leftAt(self, y):
        return (
            self.topLeft()[0] * y + self.bottomLeft()[0] * (1 - y),
            self.topLeft()[1] * y + self.bottomLeft()[1] * (1 - y),
        )

    # Fraction y of way up right side
    def rightAt(self, y):
        return (
            self.topRight()[0] * y + self.bottomRight()[0] * (1 - y),
            self.topRight()[1] * y + self.bottomRight()[1] * (1 - y),
        )

    # Draw grid bounding box
    def drawBox(self, ax):
        ax.add_line(
            Line2D(
                xdata=(
                    self.topLeft()[0],
                    self.topRight()[0],
                    self.bottomRight()[0],
                    self.bottomLeft()[0],
                    self.topLeft()[0],
                ),
                ydata=(
                    self.topLeft()[1],
                    self.topRight()[1],
                    self.bottomRight()[1],
                    self.bottomLeft()[1],
                    self.topLeft()[1],
                ),
                linestyle="solid",
                linewidth=self.linewidth,
                color=self.fgcolour,
                zorder=1,
            )
        )

    # Draw the grid
    def drawGrid(self, ax):
        lft = self.leftAt(1.0 - self.yearHeight)
        rgt = self.rightAt(1.0 - self.yearHeight)
        ax.add_line(
            Line2D(
                xdata=(lft[0], rgt[0]),
                ydata=(lft[1], rgt[1]),
                linestyle="solid",
                linewidth=self.linewidth,
                color=self.fgcolour,
                zorder=1,
            )
        )
        lft = self.leftAt(self.totalsHeight)
        rgt = self.rightAt(self.totalsHeight)
        ax.add_line(
            Line2D(
                xdata=(lft[0], rgt[0]),
                ydata=(lft[1], rgt[1]),
                linestyle="solid",
                linewidth=self.linewidth,
                color=self.fgcolour,
                zorder=1,
            )
        )
        tp = self.topAt(self.monthsWidth)
        bm = self.bottomAt(self.monthsWidth)
        ax.add_line(
            Line2D(
                xdata=(tp[0], bm[0]),
                ydata=(tp[1], bm[1]),
                linestyle="solid",
                linewidth=self.linewidth,
                color=self.fgcolour,
                zorder=1,
            )
        )
        tp = self.topAt(1.0 - self.meansWidth)
        bm = self.bottomAt(1.0 - self.meansWidth)
        ax.add_line(
            Line2D(
                xdata=(tp[0], bm[0]),
                ydata=(tp[1], bm[1]),
                linestyle="solid",
                linewidth=self.linewidth,
                color=self.fgcolour,
                zorder=1,
            )
        )
        for yrl in range(1, 10):
            x = self.monthsWidth + yrl * (1.0 - self.meansWidth - self.monthsWidth) / 10
            tp = self.topAt(x)
            bm = self.bottomAt(x)
            ax.add_line(
                Line2D(
                    xdata=(tp[0], bm[0]),
                    ydata=(tp[1], bm[1]),
                    linestyle="solid",
                    linewidth=self.linewidth,
                    color=self.fgcolour,
                    zorder=1,
                )
            )

    # Add the fixed text
    def drawFixedText(self, ax):
        tp = self.topAt(self.monthsWidth / 2)
        lft = self.leftAt(1.0 - self.yearHeight / 2)
        ax.text(
            tp[0],
            lft[1],
            "Year",
            fontsize=self.fontSize,
            horizontalalignment="center",
            verticalalignment="center",
        )
        tp = self.topAt(1.0 - self.meansWidth / 2)
        lft = self.leftAt(1.0 - self.yearHeight / 2)
        ax.text(
            tp[0],
            lft[1],
            "Means",
            fontsize=self.fontSize,
            horizontalalignment="center",
            verticalalignment="center",
        )
        tp = self.topAt(self.monthsWidth / 2)
        lft = self.leftAt(self.totalsHeight / 2)
        ax.text(
            tp[0],
            lft[1],
            "Totals",
            fontsize=self.fontSize,
            horizontalalignment="center",
            verticalalignment="center",
        )
        months = (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        )
        tp = self.topAt(self.monthsWidth / 10)
        for mdx in range(len(months)):
            lft = self.leftAt(
                1.0
                - self.yearHeight
                - (mdx + 1)
                * (1.0 - self.yearHeight - self.totalsHeight)
                / (len(months) + 1)
            )
            ax.text(
                tp[0],
                lft[1],
                months[mdx],
                fontsize=self.fontSize - 1,
                horizontalalignment="left",
                verticalalignment="center",
            )
        lft = self.leftAt(1.0 - self.yearHeight / 2)
        for ydx in range(10):
            x = (
                self.monthsWidth
                + (ydx + 0.5) * (1.0 - self.meansWidth - self.monthsWidth) / 10
            )
            tp = self.topAt(x)
            ax.text(
                tp[0],
                lft[1],
                "%04d" % (self.year + ydx),
                fontsize=self.fontSize,
                horizontalalignment="center",
                verticalalignment="center",
            )

    # Generate random numbers to fill out the data table
    #  Each month's data is represented by 3 integers (0-9) - x, y, and z
    #  where the accumulated rainfall for that month is x.yz inches.
    def generateNumbers(self):
        self.rdata = []
        for yri in range(10):
            ydata = []
            for mni in range(12):
                mdata = []
                for pni in range(3):
                    mdata.append(random.randint(0, 9))
                ydata.append(mdata)
            self.rdata.append(ydata)

    # Fill out the table with the random numbers
    def drawNumbers(self, ax):
        for yri in range(10):
            x = (
                self.monthsWidth
                + (yri + 0.5) * (1.0 - self.meansWidth - self.monthsWidth) / 10
            )
            tp = self.topAt(x)
            for mni in range(12):
                lft = self.leftAt(
                    1.0
                    - self.yearHeight
                    - (mni + 1) * (1.0 - self.yearHeight - self.totalsHeight) / (12 + 1)
                )
                inr = (
                    self.rdata[yri][mni][0]
                    + self.rdata[yri][mni][1] / 10
                    + self.rdata[yri][mni][2] / 100
                )
                strv = "%4.2f" % inr
                ax.text(
                    tp[0],
                    lft[1],
                    strv,
                    fontsize=self.fontSize,
                    horizontalalignment="center",
                    verticalalignment="center",
                )
                # Make certain numbers are identical to printed version
                self.rdata[yri][mni][0] = int(strv[0])
                self.rdata[yri][mni][1] = int(strv[2])
                self.rdata[yri][mni][2] = int(strv[3])

    # Add the monthly means
    def drawMeans(self, ax):
        tp = self.topAt(1.0 - self.meansWidth / 2)
        self.rdata.append([])
        for mni in range(12):
            lft = self.leftAt(
                1.0
                - self.yearHeight
                - (mni + 1) * (1.0 - self.yearHeight - self.totalsHeight) / (12 + 1)
            )
            inr = 0.0
            for yri in range(10):
                inr += (
                    self.rdata[yri][mni][0]
                    + self.rdata[yri][mni][1] / 10
                    + self.rdata[yri][mni][2] / 100
                )
            inr /= 10
            strv = "%04.2f" % inr
            ax.text(
                tp[0],
                lft[1],
                strv,
                fontsize=self.fontSize,
                horizontalalignment="center",
                verticalalignment="center",
            )
            mm = []
            mm.append(int(strv[0]))
            mm.append(int(strv[2]))
            mm.append(int(strv[3]))
            self.rdata[10].append(mm)

    # Add the annual totals
    def drawTotals(self, ax):
        lft = self.leftAt(self.totalsHeight / 2)
        self.rdata.append([])
        for yri in range(10):
            x = (
                self.monthsWidth
                + (yri + 0.5) * (1.0 - self.meansWidth - self.monthsWidth) / 10
            )
            tp = self.topAt(x)
            inr = 0.0
            for mni in range(12):
                inr += (
                    self.rdata[yri][mni][0]
                    + self.rdata[yri][mni][1] / 10
                    + self.rdata[yri][mni][2] / 100
                )
            if inr > 99:
                inr = inr % 100
            strv = "%05.2f" % inr
            ax.text(
                tp[0],
                lft[1],
                strv,
                fontsize=self.fontSize,
                horizontalalignment="center",
                verticalalignment="center",
            )
            at = []
            at.append(int(strv[0]))
            at.append(int(strv[1]))
            at.append(int(strv[3]))
            at.append(int(strv[4]))
            self.rdata[11].append(at)
