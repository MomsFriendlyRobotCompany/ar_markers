.. image:: https://raw.githubusercontent.com/walchko/ar_markers/master/pics/marker.png
	:target: https://github.com/walchko/ar_markers

ar_markers
=================
.. image:: https://img.shields.io/pypi/l/ar_marker.svg
	:target: https://github.com/walchko/ar_markers
.. image:: https://img.shields.io/pypi/pyversions/ar_marker.svg
	:target: https://github.com/walchko/ar_markers
.. image:: https://img.shields.io/pypi/wheel/ar_marker.svg
	:target: https://github.com/walchko/ar_markers
.. image:: https://img.shields.io/pypi/v/ar_marker.svg
	:target: https://github.com/walchko/ar_markers

Detection of hamming markers for OpenCV written in python.

Originally written by Max Brauer: `github <https://github.com/DebVortex/python-ar-markers>`_.
All I did was clean up some little stuff and package it for use on pypi.

This package is able to read and create hamming markers, described in
`this blogpost <http://iplimage.com/blog/approach-encodedecode-black-white-marker/>`_.

Install
---------

The simplest way to install is::

  pip install ar_markers

Usage
-------------

There are two helper scripts:

- ``ar_marker_generate.py`` to generate the markers. Do ``ar_marker_generate.py --help``
  to see the options
- ``ar_marker_scan.py`` to scan the marker. Once you have created and printed out a
  marker, hold the marker in front of your camera. You will see a blue border around
  the marker, (if detected) and a green number, showing the ID the marker
  represents.

or use in a program like:

.. code-block:: python

	#!/usr/bin/env python

	from __future__ import print_function
	import cv2
	from ar_markers import detect_markers


	if __name__ == '__main__':
		print('Press "q" to quit')
		capture = cv2.VideoCapture(0)

		if capture.isOpened():  # try to get the first frame
			frame_captured, frame = capture.read()
		else:
			frame_captured = False
			
		while frame_captured:
			markers = detect_markers(frame)
			for marker in markers:
				marker.highlite_marker(frame)
			cv2.imshow('Test Frame', frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
			frame_captured, frame = capture.read()

		# When everything done, release the capture
		capture.release()
		cv2.destroyAllWindows()

License
---------

GPL v3
