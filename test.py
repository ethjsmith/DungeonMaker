# draw_line.py

# this version started from single polygon test, but instead now just placing many polygons, and then connecting them

import random, math
from PIL import Image,ImageDraw

# recursive :^) and it is kind of working too... crazy
def randomshapes(numVertices,start,size,result, initialAngle,):
    '''
    numVertices is how many vertices each room should have... 10-20 seems good
    Start is a tuple of coordinates where the room should start
    size is how big the room should be
    result is misnamed, should be room count basically, the upper limit of how many rooms you can have in your dungeon
    initialAngle is used to determine where to start drawing new circles, and ... stuff idk  lol
    midpoints is a list of all places where there is already a room

    '''
    # Now with a randomized starting point


    #midpoints.append(start) # create a list of the midpoint of each room, and disallow placing new rooms too close to any existing room...

    numVertices = random.randint(numVertices-3,numVertices+7) # add some variation... has to be able to become simpler because each later version will use this new value
    size = random.randint(size-10,size+40) # I almost want this one to be a standard deviation
    points = []
    anglerange = (2 * math.pi) / numVertices
    branched = 0
    for x in range(numVertices):
        point = (
                start[0]+math.cos(x*anglerange+initialAngle-math.pi)*size*random.uniform(.7,1.3),
                start[1]+math.sin(x*anglerange+initialAngle-math.pi)*size*random.uniform(.7,1.3)
                ) # will this run?
        points.append(point)
    #result.extend(points)
    return points

def contained (point,points): # returns true if the point is close to any other points
    for p in points:
        if distance(point,p) < 570: # this should be configurable ?
            print(f" {p} is too close to {point}")
            return True
    return False
def distance(p1,p2): # haven't actually tested this lol
    d = math.sqrt(((p1[0] - p2[0])**2) + ((p1[1]-p2[1])**2))
    return d


def slope(p1,p2): # slope of two points, for generating hallways I think
    return (p2[1]-p1[1])/(p2[0]/p1[0])
def perpSlope(sl):
    return -1* (1/sl)

def midpoint(shape): # calculates a shape's midpoint lol
    total_x = 0
    total_y = 0
    for point in shape:
        total_x += point[0]
        total_y += point[1]
    total_x = total_x/len(shape)
    total_y = total_y/len(shape)
    return (total_x,total_y)

def nearest(shape,targ): # find the point in a shape that is nearest to a target point
    nr = (0,0)
    dist = 999999999
    for point in shape:
        if distance(point,targ) < dist:
            nr = point
            dist = distance(point,targ)
    return nr

x_coord = 5000
y_coord = 5000
img = Image.new('RGB', (x_coord, y_coord), color = 'white')
#img.save('pil_red.png')
draw = ImageDraw.Draw(img)

#q = randomshapes(12,(x_coord/2,y_coord/2),x_coord//15,0,1)
#draw.polygon(q,fill=128, outline ="blue")
shapes = []
q = randomshapes(12,(x_coord/2,y_coord/2),x_coord//13,0,1) # first shape, always in center
shapes.append(q)
draw.polygon(q,fill=128,outline="blue")
for x in range(6): # makes 10 random "rooms"
    #TODO make it so rooms can't overlap, by checking where rooms are already placed,
    # also put rooms closer together when they're far apart, by migrating them towards the exact middle :)  until they hit that distance to another room?
    # generate the coordinates first
    validspot = False
    co = random.randint(300,x_coord-300),random.randint(300,y_coord-300)
    # test if the point is good
    while not validspot:
        for s in shapes:
            if distance(co,midpoint(s)) < 400: # tune
                co = random.randint(300,x_coord-300),random.randint(300,y_coord-300)
            else:
                print("good ")
                validspot = True
                break
    # valid spot is found
    q = randomshapes(12,(random.randint(300,x_coord-300),random.randint(300,y_coord-300)),x_coord//13,0,1)
    shapes.append(q)
    draw.polygon(q,fill=128, outline ="blue")
print(shapes)
# links the rooms together

# TODO link rooms based on distance from each other, rather than randomly
for shape in shapes:
    shape2 = shapes[random.randint(0,len(shapes)-1)]
    # if shape == shape2:
    #     if shape2 == 0: # this can break if the room size is 1, which ... shouldn't happen
    #         shape2 += 1
    #     else:
    #         shape2 -= 1
    while shape == shape2:
        shape2 = shapes[random.randint(0,len(shapes)-1)]

    # different approach: find the points that are nearest each other, and link between them
    p1 = nearest(shape,midpoint(shape2))
    nxt = False
    for point in shape:
        if nxt:
            p1a = point
            break
        if point == p1:
            nxt = True


    p2 = nearest(shape2,midpoint(shape))
    nxt = False
    for point in shape2[::-1]:
        if nxt:
            p2a = point
            break
        if point == p2:
            nxt = True

    c = p1a,p1,p2,p2a
    draw.polygon(c,fill=253)

    # different way to connect rooms by drawing randomly from the midpoints of different rooms
    # m1 = midpoint(shape)
    # m2 = midpoint(shape2)
    # m1_1 = m1[0]+random.randint(100,250),m1[1]+random.randint(100,250)
    # m2_1 = m2[0]+random.randint(100,250),m2[1]+random.randint(100,250)
    # # TODO add a system that adds points randomly in the hallways, allowing them to curve around a bit
    # c = m1,m1_1,m2_1,m2 # this order matters
    # draw.polygon(c,fill=128)
# draw a grid
xx = 0
step = x_coord/100
while xx < x_coord:
    draw.line([(xx,0),(xx,y_coord)],fill=200)
    xx = xx + step
xx = 0
while xx < y_coord:
    draw.line([(0,xx),(x_coord,xx)],fill=200)
    xx = xx + step

img.show()
