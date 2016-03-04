#constants and variables < -- this part must be reorganizd greatly
class constants:

    ##### Visualization
    wsize=(800,600)
    
    light=(-1,-1,100)
    #direct=(0,0,1)
    c=100,100
    scale_factor=10
    cmass_xyz=(150,80,100)

    rot_factor=100 # this is z component of ruling vector
    base_vec=(0,0,1)
    start_rot=(0,0)
    rot_axis=(1,0,0)
    angl=0

    position_xy=(wsize[0]/2,wsize[1]/2)
    cur_position_xy=position_xy
    cursor_start_xy=(0,0)

    vect=[]
    subvect=[]

    ##### Widgets controlling
    Gwidgets = []

    ##### Mechanical
