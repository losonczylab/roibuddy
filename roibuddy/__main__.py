from __future__ import absolute_import

import sys

# NOTE: The import order of PyQt, guidata, and guiqwt is very import and
# will cause import errors if changed.
# The order is correct in roi_buddy.py, so the import from there must be first.
from .roi_buddy import RoiBuddy

from PyQt4.QtGui import QApplication

def main():
    app = QApplication(sys.argv)
    form = RoiBuddy()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
