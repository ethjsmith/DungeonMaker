import random
class Dungeon:
    # the dungeon data structure should hold some info about the dungeon, and then a bunch of room objects
    theme=0
    type=0
    rooms = []
    firstroom=0
    def __init__(self):
        print("ok")
    def generateRoom(self):
        self.firstroom = Room(0)
    def printDungeon(self):
        self.firstroom.printroom()

class Room:
    size_x=0
    size_y=0
    type=0 # this is what kind of room it is, which roughly shows what will be in the room
    others=[] # the rooms that are connected to this one... maybe a tuple or something i d k
    id = 0
    def __init__(self,x,y):
        self.size_x = x
        self.size_y = y
    def __init__(self,depth): # a random room
        self.id = random.randint(1,500)
        print(f"making a room: {self.id}")
        if (depth > 1):
            o = 0
        elif (depth > 0):
            o = random.randint(0,1)
        else:
            o = random.randint(1,2)
        for x in range(o): # ?
            print(f"linking a new room to {self.id}")
            self.others.append(Room(depth+1))
    def printroom(self):
        print(f" room, connected to",end="")
        print(f"{self.others}")
        # for x in self.others:
        #     x.printroom()
# generate a room
def genroom():
    x = random.randint(1,10)
    y = random.randint(1,10)
    room = [[" "] * y] * x
    for x in room:
        for y in x:
            # pick tiles ? rudamentary to just pick randomly ?
            print("X")
    return room

def printroom(room):
    for x in room:
        for y in x:
            print(f"{y},",end="")
        print("")
#printroom(genroom())
d = Dungeon()
d.generateRoom()
d.printDungeon()
