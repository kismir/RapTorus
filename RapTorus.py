from threading import Thread
import time
import sys
import os
# add module folders to path
sys.path.append(os.getcwd()+'/Gmodule')
sys.path.append(os.getcwd()+'/MSHmodule')
import gExtract
import mshExtract
from MainFrame import MFrame
from constants import constants

## open stl file
print('exctracting geometry from file')
path='D:/tre.stl'
cons=gExtract.eSTL(path) # model=[[normal,vecn1,vecn2,vecn3],... ](triangles); cmass = (x,y,z)
print('stl surface elements: ',len(cons.vect))
##assign geometry
cons.Gwidgets.append('geometry')
print('model assigned to constants')


## open mesh file
print('exctracting geometry from file')
path='D:/el_ex.txt'
cons1=mshExtract.mExt(path)
cons1.Gwidgets.append('mesh')
print('stl surface elements: ',len(cons1.vect))

c=[cons,cons1]
## Initialize Main Frame with specific constants
MFrame(c)

#t = Thread(target=MFrame, args=(cons,))
#t.start()
#def r(cons):
#    while 1:
#        time.sleep(0.5)
#        print('ok')
#p = Thread(target=r, args=(cons,))
#p.start()
#p.join()
#t.join()



