.. image:: pics/marker.png
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


::

  pip install ar_markers

Helperscripts
-------------

There are two helperscripts located in ``ar_markers/scripts``. ``generate_marker`` to generate the markers and `livetest`. To do the ``livetest``, first generate some markers and print them out. After that, start the livetest and hold the marker into your camera. You will see a blue border around the marker, (if detected) and a green number, showing the ID the marker represents.

License
---------

GPL v3
