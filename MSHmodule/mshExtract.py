from ElemDescr import *

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

def edgeAss(verts,elements):
    edges=[]
    g=0
    for i,el in enumerate(elements):
        for j,item in enumerate(el[11:-1]):
            g=g+1
            ed=edge()
            ed.number=g
            ed.edgeList=[]
            vertexOBJ=findObjectByNum(verts,item)
            e.vertexList.append(vertexOBJ)
        edges.append(e)
    return edges

def elAss(verts,elements):
    els=[]
    for el in elements:
        e=element()
        e.number=el[10]
        e.vertexList=[]
        for item in el[11:]:
            vertexOBJ=findObjectByNum(verts,item)
            e.vertexList.append(vertexOBJ)
        els.append(e)
    return els

path='D:/el_ex.txt'
vertices,elements=mshAN(path)
verts=vAss(vertices)
elements=elAss(verts,elements)
for i in range(1,20):
    a=findObjectByNum(elements,i)
    print(a.vertexList)

