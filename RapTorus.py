import Gmodule.gExtract as gExtract
from Gmodule.WCanv import MFrame
from Gmodule.constants import constants
from threading import Thread
import time

#initializing vizulization constants for model
cons=constants()
print('constants initialized')

## open stl file
print('exctracting geometry from file')
path='D:/tre.stl'
model,cmass=gExtract.eSTL(path)
print('stl surface elements: ',len(model))

##assign geometry
cons.vect=model
cons.cmass_xyz=cmass
cons.Gwidgets.append('geometry')
print('model assigned to constants')

## Initialize
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



