import numpy as np

import pfplot as pf
print('pfplot version {}'.format(pf.ver()))

pf.cfg()
x = np.linspace(0, 11, 12)
y = 2 * x
z = 3 * x
pf.plot(x, y, 'test')
pf.plot(x, z, 'test2')
pf.set_labels('Time (min.)', 'Fluorescence Intensity (a.u.)')
pf.show()
