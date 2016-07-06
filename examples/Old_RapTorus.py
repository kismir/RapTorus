import tkinter as tk
from random import random
from math import pi,acos,sqrt,cos,sin,floor

'''http://stackoverflow.com/a/4870905
Using quaternions to represent rotation is not difficult from an algebraic point of view.
Personally, I find it hard to reason visually about quaternions,
but the formulas involved in using them for rotations are quite simple.
I'll provide a basic set of reference functions here; see this page for more.
You can think of quaternions (for our purposes) as a scalar plus a 3-d vector -- abstractly,
w + xi + yj + zk, here represented by a simple tuple (w, x, y, z).
The space of 3-d rotations is represented in full by a sub-space of the quaternions,
the space of unit quaternions, so you want to make sure that your quaternions are normalized.
You can do so in just the way you would normalize any 4-vector
(i.e. magnitude should be close to 1; if it isn't, scale down the values by the magnitude):'''

def normalize(v, tolerance=0.00001):
    mag2 = sum(n * n for n in v)
    if abs(mag2 - 1.0) > tolerance:
        mag = sqrt(mag2)
        v = tuple(n / mag for n in v)
    return v

'''Please note that for simplicity,
the following functions assume that quaternion values are already normalized.
In practice, you'll need to renormalize them from time to time,
but the best way to deal with that will depend on the problem domain.
These functions provide just the very basics, for reference purposes only.
Every rotation is represented by a unit quaternion,
and concatenations of rotations correspond to multiplications of unit quaternions.
The formula1 for this is as follows:'''

def q_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return w, x, y, z

'''To rotate a vector by a quaternion, you need the quaternion's conjugate too. That's easy:'''

def q_conjugate(q):
    w, x, y, z = q
    return (w, -x, -y, -z)

'''Now quaternion-vector multiplication is as simple as converting a vector into a quaternion
(by setting w = 0 and leaving x, y, and z the same) and then multiplying q * v * q_conjugate(q):'''

def qv_mult(q1, v1):
    q2 = (0.0,) + v1
    return q_mult(q_mult(q1, q2), q_conjugate(q1))[1:]

'''Finally, you need to know how to convert from axis-angle rotations to quaternions.
Also easy! It makes sense to "sanitize" input and output here by calling normalize.'''

def axisangle_to_q(v, theta):
    v = normalize(v)
    x, y, z = v
    theta /= 2
    w = cos(theta)
    x = x * sin(theta)
    y = y * sin(theta)
    z = z * sin(theta)
    return w, x, y, z

'''And back:'''

def q_to_axisangle(q):
    w, v = q[0], q[1:]
    theta = acos(w) * 2.0
    return normalize(v), theta

'''Here's a quick usage example.
A sequence of 90-degree rotations about the x, y, and z axes
will return a vector on the y axis to its original position. This code performs those rotations:'''


'''Keep in mind that this sequence of rotations won't return all vectors to the same position;
for example, for a vector on the x axis, it will correspond to a 90 degree rotation about the y axis.
(Keep the right-hand-rule in mind here;
a positive rotation about the y axis pushes a vector on the x axis into the negative z region.)'''


'''As always, please let me know if you find any problems here.
1. The quaternion multiplication formula looks like a crazy rat's nest,
but the derivation is simple (if tedious). Just note first that ii = jj = kk = -1; then that ij = k, jk = i, ki = j;
and finally that ji = -k, kj = -i, ik = -j.
Then multiply the two quaternions,
distributing out the terms and rearranging them based on the results of each of the 16 multiplications.
This also helps to illustrate why you can use quaternions to represent rotation;
the last six identities follow the right-hand rule,
creating bijections between rotations from i to j and rotations around k, and so on.'''

class cons: #constants and globals
    light=(-1,-1,100)
    direct=(0,0,1)
    c=100,100
    scale_factor=10
    cmass_xy=(150,40)

    rot_factor=100 # this is z component of ruling vector
    base_vec=(0,0,1)
    start_rot=(0,0)
    rot_axis=(1,0,0)
    angl=0

    position_xy=(400,400)
    cur_position_xy=position_xy
    cursor_start_xy=(0,0)

    vect=[]
    subvect=[]

##################
#angle
def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def length(v):
  return sqrt(dotproduct(v, v))

def angle(v1, v2):
  return acos(dotproduct(v1, v2) / (length(v1) * length(v2)))

def cross(a, b): # cross vector multiplication
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

def rotAng(b_vec,axis,angle): # here quaternion multiplication comes
    r1 = axisangle_to_q(axis,angle)
    v = qv_mult(r1,b_vec)
    return v

## open stl file

print('exctracting geometry from file')
f=open('D://tre1.STL','r')
h=f.readlines()
allal=[]
for line in h:
    line=line.split(' ')
    if 'normal' in line:
        #print ('normal: ',line[-3],line[-2],line[-1][:-1])
        allal.append((line[-3],line[-2],line[-1][:-1]))
    if 'vertex' in line:
        #print ('vertex: ',line[-3],line[-2],line[-1][:-1])
        allal.append((line[-3],line[-2],line[-1][:-1]))
f.close()

k=0
tri=[]
point=[]
for i in allal:

    point.append(i)
    k=k+1
    if k ==4:
        k=0
        tri.append(point)
        point=[]

vect=[]
for tr in tri:
    t=[]
    for p in tr:
        f=[]
        for z in p:
            f.append(float(z))
        t.append(f)
    vect.append(t)

