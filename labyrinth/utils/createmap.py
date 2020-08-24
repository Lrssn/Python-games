from random import randrange, random
import numpy
def createMap(sizeX, sizeY):
    map = numpy.zeros((sizeX, sizeY))
    map = cellular_automata(sizeX, sizeY)
    endset = False
    while endset == False:
        endx = randrange(2,sizeX-1)
        endy = randrange(4,sizeY-2)
        if map[endx][endy] == 0:
            endset = True
            break

    startset = False
    while startset == False:    
        startx = randrange(2,sizeX - 2)
        starty = randrange(4,sizeY - 2)
        if startx == endx and starty == endy:
            startx = startx+1
        if map[startx][starty] == 0:
            startset = True
            break


    a = []
    b = ""
    for y in range(sizeY):
        for x in range(sizeX):
            if x == endx and y == endy:
                b=b+"E"
            elif x == startx and y == starty:
                b=b+"S"
            elif x == 0:
                b = b + "W"
            elif x == sizeX-1:
                b = b + "W"
            elif y == 0:
                b = b + "W"
            elif y == sizeY-1:
                b = b + "W"
            elif map[x][y] == 1:
                b = b + "W"
            else:
                b = b + "G"
        a.append(b)
        b = ""
    return a

def cellular_automata(sizeX, sizeY):
    simsteps = 5
    map = initmap(sizeX, sizeY)
    i = 1
    while i < simsteps:
        newmap = simulation_step(map, sizeX, sizeY)
        map = newmap
        i = i + 1

    return map

def simulation_step(map, sizeX, sizeY):
    kill_count = 2
    birth_count = 4
    newmap = numpy.zeros((sizeX, sizeY))
    for i in range(2, sizeX-1):
        for j in range(2, sizeY-1):
            c = count_neighbours(map, i, j)
            if map[i][j]==1:
                if c < kill_count:
                    newmap[i][j]=0
                else:
                    newmap[i][j]=1
            else:
                if c > birth_count:
                    newmap[i][j]=1
                else:
                    newmap[i][j]=0
                    

    return newmap 


def count_neighbours(map, x, y):
    count = 0
    for i in range(-1, 1):
        for j in range(-1, 1):
            if i == 0 and j == 0:
                count = count + 0
            elif map[x+i][y+j]==1:
                count = count + 1
    return count

def initmap(sizex, sizey):
    alive_chance = 0.2
    map = numpy.zeros((sizex, sizey))
    for y in range(0, sizey):
        for x in range(0, sizex):
            if random() > alive_chance:
                map[x][y] = 1

    return map