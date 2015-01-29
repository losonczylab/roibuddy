import numpy as np


def add_item_with_z_offset(self, item, zoffset):
    """
    Add a plot *item* instance within a specified z range, over *zmin*
    """
    zlist = sorted([_it.z() for _it in self.items
                    if _it.z() >= zoffset]+[zoffset-1])
    dzlist = np.argwhere(np.diff(zlist) > 1)
    if len(dzlist) == 0:
        z = max(zlist)+1
    else:
        z = zlist[dzlist[0, 0]] + 1
    self.add_item(item, z=z)
