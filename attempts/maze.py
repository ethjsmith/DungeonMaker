#maze.py
import random
from math import e
class Maze:
    # generates a dungeon by making a maze, and then adding some rooms... v3 of dungeon generator
    def __init__(self,y,x):
        self.xlen = x
        self.ylen = y
        self.field = []
        self.front = []
        for yy in range(y):
            row = []
            for xx in range(x):
                row.append("?")
            self.field.append(row)
        startingx = random.randint(0,self.xlen-1)
        startingy = random.randint(0,self.ylen-1)
        self.carve(startingx,startingy)

        brate = 0
        while (len(self.front)): # while we have options
            p = random.random()
            p = p**(e**-brate)
            c = self.front[int(p*len(self.front))]
            if self.check(*c):
                self.carve(*c)
            else:
                self.harden(*c)
            self.front.remove(c)

            for y in range(self.ylen):
                for x in range(self.xlen):
                    if self.field[y][x] == "?":
                        self.field[y][x] == "#"
        self.printme()
    def carve(self,y,x): # make the cell into a path
        xt = []
        self.field[y][x] == "." # set our position to a path
        # now check adjacent tiles to set them up to possibly be walls or more paths
        if x > 0:
            if self.field[y][x-1] == "?":
                self.field[y][x-1] = ","
                xt.append((y,x-1))
        if x < self.xlen - 1:
            if self.field[y][x+1] == "?":
                self.field[y][x+1] = ","
                xt.append((y,x+1))
        if y > 0:
            if self.field[y-1][x] == "?":
                self.field[y-1][x] = ","
                xt.append((y-1,x))
        if y < self.ylen-1:
            if self.field[y+1][x] == "?":
                self.field[y+1][x] = ","
                xt.append((y+1,x))
        random.shuffle(xt)
        self.front.extend(xt)

    def harden(self,y,x): # make a spot into a wall
        self.field[y][x] = "#"
    def printme(self):
        char = " "
        for y in range(self.ylen):
            for x in range(self.xlen):
                char += self.field[y][x]
            print(char)
    def check(self,y,x):# checks if this cell can be a path
        edges = 0
        if x > 0: # I think there's a better way to do this, where you put the outside indices in a list and then step through it... idk if it's better, but it looks cleaner than a bunch of IF statements LOOL
            if self.field[y][x-1] == ".":
                edges += 1
        if x < self.xlen-1:
            if self.field[y][x+1] == ".":
                edges += 2
        if y > 0:
            if self.field[y-1][x] == ".":
                edges += 4
        if y < self.ylen-1:
            if self.field[y+1][x] == ".":
                edges += 8
        if edges == 1:
            if x < self.xlen-1:
                if y > 0:
                    if self.field[y-1][x+1] == '.':
                        return False
                if y < self.ylen-1:
                    if self.field[y+1][x+1] == '.':
                        return False
            return True
        elif edges == 2:
            if x > 0:
                if y > 0:
                    if self.field[y-1][x-1] == '.':
                        return False
                if y < self.ylen-1:
                    if self.field[y+1][x-1] == '.':
                        return False
            return True
        elif edges == 4:
            if y < self.ylen-1:
                if x > 0:
                    if self.field[y+1][x-1] == '.':
                        return False
                if x < self.xlen-1:
                    if self.field[y+1][x+1] == '.':
                        return False
            return True
        elif edges == 8:
            if y > 0:
                if x > 0:
                    if self.field[y-1][x-1] == '.':
                        return False
                if x < self.xlen-1:
                    if self.field[y-1][x+1] == '.':
                        return False
                else: # diagnol stuff
                    if [1,2,4,8].count(edges): # what ?
                        return True
                    return False
r = Maze(10,10)
