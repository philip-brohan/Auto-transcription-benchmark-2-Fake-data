#!/usr/bin/env python

# Make 10,000 fake images, each with associated data file
#  These images have a random (uniform) shift in both x and y).

import os
import random

image_dir = "%s/OCR-fake/images" % os.getenv("SCRATCH")

f = open("run_mi.sh", "w+")

for idx in range(10000):
    fn = "%s/%04d.png" % (image_dir, idx)
    if os.path.exists(fn):
        continue
    xshift=random.randint(-10,10)
    yshift=random.randint(-20,20)
    f.write(
        ('../make_image_data_pair.py --opdir=%s/OCR-fake/ --docn="%04d"' +
         ' --xshift=%d --yshift=%d\n' )
         % (os.getenv("SCRATCH"), idx, xshift,yshift)
    )
