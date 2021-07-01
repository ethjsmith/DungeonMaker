# draw_line.py

# this version started from single polygon test, but instead now just placing many polygons, and then connecting them

import random, math
from PIL import Image,ImageDraw

# No longer recursive, because honestly, what the F was I thinking with that
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

def distance(p1,p2): # returns the distance between two points ( which are assumed to be tuples, but really a list would work too... which is bad )
    d = math.sqrt(((p1[0] - p2[0])**2) + ((p1[1]-p2[1])**2))
    return d


def slope(p1,p2): # slope of two points, for generating hallways I think
    return (p2[1]-p1[1])/(p2[0]/p1[0])
def perpSlope(sl):# make a slope into a perpendicular slope... unused
    return -1* (1/sl)

def midpoint(shape): # calculates a shape's midpoint for use in measuring compared against other shapes
    total_x = 0
    total_y = 0
    for point in shape:
        total_x += point[0]
        total_y += point[1]
    total_x = total_x/len(shape)+1
    total_y = total_y/len(shape)+1
    return (total_x,total_y)

def nearest(shape,targ): # find the point in a shape that is nearest to a target point
    nr = (0,0)
    dist = 999999999
    for point in shape:
        if distance(point,targ) < dist:
            nr = point
            dist = distance(point,targ)
    return nr


x_coord = 5000 # these could be set my a config or something
y_coord = 5000
img = Image.new('RGB', (x_coord, y_coord), color = 'white')
draw = ImageDraw.Draw(img,"RGBA")
shapes = []
q = randomshapes(12,(x_coord/2,y_coord/2),x_coord//13,0,1) # first shape, always in center
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

    q = randomshapes(12,co,x_coord//13,0,1)
    shapes.append(q)
    draw.ellipse([(co[0]-10,co[1]-10),(co[0]+10,co[1]+10)],fill="black") # draw a dot at the midpoint of the room, for debugging
    draw.polygon(q,fill=(random.randint(1,100),random.randint(1,250),random.randint(1,250),150), outline ="blue")
print(shapes)
# links the rooms together

# links rooms based on distance, instead of randomly, but that means that often rooms link to each other instead of random ? TODO add more links
for shape in shapes:
    shape2 = []
    dist = 999999999
    for s in shapes:
        nd = distance(midpoint(shape),midpoint(s))
        if nd > 50 and nd < dist:
            shape2 = s
            dist = nd

    # This section generates paths by picking two near points on circles and links them
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
    for point in shape2[::-1]: # goes the reverse way as point 1, in an attempt to reduce hourglass shaped paths
        if nxt:
            p2a = point
            break
        if point == p2:
            nxt = True
    c = (p1a,p1,p2,p2a)
    #print(f"C:{c}")
    draw.polygon(c,fill=(250,0,0,125))
# TODO add more links between rooms, to ensure that the entire maps is connected
# TODO fix rooms that are close to each other connecting to each other
# TODO make hallways more variable 


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
