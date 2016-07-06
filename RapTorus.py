from initialization import *

## open mesh file
print('exctracting geometry from file')
path='D:/el_ex.txt'
cons1=mshExtract.mExt(path)
cons1.Gwidgets.append('mesh')
print('stl surface elements: ',len(cons1.vect))

c=[cons1]
## Initialize Main Frame with specific constants
MFrame(c)
