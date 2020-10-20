#!/usr/bin/env python

# Make 10,000 fake box images, each with associated data file
#  These images have a random perturbations in font, shift, scale, and rotation).

import os
import random

# Get the list of fonts to use
from fonts import fontNames
from fonts import fontScales

image_dir = "%s/OCR-fake-box/images" % os.getenv("SCRATCH")

f = open("run_mi.sh", "w+")

for idx in range(10000):
    fn = "%s/%04d.png" % (image_dir, idx)
    if os.path.exists(fn):
        continue
    fontFamily = random.choice(fontNames)
    fontStyle = random.choice(["normal", "italic", "oblique"])
    fontWeight = random.choice(["normal", "bold", "light"])
    fontSize = 12
    if fontFamily in fontScales:
        fontSize *= fontScales[fontFamily]
    jitterFontRotate = random.normalvariate(0, 3)
    jitterFontSize = random.normalvariate(0, 1)
    jitterGridPoints = random.normalvariate(0, 0.001)
    f.write(
        (
            './make_image_data_pair.py --opdir=%s/OCR-fake-box/ --docn="%04d"'
            + " --jitterFontRotate=%f --jitterFontSize=%f"
            + " --jitterGridPoints=%f --fontFamily='%s' --fontSize=%f"
            + " --fontStyle=%s --fontWeight=%s\n"
        )
        % (
            os.getenv("SCRATCH"),
            idx,
            jitterFontRotate,
            jitterFontSize,
            jitterGridPoints,
            fontFamily,
            fontSize,
            fontStyle,
            fontWeight,
        )
    )
