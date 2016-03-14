#constants and variables < -- this part must be reorganizd greatly
class constants:
    def __init__(self):

        ##### Visualization
        self.wsize=(800,600)
        
        self.light=(-1,-1,100)
        #direct=(0,0,1)
        self.c=100,100
        self.scale_factor=3.5
        self.cmass_xyz=(150,80,100)

        self.rot_factor=100 # this is z component of ruling vector
        self.base_vec=(0,0,1)
        self.start_rot=(0,0)
        self.rot_axis=(1,0,0)
        self.angl=0

        self.position_xy=(self.wsize[0]/2,self.wsize[1]/2)
        self.cur_position_xy=self.position_xy
        self.cursor_start_xy=(0,0)

        self.vect=[]
        self.subvect=[]

        ##### Widgets controlling
        self.Gwidgets = []

        ##### Mechanical
