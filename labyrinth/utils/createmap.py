from random import randrange, random
def createMap(sizeX, sizeY):
    a = []
    b = ""
    endx = randrange(0,sizeX)
    endy = randrange(0,sizeY)
    
    for y in range(sizeY):
        for x in range(sizeX):
            if x == endx and y == endy:
                b=b+"E"           
            elif x == 0:
                b = b + "W"
            elif x == sizeX-1:
                b = b + "W"
            elif y == 0:
                b = b + "W"
            elif y == sizeY-1:
                b = b + "W"
            elif random() > 0.7:
                b = b + "W" #TODO: better algorithm
            else:
                b = b + " "
        a.append(b)
        b = ""
    return a