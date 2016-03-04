from threading import Thread
import time
import sys
import os
# add module folders to path
sys.path.append(os.getcwd()+'/Gmodule')
import gExtract as gExtract
from MainFrame import MFrame
from constants import constants

#initializing vizulization constants for model and also variables space
cons=constants()
print('constants initialized')

## open stl file
print('exctracting geometry from file')
path='D:/tre.stl'
try:
    model,cmass=gExtract.eSTL(path) # model=[[normal,vecn1,vecn2,vecn3],... ](triangles); cmass = (x,y,z)
    print('stl surface elements: ',len(model))
except:
    print('no model detected. sry')

##assign geometry
cons.vect=model
cons.cmass_xyz=cmass
cons.Gwidgets.append('geometry')
print('model assigned to constants')

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



