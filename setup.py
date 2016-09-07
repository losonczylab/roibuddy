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
    version='1.0.1',
    packages=['roibuddy'],
    entry_points={'gui_scripts': ['roibuddy = roibuddy.__main__:main']},
    install_requires=[
        'sima>=1.0.0',
        'guiqwt>=3.0.0',
        'guidata>=1.7.0',
        'pythonqwt',
    ],
    package_data={
        'roibuddy': [
            'icons/*'
        ]
    },
    author="The SIMA Development Team",
    author_email="software@losonczylab.org",
    description="GUI for editing segmentations when using SIMA",
    license="GNU GPLv2",
    url="http://www.losonczylab.org/sima/",
    keywords="imaging microscopy neuroscience segmentation",
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    platforms=["Linux", "Mac OS-X", "Windows"],
)
