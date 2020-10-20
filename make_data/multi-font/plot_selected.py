#!/usr/bin/env python

# Show examples of digits in all available fonts

import matplotlib.font_manager

import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

# Pick some selected fonts (system dependent)
names = [
    "AR PL UKai CN",
    "AR PL UMing CN",
    "Abyssinica SIL",
    "Andale Mono",
    "AnjaliOldLipi",
    "Arial",
    "Arial Black",
    "BPG Chveulebrivi GPL&GNU",
    "BPG Courier GPL&GNU",
    "BPG Glaho GPL&GNU",
    "C059",
    "Caladea",
    "Cantarell",
    "Carlito",
    "Comic Sans MS",
    "Courier New",
    "David CLM",
    "DejaVu Sans",
    "DejaVu Sans Mono",
    "DejaVu Serif",
    "Dyuthi",
    "Frank Ruehl CLM",
    "FreeMono",
    "FreeSans",
    "FreeSerif",
    "Garuda",
    "Georgia",
    "Gubbi",
    "Hadasim CLM",
    "IPAGothic",
    "IPAMincho",
    "IPAPGothic",
    "IPAPMincho",
    "Impact",
    "Jomolhari",
    "KacstScreen",
    "KacstTitle",
    "KacstTitleL",
    "Kalyani",
    "Keter YG",
    "Khmer OS",
    "Khmer OS Siemreap",
    "Khmer OS System",
    "Kinnari",
    "Liberation Mono",
    "Liberation Sans",
    "Liberation Sans Narrow",
    "Liberation Serif",
    "Lohit Assamese",
    "Lohit Devanagari",
    "Lohit Gujarati",
    "Lohit Kannada",
    "Lohit Marathi",
    "Lohit Punjabi",
    "Lohit Tamil",
    "Loma",
    "Meera",
    "Miriam CLM",
    "Miriam Mono CLM",
    "Nafees Web Naskh",
    "Nanum Brush Script",
    "Nanum Pen Script",
    "NanumGothic",
    "NanumMyeongjo",
    "Navilu",
    "Nimbus Mono PS",
    "Nimbus Roman",
    "Nimbus Sans",
    "Nimbus Sans Narrow",
    "Norasi",
    "Noto Sans",
    "Noto Sans Devanagari",
    "Noto Sans Khmer",
    "Noto Sans Tamil",
    "Noto Sans UI",
    "Noto Serif",
    "Noto Serif Lao",
    "Nuosu SIL",
    "Open Sans",
    "OpenSymbol",
    "Overpass",
    "P052",
    "PT Sans",
    "PT Sans Narrow",
    "Padauk",
    "PakType Naqsh",
    "Pothana2000",
    "Purisa",
    "Rachana",
    "RaghuMalayalam",
    "STIX",
    "STIXGeneral",
    "Saab",
    "Sawasdee",
    "Simple CLM",
    "Stam Ashkenaz CLM",
    "Stone Sans ITC TT",
    "Stone Sans Sem ITC TT",
    "Stone Serif ITC TT",
    "Stone Serif Sem ITC TT",
    "Suruma",
    "Tahoma",
    "Tibetan Machine Uni",
    "Times New Roman",
    "Tlwg Typist",
    "Trebuchet MS",
    "URW Bookman",
    "URW Gothic",
    "Umpush",
    "Unikurd Web",
    "VL Gothic",
    "VL PGothic",
    "Vemana2000",
    "Verdana",
    "Waree",
    "WenQuanYi Micro Hei",
    "WenQuanYi Zen Hei",
    "Z003",
    "cmb10",
    "cmr10",
    "cmtt10",
    "eufm10",
    "kacstPen",
]

scales = {"Nanum Brush Script": 1.5, "Nanum Pen Script": 1.5}


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
    scale = 1
    if names[fi] in scales:
        scale = scales[names[fi]]
    x = int(fi / 50) * 0.30 + 0.02
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
        x + 0.18,
        y,
        "0.123456789",
        fontdict={
            "family": names[fi],
            "size": 22 * scale,
            "style": "normal",
            "weight": "normal",
        },
        horizontalalignment="left",
        verticalalignment="top",
    )


fig.savefig("selected.png")
