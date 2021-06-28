import random
class Dungeon:
    # the dungeon data structure should hold some info about the dungeon, and then a bunch of room objects
    # hmm the fact that I was making class variables explains a lot acutally lol im so dumb
    def __init__(self):
        self.theme=0 # TODO implement these for themeing a room/dungeon
        self.type=0
        self.rooms = []
        self.firstroom=0
        self.rooms.append(Room())
    def makeDungeon(self,n):
        x = 0
        while x < n:
            a = random.randint(0,len(self.rooms)-1)
            r = Room()
            self.rooms[a].addchild(r)
            self.rooms.append(r)
            print(f"adding new {r} and adding it to index {a}")
            x+=1
    def printDungeon(self):
        print(self.rooms)
        for room in self.rooms:
            room.printRoom()

# terrain types:
# 0 passable terrain?
# 1 parent room link
# 2 child room link

#TODO more

class Room:
    def __init__(self):
        self.children = []
        self.id = random.randint(1,100) # placeholder mostly for helping with debugging by giving rooms an identifier
        self.x = random.randint(3,8)
        self.y = random.randint(3,8)
        self.grid = [ [0] * self.x for i in range(self.y)]
        tmp = enumerateOutside(self.grid)
        self.grid = tmp[0]
        # place the entry and exit points
        exit = False
        placed =0
        for x,a in enumerate(self.grid):
            for y,b in enumerate(a):
                if self.grid[x][y] == -1: # this doesn't quite work
                    place = random.randint(0,tmp[1])
                    if place <= len(self.children)+placed:
                        placed += 1
                        if not exit:
                            self.grid[x][y] = 1
                            exit = True
                        else:
                            self.grid[x][y] = 2


    def __str__(self):
        return f"Room:{self.id}"
    def __repr__(self):
        return self.__str__()
    def addchild(self,r):
        self.children.append(r)
    def printRoom(self):
        print(f" room: {self.id}, leads to: ",end="")
        print(self.children)
        print("")
        print(self.grid)
def enumerateOutside(grid):
    count = 0
    for x,axis in enumerate(grid):
        for y, axiis in enumerate(axis):
            print(f"{x},{y}")
            if x==0 or y==0 or x==len(grid)-1 or y==len(axis)-1:
                print("matches")
                grid[x][y] = -1 # placeholder
                print(grid)
                count +=1
    print(grid)
    return (grid,count)
            # this is a valid position for a boundary


d = Dungeon()
d.makeDungeon(5)
d.printDungeon()
