import sqlite3
from ElemDescr import *
from collections import Counter
import itertools
from constants import constants
import time

def PdbInfo(path):
    """Get all table names"""

    con = sqlite3.connect(path)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    Tlistoflists=cursor.fetchall()
    Tlist=[]
    for lst in Tlistoflists:
        Tlist.append(lst[0])

    for i in Tlist:

        cursor.execute('PRAGMA TABLE_INFO({})'.format(i))
        info = cursor.fetchall()

        print('\n'+str(i))
        print("\nColumn Info:\nID, Name, Type, NotNull, DefaultVal, PrimaryKey")
        for col in info:
            print(col)
    con.close()
            

def getPdbData(path):
    """Get all table names"""

    con = sqlite3.connect(path)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    Tlistoflists=cursor.fetchall()
    Tlist=[]
    for lst in Tlistoflists:
        Tlist.append(lst[0])

    data={}
    for i in Tlist:
        cursor.execute('SELECT * FROM {0}'.format(i))
        data[i]=cursor.fetchall()

    con.close()

    return data

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def vAss(data):
    nodes=data['Nodes']
    verts=[]
    for node in nodes:
        v=vertex()
        v.number=node[0]
        v.x=node[1]
        v.y=node[2]
        v.z=node[3]
        verts.append(v)
    return verts
        
def findObjectByNum(theList,number):
    obj=next((x for x in theList if x.number == number), None)
    return obj

def cross(a, b): # cross vector multiplication
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

def vSubtraction(a, b): # 
    c=[a[0] - b[0],
         a[1] - b[1],
         a[2]- b[2]]
    return c

def getFaceNodes(faceN,data):
    FaceNodes=data['FaceNodes']
    FN=[]
    for line in FaceNodes:
        if line[0]==faceN:
            FN.append(line[1])

    return FN    
    

def outerFaces(vertices,data): # define outer faces
    faces=data['Faces']
    OuterFaces=[]
    for f in faces:
        if f[2]==0:
            OuterFaces.append(f[0])
    vect=[]
    for faceN in OuterFaces:
        face=getFaceNodes(faceN,data)
        v=[]
        for nodeN in face: 
            nodeObj=findObjectByNum(vertices,nodeN)
            vec=[nodeObj.x,nodeObj.y,nodeObj.z]
            v.append(vec)
        v1=vSubtraction(v[1],v[0])
        v2=vSubtraction(v[2],v[1])
        normal=cross(v1,v2)
        sumUP=[normal]
        for i in v:
            sumUP.append(i)
        vect.append(sumUP)

    print(len(vect))

    return vect        

def mExt(path):
    data=getPdbData(path)
    vertsC=vAss(data)
    vect=outerFaces(vertsC,data)

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
    
    cons=constants()
    print('constants successfully initialized')
    cons.vect=vect
    cons.cmass_xyz=cmass

    return cons





