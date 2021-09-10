# draw_line.py

# this version started from single polygon test, but instead now just placing many polygons, and then connecting them

import random, math, conf
from PIL import Image,ImageDraw


def randomshapes(numVertices,start,size, initialAngle):
    '''
    numVertices is roughly how many vertices each room should have... 10-20 seems good
    Start is a tuple of coordinates where the room should start
    size is roughly how big the room should be
    initialAngle is used to determine where to start drawing new circles, and ... stuff idk  lol
    '''
    # Now with a randomized starting point
    numVertices = random.randint(numVertices-5,numVertices+7) # add some variation between each room
    size = random.randint(size-10,size+40) # Should this follow a standard distribution?
    points = []
    anglerange = (2 * math.pi) / numVertices
    branched = 0
    for x in range(numVertices):
        point = (
                start[0]+math.cos(x*anglerange+initialAngle-math.pi)*size*random.uniform(.7,1.3),
                start[1]+math.sin(x*anglerange+initialAngle-math.pi)*size*random.uniform(.7,1.3)
                )
        points.append(point)
    return points

def distance(p1,p2): # returns the distance between two points ( which are assumed to be tuples, but really a list would work too... which is bad )
    d = math.sqrt(((p1[0] - p2[0])**2) + ((p1[1]-p2[1])**2))
    return d

def intr(A,B,C): # component of the intersects function # using some fancy stackoverflow math 
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0]) # true if intersect
def intersect(A,B,C,D):# takes line a ,b and c,d
    return intr(A,C,D) != intr(B,C,D) and intr(A,B,C) != intr(A,B,D)

def midpoint(shape): # calculates a shape's midpoint for use in measuring compared against other shapes
    total_x = 0
    total_y = 0
    for point in shape:
        total_x += point[0]
        total_y += point[1]
    total_x = total_x/len(shape)+1
    total_y = total_y/len(shape)+1
    return (total_x,total_y)

def nearest(shape,targ):
    '''
    find the point in a shape that is nearest to a target point
    shape: is the shape which you are drawing points from
    targ: the target coordinate point that you're finding the nearest point to
    '''
    nr = (0,0)
    dist = 999999999
    for point in shape:
        #print(f"trying {point} ")
        if distance(point,targ) < dist:
        #    print(f"{point} is closer, replacing {nr} with {point}")
            nr = point
            dist = distance(point,targ)
    #print(f"returning {nr}")
    return nr
def link( s1,s2): # generates the coordinates to link two rooms
    # the ordering, ( or naming ) is confusing, but the order if you visualize the points as a sqaure would be first-> second-> forth-> third
    firstTargetPoint = nearest(s1,midpoint(s2))
    #print(f" got {firstTargetPoint} from nearest")
    secondTargetPoint = nearest(s2,firstTargetPoint)
    print(s1)
    print(f"POINT: {firstTargetPoint}")
    q1 = adjacentPoints(s1,firstTargetPoint)
    q2 = adjacentPoints(s2,secondTargetPoint)
    thirdTargetPoint = nearest(q1,secondTargetPoint)
    fourthTargetPoint = nearest(q2,thirdTargetPoint)
    if intersect(firstTargetPoint,secondTargetPoint,fourthTargetPoint,thirdTargetPoint): # TODO test the order of the points, to see if this actually works?
        return (firstTargetPoint,fourthTargetPoint,secondTargetPoint,thirdTargetPoint)
    else:
        return (firstTargetPoint,secondTargetPoint,fourthTargetPoint,thirdTargetPoint)
def adjacentPoints(shape,point):
    '''
    this might be genuinely bad :)
    shape is a list of points
    point is a point in there
    '''
    print(f"SHAPE:{shape}")
    print(f"POINT:{point}")
    ind = shape.index(point)
    lower = ind - 1
    if lower < 0:
        lower = len(shape)-1
    upper = ind + 1
    if upper > len(shape)-1:
        upper = 0
    return (shape[lower],shape[upper])

x_coord = 5000 # these could be set by a config or something
y_coord = 5000
img = Image.new('RGB', (x_coord, y_coord), color = 'white')
draw = ImageDraw.Draw(img,"RGBA")
shapes = []
q = randomshapes(12,(x_coord/2,y_coord/2),x_coord//13,1) # first shape, always in center
shapes.append(q)
draw.polygon(q,fill=(128,0,0,125),outline="blue")
for x in range(9): # makes {x} random "rooms" change the number to increase or decrease the number of generated rooms
    valid = False
    while not valid: # checks if a room is in a valid place ( not overlapping )
        co = random.randint(300,x_coord-300),random.randint(300,y_coord-300)
        valid = True
        for s in shapes:
            if distance(co,midpoint(s)) < (x_coord//13)*2: # distance is based on the x coordinate of the canvas size
                valid = False
                break

    q = randomshapes(12,co,x_coord//13,1)
    shapes.append(q)
    draw.ellipse([(co[0]-10,co[1]-10),(co[0]+10,co[1]+10)],fill="black") # draw a dot at the midpoint of the room, for debugging
    draw.polygon(q,fill=(random.randint(1,100),random.randint(1,250),random.randint(1,250),150), outline ="blue")

# links rooms together, based on distance
for shape in shapes:
    shape2 = []
    dist = 999999999
    for s in shapes: # finds the closest shape
        nd = distance(midpoint(shape),midpoint(s))
        if nd > 50 and nd < dist:
            shape2 = s
            dist = nd
    #print(f"{shape},,,{shape2}")
    c= link(shape,shape2)
    #print(f"C:{c}")
    draw.polygon(c,fill=(250,0,0,125))


    # This section generates paths by picking two near points on circles and links them
    # p1 = nearest(shape,midpoint(shape2))
    # nxt = False
    # for point in shape:
    #     if nxt:
    #         p1a = point
    #         break
    #     if point == p1:
    #         nxt = True
    # p2 = nearest(shape2,midpoint(shape))
    # nxt = False
    # for point in shape2[::-1]: # goes the reverse way as point 1, in an attempt to reduce hourglass shaped paths
    #     if nxt:
    #         p2a = point
    #         break
    #     if point == p2:
    #         nxt = True
    #c = (p1a,p1,p2,p2a)

# TODO add more links between rooms, to ensure that the entire maps is connected
# TODO fix rooms that are close to each other connecting to each other
# TODO make hallways more variable
# TODO square rooms/sections
# TODO just more room shapes in general

# draw a grid over the room
xx = 0
step = x_coord/100
while xx < x_coord:
    draw.line([(xx,0),(xx,y_coord)],fill=(200,0,0,125))
    xx = xx + step
xx = 0
while xx < y_coord:
    draw.line([(0,xx),(x_coord,xx)],fill=(200,0,0,125))
    xx = xx + step

img.show()
