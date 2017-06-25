from __future__ import print_function
from setuptools import setup
from ar_markers.version import __version__ as VERSION
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution


PACKAGE_NAME = 'ar_markers'
BuildCommand.pkg = PACKAGE_NAME
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION
README = open('readme.rst').read()

setup(
	name=PACKAGE_NAME,
	version=VERSION,
	author="Kevin Walchko",
	keywords=['framework', 'robotic', 'robot', 'vision', 'ros', 'distributed'],
	author_email="walchko@github.users.noreply.com",
	description="A python robotic framework and tools",
	license="MIT",
	classifiers=[
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.6',
		'Operating System :: Unix',
		'Operating System :: POSIX :: Linux',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: POSIX',
		'Topic :: Scientific/Engineering',
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
		'Topic :: Scientific/Engineering :: Image Recognition',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],
	install_requires=[
		'build_utils'
	],
	url="https://github.com/walchko/{}".format(PACKAGE_NAME),
	long_description=README,
	packages=[PACKAGE_NAME],
	cmdclass={
		'publish': PublishCommand,
		'make': BuildCommand
	},
	scripts=[
		'bin/ar_marker_generate.py',
		'bin/ar_marker_scan.py'
	]
)
