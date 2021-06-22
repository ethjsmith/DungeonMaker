# draw_line.py
import random, math
from PIL import Image,ImageDraw

class Point():
    def __init__(self): # why did I do it like this lol why not just x and y
        self.coords = (0,0)
        self.others = []
    def setCoords(self,x,y):
        self.coords = (x,y)
    def addOther(self,other):
        self.others.append(other)
    def __repr__(self):
        return f"Point at {self.coords}"

def square(p):
    # from one point, creates a list of four points making a square of random size
    # TODO: generate the square around the point, instead of using it as the cornerstone
    size = random.uniform(50,200)
    point2 = Point()
    point2.setCoords(p.coords[0],p.coords[1]+size)
    point3 = Point()
    point3.setCoords(p.coords[0]+size,p.coords[1]+size)
    point4 = Point()
    point4.setCoords(p.coords[0]+size,p.coords[1])
    return [p,point2,point3,point4]

def randomshape(n,start,s):# n is how many points you want, and start is the starting point(midpoint of the room ), s is the scale, or how big roughly
    points = []
    anglerange = (2 * math.pi) / n
    for x in range(n):
        p = (start[0]+math.cos(x*anglerange)*s,start[1]+math.sin(x*anglerange)*s)
        points.append(p)
    return points

# copy of randomshape but this one makes multiple circles :)
# recursive :^) and it is kind of working too... crazy
def randomshapes(numVertices,start,size,result, initialAngle):
        numVertices = random.randint(numVertices-2,numVertices+4) # add some variation... has to be able to become simpler because each later version will use this new value
        size = random.randint(size-2,size+20) # I almost want this one to be a standard deviation
        points = []
        if result != 0:
            len = random.uniform(size-1,size+5)
            s = start[0] + math.cos(initialAngle)*size*4
            v = start[1] + math.sin(initialAngle)*size*4
            start = (s,v)
            print(f"New point at {start}")
        anglerange = (2 * math.pi) / numVertices
        branched = 0
        for x in range(numVertices):
            point = (
                    start[0]+math.cos(x*anglerange+initialAngle-math.pi)*size*random.uniform(.7,1.3),
                    start[1]+math.sin(x*anglerange+initialAngle-math.pi)*size*random.uniform(.7,1.3)
                    ) # will this run?
            if branched <2 and random.randint(0,4)<1 and result < 2:
                print("deeper")
                branched += 1
                points.extend(randomshapes(numVertices,start,size,result+1,(x+1)*anglerange+initialAngle-math.pi))
            points.append(point)
        #result.extend(points)
        return points



def connectshapes(shape, shape2): # takes two shapes... maybe connects them ?
    # find the points that are nearest each other
    print("I dont think this is the best way to do it ")

def distance(p1,p2):
    d = math.sqrt(((p1[0] - p2[0])**2) + ((p1[1]-p2[1])**2))
    return d



img = Image.new('RGB', (1000, 1000), color = 'white')
#img.save('pil_red.png')
draw = ImageDraw.Draw(img)
#draw.line((100,200,150,300),fill=128)
stuff = {}
for x in range(1,25):
    a = Point()
    a.setCoords(random.randint(0,1000),random.randint(0,1000))
    stuff[a.coords] = a

pz = Point()
pz.setCoords(random.randint(0,1000),random.randint(0,1000))

q = square(pz)
#print(q)
# I think we only need two points for this square:)
#draw.rectangle((q[0].coords[0],q[0].coords[1],q[2].coords[0],q[2].coords[1]),fill=128)
# rpk = randomshape(15,(500,500),50)
# rpk2 = randomshape(15,(600,600),25)
# print(rpk)
# for x in rpk2:
#     rpk.append(x)
q = randomshapes(10,(500,500),30,-1,1)
draw.polygon(q,fill=128, outline ="blue")
img.show()
