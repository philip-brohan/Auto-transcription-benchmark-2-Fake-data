#!/usr/bin/env python

# Make 10,000 fake images, each with associated data file
#  These images have a random perturbations in shift, scale, and rotation).

import os
import random

image_dir = "%s/OCR-fake/images" % os.getenv("SCRATCH")

f = open("run_mi.sh", "w+")

for idx in range(10000):
    fn = "%s/%04d.png" % (image_dir, idx)
    if os.path.exists(fn):
        continue
    xshift = random.randint(-10, 10)
    yshift = random.randint(-20, 20)
    xscale = random.normalvariate(1, 0.03)
    yscale = random.normalvariate(1, 0.03)
    rotate = random.normalvariate(0, 3)
    f.write(
        (
            '../make_image_data_pair.py --opdir=%s/OCR-fake/ --docn="%04d"'
            + " --xshift=%d --yshift=%d --xscale=%f --yscale=%f"
            + " --rotate=%f\n"
        )
        % (os.getenv("SCRATCH"), idx, xshift, yshift, xscale, yscale, rotate)
    )
