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

#initializing vizulization constants for model and also variables space
cons=constants()
print('constants initialized')

## open stl file
print('exctracting geometry from file')
path='D:/tre.stl'
cons=gExtract.eSTL(path) # model=[[normal,vecn1,vecn2,vecn3],... ](triangles); cmass = (x,y,z)
print('stl surface elements: ',len(model))
##assign geometry
cons.Gwidgets.append('geometry')
print('model assigned to constants')

## open mesh file
#print('exctracting geometry from file')
#path='D:/el_ex.txt'
#model,cmass=mshExtract.mExt(path)
#print('stl surface elements: ',len(model))


## Initialize Main Frame with specific constants
MFrame(cons)

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



