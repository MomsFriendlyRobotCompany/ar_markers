.. image:: https://raw.githubusercontent.com/walchko/ar_markers/master/pics/marker.png
	:target: https://github.com/walchko/ar_markers

ar-markers
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

Helperscripts
-------------

There are two helper scripts:

- ``ar_marker_generate.py`` to generate the markers. Do ``ar_marker_generate.py --help``
  to see the options
- ``ar_marker_scan.py`` to scan the marker. Once you have created and printed out a
  marker, hold the marker into your camera. You will see a blue border around
  the marker, (if detected) and a green number, showing the ID the marker
  represents.

License
---------

GPL v3
