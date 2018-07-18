#!/usr/bin/env python3

from __future__ import print_function
import cv2
from ar_markers import detect_markers
from opencvutils.CameraCalibrate import CameraCalibration
import time
import numpy as np

def calibrate(cam):
    imgs = []
    for i in range(10):
        # time.sleep(1)
        ok, im = cam.read()
        if ok:
            imgs.append(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY))
            print("*** captured image {} ***".format(i))
            cv2.imshow('image', im)
            cv2.waitKey(1000)

    cal = CameraCalibration()
    cal.marker_checkerboard = True
    info = cal.calibrate(imgs, marker_size=(9, 6))
    cal.printMatrix()
    print(">>", info)
    return info

def undistort(image, mtx, dist, alpha=0.5):
    """
    image: an image
    alpha = 0: returns undistored image with minimum unwanted pixels (image
                pixels at corners/edges could be missing)
    alpha = 1: retains all image pixels but there will be black to make up
                for warped image correction
    """
    h,w = image.shape[:2]
    # mtx = self.data['camera_matrix']
    # dist = self.data['dist_coeff']
    # Adjust the calibrations matrix
    # alpha=0: returns undistored image with minimum unwanted pixels (image pixels at corners/edges could be missing)
    # alpha=1: retains all image pixels but there will be black to make up for warped image correction
    # returns new cal matrix and an ROI to crop out the black edges
    newcameramtx, _ = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), alpha)
    # undistort
    ret = cv2.undistort(image, mtx, dist, None, newcameramtx)
    return ret


cnt = 0
mrkdet = False
camera_calibrated = False
cal_info = {'camera_matrix': np.array([[1.21993326e+03, 0.00000000e+00, 2.26144165e+02],
       [0.00000000e+00, 1.20871399e+03, 4.10356637e+02],
       [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]), 'dist_coeff': np.array([[-2.12366745e-01,  1.08876662e+00, -1.52749901e-03,
         4.71534727e-03, -1.53711160e+00]]), 'rms': 0.8719776863403512}

window_size = (640, 480)
cam = cv2.VideoCapture(0)
cam.set(3, window_size[0])  # set width
cam.set(4, window_size[1])  # set height

while True:
    ret, im = cam.read()

    if ret:
        if camera_calibrated:
            im = undistort(im, cal_info['camera_matrix'], cal_info['dist_coeff'])
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        if mrkdet:
            markers = detect_markers(im)
            for mark in markers:
                mark.highlite_marker(im)

        cv2.imshow('image', im)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        elif key == ord("c"):
            cal_info = calibrate(cam)

        elif key == ord("r"):
            if cal_info is not None:
                camera_calibrated = not camera_calibrated
            print(">> Camera is calibrated and Rectifying images:", camera_calibrated)

        elif key == ord("s"):
            cv2.imwrite("image-{}.png".format(cnt), im)
            print('>> Wrote: {}'.format("image-{}.png".format(cnt)))
            cnt += 1
        elif key == ord("m"):
            mrkdet = not mrkdet
            print("*** Detecting Markers: {} ***".format(mrkdet))

cam.release()
cv2.destroyAllWindows()
