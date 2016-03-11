from ElemDescr import *
from collections import Counter
import itertools


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
        e.facesList=[(el[11+0],el[11+1],el[11+2],el[11+3]),
                    (el[11+4],el[11+5],el[11+6],el[11+7]),
                    (el[11+0],el[11+1],el[11+5],el[11+4]),
                    (el[11+1],el[11+2],el[11+6],el[11+5]),
                    (el[11+2],el[11+3],el[11+7],el[11+6]),
                    (el[11+3],el[11+0],el[11+4],el[11+7])] #creating faces set
        els.append(e)
        #print(len(els))
    return els

def cross(a, b): # cross vector multiplication
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

def outerFaces(vertices,elements): # define outer faces
    faces=[]
    for el in elements:
        for face in el.facesList:
            faces.append(face)
    flist=[]
    faceslen=len(faces)
    for i in range(faceslen):
        if len(faces)>0:
            face=faces[0]
            faces=faces[1:]
            strtl=len(faces)
            allFacePermutations=list(itertools.permutations(face))
            #print(allFacePermutations)
            for prmf in allFacePermutations:
                try:
                    faces.remove(prmf)
                except:
                    pass
            if strtl==len(faces):
                flist.append(face)

            ## FLIST -list of (list of vertices numbers of outer faces)
            ## forming vector with normals
    vect=[]
    for f in flist:
        v=[]
        for nodeN in f: 
            nodeObj=findObjectByNum(vertices,nodeN)
            vec=[nodeObj.x,nodeObj.y,nodeObj.z]
            v.append(vec)
        normal=cross(v[0],v[1])
        sumUP=[normal]
        for i in v:
            sumUP.append(i)
        vect.append(sumUP)

    print(len(vect))
            
    return vect        

def mExt(path):
    verticesV,elemG=mshAN(path)
    vertsC=vAss(verticesV)
    elementsC=elAss(vertsC,elemG)
    vect=outerFaces(vertsC,elementsC)

    ## define center of mass << ----- change this
    xvert=[]
    yvert=[]
    zvert=[]
    for v in vect:
        xvert.append((v[1][0]+v[2][0]+v[3][0])/3.0)
        yvert.append((v[1][1]+v[2][1]+v[3][1])/3.0)
        zvert.append((v[1][2]+v[2][2]+v[3][2])/3.0)
    x=sum(xvert)/len(xvert)
    y=sum(yvert)/len(yvert)
    z=sum(zvert)/len(zvert)
    cmass=(x,y,z)

    return vect,cmass



