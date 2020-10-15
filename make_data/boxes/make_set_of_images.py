#!/usr/bin/env python

# Make 10,000 fake box images, each with associated data file
#  These images have a random perturbations in shift, scale, and rotation).

import os
import random

image_dir = "%s/OCR-fake-box/images" % os.getenv("SCRATCH")

f = open("run_mi.sh", "w+")

for idx in range(10000):
    fn = "%s/%04d.png" % (image_dir, idx)
    if os.path.exists(fn):
        continue
    jitterFontRotate = random.normalvariate(0, 3)
    jitterFontSize = random.normalvariate(0, 1)
    jitterGridPoints = random.normalvariate(0, 0.001)
    f.write(
        (
            './make_image_data_pair.py --opdir=%s/OCR-fake-box/ --docn="%04d"'
            + " --jitterFontRotate=%f --jitterFontSize=%f"
            + " --jitterGridPoints=%f\n"
        )
        % (
            os.getenv("SCRATCH"),
            idx,
            jitterFontRotate,
            jitterFontSize,
            jitterGridPoints,
        )
    )
