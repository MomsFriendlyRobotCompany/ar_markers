#!/usr/bin/env python3

import cv2
from ar_markers import detect_markers


img = cv2.imread('image-0.png')
markers = detect_markers(img)
print(markers)

for m in markers:
    print(">> Found:", m.id)
