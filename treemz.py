# makes a node that connects to other nodes in a tree shape, and then gives each one a coordinate ?
# this probably isn't actually a tree but I was kind of thinking about a tree when I started it
import random

# it's a coordinate, and links to other coordinates
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


class Point():
    def __init__(self):
        self.coords = (0,0)
        self.others = []
    def setCoords(self,x,y):
        self.coords = (x,y)
    def addOther(self,other):
        self.others.append(other)
    def __repr__(self):
        return f"Point at {self.coords}"

stuff = {}
for x in range(1,25):
    a = Point()
    a.setCoords(random.randint(0,10),random.randint(0,10))
    stuff[a.coords] = a

def squarify(tup):
    xq = []
    size = random.uniform(.5,2)
    xq.append((tup[0],tup[1]))
    xq.append((tup[0],tup[1]+size))
    xq.append((tup[0]+size,tup[1]+size))
    xq.append((tup[0]+size,tup[1]))
    xq.append((tup[0],tup[1]))
    z = (tup[0]+size/2,tup[1]+size/2)
    return (xq,z)

print(stuff)

# for item in stuff:
#     xx.append(stuff[item].coords[0])
#     yy.append(stuff[item].coords[1])
midpoints = []
for item in stuff:
    xx = []
    yy = []
    q = squarify(stuff[item].coords)
    midpoints.append(q[1])
    for z in q[0]:
        xx.append(z[0])
        yy.append(z[1])
    plt.plot(xx,yy)

xx=[]
yy=[]
for p in midpoints: # this part draws connections from each midpoint.
# for a different type it would have to be a different way of being drawn. Even this one isn't that good ... 
    xx.append(p[0])
    yy.append(p[1])
plt.plot(xx,yy)
# xpoints = np.array(xx)
# ypoints = np.array(yy)
#
# plt.plot(xpoints,ypoints,'o')
plt.grid(linewidth="1.0")
plt.show()
