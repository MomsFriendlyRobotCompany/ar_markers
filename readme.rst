.. image:: https://raw.githubusercontent.com/walchko/ar_markers/master/pics/marker.png
	:target: https://github.com/walchko/ar_markers

ar_markers
=================
.. image:: https://img.shields.io/pypi/l/ar_markers.svg
	:target: https://github.com/walchko/ar_markers
.. image:: https://img.shields.io/pypi/pyversions/ar_markers.svg
	:target: https://github.com/walchko/ar_markers
.. image:: https://img.shields.io/pypi/wheel/ar_markers.svg
	:target: https://github.com/walchko/ar_markers
.. image:: https://img.shields.io/pypi/v/ar_markers.svg
	:target: https://github.com/walchko/ar_markers

Detection of hamming markers for OpenCV written in python.

Originally written by Max Brauer: `github <https://github.com/DebVortex/python-ar-markers>`_.
All I did was clean up some little stuff and package it for use on pypi.

This package is able to read and create hamming markers, described in
`this blogpost <http://iplimage.com/blog/approach-encodedecode-black-white-marker/>`_.

Purpose
--------

This project was for a robotics/computer vision `class <https://github.com/MarsUniversity/ece387>`_
I taught Spring 2018. I wanted something simple enough we could go through the
code and they could understood how it worked. I also taught them OpenCV, so
I wanted something written in that. Eventually we made "street signs" and the
students drove Roomba robots around on these "strees" (ok, really it was 3 inch
wide black tape for the roads). When they detected an intersection, they used
a camera to read the street sign (ar marker) and it told them to: go straight,
turn left, or turn right.

Sometimes it isn't as robust as I would like, so you may have to move the target
around before it gets recognized.

Install
---------

The simplest way to install is::

  pip install ar_markers

You will also need OpenCV 3.x as a minimum. On macOS you can do::

	brew install opencv

Usage
-------------

There are two helper scripts:

- ``ar_markers_generate.py`` to generate the markers. Do ``ar_markers_generate.py --help``
  to see the options
- ``ar_markers_scan.py`` to scan the marker. Once you have created and printed out a
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

BSD License
-------------

Copyright (c) 2007, Max Brauer
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