cons.vect=vect

print('stl surface elements: ',len(tri))

###  saving to tri list all normals and pts

light=normalize(cons.light) # vector of light direction
direct=cons.direct ## vector of the model direction
h=800

root = tk.Tk()
canvas = tk.Canvas(
    width = h,
    height = h,
    bg = '#FFF')
print('canvas created')
#cons.cur_position_xy=cons.position_xy# center of coordinates of the model

def draw(canvas):
    rot_axis=cons.rot_axis
    angl=cons.angl
    cmass_xy=cons.cmass_xy
    vect=cons.vect

    canvas.delete("all")
    cons.subvect=[]
    for vec in vect:

        #coordinates and normals
        csf=cons.scale_factor
        vec1=rotAng((vec[1][0]-cmass_xy[0]/csf,vec[1][1]-cmass_xy[1]/csf,vec[1][2]),rot_axis,angl)
        vec2=rotAng((vec[2][0]-cmass_xy[0]/csf,vec[2][1]-cmass_xy[1]/csf,vec[2][2]),rot_axis,angl)
        vec3=rotAng((vec[3][0]-cmass_xy[0]/csf,vec[3][1]-cmass_xy[1]/csf,vec[3][2]),rot_axis,angl)
        
        f_normal=(vec[0][0],vec[0][1],vec[0][2])
        f_normal=normalize(f_normal)
        n_vec=rotAng(f_normal,rot_axis,angl)
        
        z1=(vec1[0]*cons.scale_factor,vec1[1]*cons.scale_factor,vec1[2]*cons.scale_factor)
        z2=(vec2[0]*cons.scale_factor,vec2[1]*cons.scale_factor,vec2[2]*cons.scale_factor)
        z3=(vec3[0]*cons.scale_factor,vec3[1]*cons.scale_factor,vec3[2]*cons.scale_factor)

        bright_factor=sum((a*b) for a, b in zip(light, n_vec)) # scalar vector multiplication
        normal=abs(bright_factor)/1.5
        if bright_factor>0:
            python_green = (int(abs(floor(205*normal+50))),int(abs(floor(205*normal+50))),int(abs(floor(205*normal+50))))
        else:
            python_green =(0,0,0)
        tk_rgb = "#%02x%02x%02x" % python_green

        if n_vec[2]>0:
            canvas.create_polygon((z1[0]+cons.cur_position_xy[0], z1[1]+cons.cur_position_xy[1],
                                    z2[0]+cons.cur_position_xy[0], z2[1]+cons.cur_position_xy[1],
                                    z3[0]+cons.cur_position_xy[0], z3[1]+cons.cur_position_xy[1]), fill=tk_rgb, outline='black')

        vec1=(vec1[0]+cmass_xy[0]/csf,vec1[1]+cmass_xy[1]/csf,vec1[2])
        vec2=(vec2[0]+cmass_xy[0]/csf,vec2[1]+cmass_xy[1]/csf,vec2[2])
        vec3=(vec3[0]+cmass_xy[0]/csf,vec3[1]+cmass_xy[1]/csf,vec3[2])
        cons.subvect.append([n_vec,vec1,vec2,vec3])

def draw_loading(canvas):
    a=canvas.create_text(30,30,font=20,anchor='nw')
    canvas.insert(a,0,'RapTorus v1.16.0224 ; (tap and drag left mouse button)')

def def_rot_center(event):
    x,y=event.x, event.y
    cons.start_rot=x,y
    #draw(canvas)

def new_base_vec(event):
    cons.vect=cons.subvect
    cons.angl=0
    #draw(canvas)

def do_rot_motion(event): # changing direction vector based on the position where cursor is
    x, y = event.x, event.y  
    rot_factor=cons.rot_factor # making direct vector go outta plane to have outta plane rotation
    bv=cons.base_vec
    new_vec=(x-cons.start_rot[0],y-cons.start_rot[1],rot_factor)
    new_vec=normalize(new_vec)
    if bv!=new_vec:
        cons.rot_axis=cross(bv,new_vec)
        cons.angl=angle(bv,new_vec)
    draw(canvas)

def do_scale(event):
    if event.delta>0:
        cons.scale_factor=cons.scale_factor*0.9
    else:
        cons.scale_factor=cons.scale_factor*1.1
    draw(canvas)

def start_position(event):
    x, y = event.x, event.y
    cons.cursor_start_xy=x,y
    #draw(canvas)

def new_position(event):
    cons.position_xy=cons.cur_position_xy
    #draw(canvas)

def do_translate_motion(event):
    x, y = event.x, event.y
    delta_pos=x-cons.cursor_start_xy[0],y-cons.cursor_start_xy[1]
    cons.cur_position_xy=cons.position_xy[0]+delta_pos[0],cons.position_xy[1]+delta_pos[1]
    draw(canvas)

#root.bind('<Motion>', rot_motion)
print('listen to bindings')
root.bind("<B1-Motion>", do_rot_motion)
root.bind("<ButtonPress-1>", def_rot_center)
root.bind("<ButtonRelease-1>", new_base_vec)
root.bind('<MouseWheel>',do_scale)
root.bind('<B3-Motion>',do_translate_motion)
root.bind("<ButtonPress-3>", start_position)
root.bind("<ButtonRelease-3>", new_position)
draw_loading(canvas)
canvas.pack()
root.mainloop()
