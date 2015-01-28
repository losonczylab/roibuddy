from setuptools import setup
setup(
    name='ROIBuddy',
    version='1.0.0-dev',
    author_email='software@losonczylab.org',
    url='http://www.losonczylab.org/sima/roibuddy',
    license='GNU General Public License (GPL)',
    packages=['ROIBuddy'],
    entry_points={'gui_scripts': ['roibuddy = ROIBuddy.roi_buddy:main']}
)
