#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib as mpl
import enum
import os
import numpy as np
from PIL import Image

mpl.rcParams['figure.dpi'] = 125


class Category(enum.Enum):
    dog = 0
    cat = 1


def image_to_example(path, width=64, height=64):
    filename = os.path.basename(path)

    # normalize the input image, so that we only work with images of the same size
    with Image.open(path) as img:
        resized = img.resize((width, height))

    # encoding of string labels: "dog" -> 0, "cat" -> 1
    y = Category[filename.split('.')[0]].value

    # RGB image is flattened into a one long column vector of floats,
    # that denote color intensity
    x = np.array(resized, dtype=np.float64) \
          .reshape(width * height * 3, 1) / 256.

    return x, y, path

