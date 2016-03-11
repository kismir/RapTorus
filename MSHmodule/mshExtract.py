from ElemDescr import *
from collections import Counter

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def mshAN(path):
    f=open(path,'r')
    h=f.readlines()
    vertices=[]
    elements=[]
    for i in h:
        lst=i.split(' ')
        nlst=[]
        for u in lst:
            if is_number(u):
                nlst.append(float(u))
        if len(nlst)>2 and len(nlst)<10:
            vertices.append(nlst)
        if len(nlst)>2 and len(nlst)>10:
            elements.append(nlst)

    return vertices,elements

def vAss(vertices):
    verts=[]
    for vi in vertices:
        v=vertex()
        v.number=vi[0]
        v.x=vi[1]
        v.y=vi[2]
        v.z=vi[3]
        verts.append(v)
    return verts
        
def findObjectByNum(theList,number):
    obj=next((x for x in theList if x.number == number), None)
    return obj

def sameLists(s, t):
    return Counter(s) == Counter(t)

def elAss(verts,elements):
    els=[]
    for el in elements:
        e=element()
        e.number=el[10]
        e.vertexList=[]
        #my_dict = {i:el[11:].count(i) for i in el[11:]}
        #print(len(my_dict ))
        for item in el[11:]:
            vertexOBJ=findObjectByNum(verts,item)
            e.vertexList.append(vertexOBJ)
        e.facesList=[sorted([el[11+0],el[11+1],el[11+2],el[11+3]]),
                             sorted([el[11+4],el[11+5],el[11+6],el[11+7]]),
                             sorted([el[11+0],el[11+1],el[11+5],el[11+4]]),
                             sorted([el[11+1],el[11+2],el[11+6],el[11+5]]),
                             sorted([el[11+2],el[11+3],el[11+7],el[11+6]]),
                             sorted([el[11+3],el[11+0],el[11+4],el[11+7]])] #creating faces set
        els.append(e)
        print(len(els))
    return els

def outerFaces(elements): # define outer faces
    faces=[]
    for el in elements:
        for face in el.facesList:
            faces.append(face)
    print(len(faces))
    flist=[]
    faceslen=len(faces)
    for i in range(faceslen):
        face=faces[0]

        print(len(faces))
        Removeind=[]
        faces=faces[1:]
        strtl=len(faces)
        try:
            faces.remove(face)
        except:
            pass
        if strtl==len(faces):
            flist.append(face)

            

    return flist        

path='D:/el_ex.txt'
vertices,elements=mshAN(path)
verts=vAss(vertices)
elements=elAss(verts,elements)
for i in range(50,70):
    a=findObjectByNum(elements,i)
fl=outerFaces(elements)
print(fl)
    #print(a.vertexList)

