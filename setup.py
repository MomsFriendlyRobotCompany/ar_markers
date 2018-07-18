from __future__ import print_function
from setuptools import setup
# from ar_markers.version import __version__ as VERSION
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution
from build_utils import SetGitTag
from build_utils import get_pkg_version


VERSION = get_pkg_version('ar_markers/__init__.py')
PACKAGE_NAME = 'ar_markers'
BuildCommand.pkg = PACKAGE_NAME
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION
SetGitTag.version = VERSION
README = open('readme.rst').read()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author="Kevin Walchko",
    keywords=['framework', 'robotic', 'marker', 'vision', 'ar marker', 'ar'],
    author_email="walchko@github.users.noreply.com",
    description="A python robotic framework and tools",
    license="BSD",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
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
        'build_utils', 'numpy'
    ],
    url="https://github.com/MomsFriendlyRobotCompany/{}".format(PACKAGE_NAME),
    long_description=README,
    packages=[PACKAGE_NAME],
    cmdclass={
        'publish': PublishCommand,
        'make': BuildCommand,
        'git': SetGitTag
    },
    scripts=[
        'bin/ar_markers_generate.py',
        'bin/ar_markers_scan.py'
    ]
)
