#!/usr/bin/env python3

from __future__ import print_function
import cv2
from ar_markers import detect_markers

cnt = 0
mrkdet = False

window_size = (640, 480)
cam = cv2.VideoCapture(0)
cam.set(3, window_size[0])  # set width
cam.set(4, window_size[1])  # set height

while True:
    ret, im = cam.read()

    if ret:
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        if mrkdet:
            markers = detect_markers(im)
            for mark in markers:
                im = mark.highlite_marker(im)

        cv2.imshow('image', im)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        elif key == ord("s"):
            cv2.imwrite("image-{}.png".format(cnt), im)
            print('>> Wrote: {}'.format("image-{}.png".format(cnt)))
            cnt += 1
        elif key == ord("m"):
            mrkdet = not mrkdet
            print("*** Detecting Markers: {} ***".format(mrkdet))

cam.release()
cv2.destroyAllWindows()
