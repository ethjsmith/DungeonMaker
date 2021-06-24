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

    numVertices = random.randint(numVertices-2,numVertices+4) # add some variation... has to be able to become simpler because each later version will use this new value
    size = random.randint(size-2,size+20) # I almost want this one to be a standard deviation
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

def midpoint(shape):
    # calculates a shape's midpoint lol
    total_x = 0
    total_y = 0
    for point in shape:
        total_x += point[0]
        total_y += point[1]
    total_x = total_x/len(shape)
    total_y = total_y/len(shape)
    return (total_x,total_y)

x_coord = 5000
y_coord = 5000
img = Image.new('RGB', (x_coord, y_coord), color = 'white')
#img.save('pil_red.png')
draw = ImageDraw.Draw(img)

#q = randomshapes(12,(x_coord/2,y_coord/2),x_coord//15,0,1)
#draw.polygon(q,fill=128, outline ="blue")
shapes = []
for x in range(10): # makes 10 random "rooms"
    q = randomshapes(12,(random.randint(500,x_coord-500),random.randint(500,y_coord-500)),x_coord//13,0,1)
    shapes.append(q)
    draw.polygon(q,fill=128, outline ="blue")
print(shapes)
# links the rooms together
for shape in shapes:
    shape2 = random.randint(0,len(shapes)-1)
    if shape == shapes[shape2]:
        if shape2 == 0: # this can break if the room size is 1, which ... shouldn't happen
            shape2 += 1
        else:
            shape2 -= 1
    # a better way would be to take two edges from each and connect them that way ?
    m1 = midpoint(shape)
    m2 = midpoint(shapes[shape2])
    m1_1 = m1[0]+random.randint(100,250),m1[1]+random.randint(100,250)
    m2_1 = m2[0]+random.randint(100,250),m2[1]+random.randint(100,250)
    c = m1,m1_1,m2_1,m2 # this order matters
    draw.polygon(c,fill=128)
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
