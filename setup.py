from setuptools import setup

CLASSIFIERS = """\
Development Status :: 4 - Beta
Intended Audience :: Science/Research
License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)
Operating System :: MacOS
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Programming Language :: Python
Topic :: Scientific/Engineering

"""

setup(
    name='roibuddy',
    version='1.0.0-dev',
    packages=['roibuddy'],
    entry_points={'gui_scripts': ['roibuddy = roibuddy.roi_buddy:main']},
    install_requires=[
        'sima',
        'guiqwt>=2.1.6',
        'guidata>=1.4.1',
    ],
    author="The SIMA Development Team",
    author_email="software@losonczylab.org",
    description="GUI for editing segmentations when using SIMA",
    license="GNU GPLv2",
    url="http://www.losonczylab.org/sima/",
    keywords="imaging microscopy neuroscience segmentation",
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    platforms=["Linux", "Mac OS-X", "Windows"],
)
