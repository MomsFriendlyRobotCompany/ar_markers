#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
    name='ar_markers',
    version='1.0',
    packages=find_packages(),
    install_requires=['numpy'],
    # scripts=[
    #     'ar_markers/scripts/ar_markers_generate_marker.py',
    #     'ar_markers/scripts/ar_markers_livetest.py'
    # ],
    setup_requires=[],
    author='Max Brauer',
    # author_email='max@max-brauer.com',
    description='Detection of hamming markers for OpenCV written in python',
    url='https://github.com/walchko/ar_markers',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
)
