import random
import noise
import numpy
import imageio

def createmap(sizex, sizey, scale= 200, octaves=6, persistence=0.5, lacunarity=2.0, thresholds = [0.5]):
    img = numpy.zeros((sizey, sizex))
    for i in range(sizey):
        for j in range(sizex):
            img[i][j] = noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=2048, 
                                    repeaty=2048, 
                                    base=1)
    set_image = numpy.zeros(img.shape)
    for i in range(sizey):
        for j in range(sizex):
            for k in range(len(thresholds)):
                if img[i][j] <= thresholds[k]:
                    set_image[i][j] = k
                    break

    return set_image

def cellular_automata(sizex, sizey, live_chance = 0.4, nrofsimsteps = 7, starvationLimit = 4, overpopLimit = 6, birthNumber = 4):
    shape = (sizey, sizex)
    dead = 0
    live = 1
    

    new_map = numpy.ones(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            choice = random.uniform(0, 1)
            new_map[i][j] = dead if choice < live_chance else live

    temp_map = numpy.ones(shape)

    for simstep in range(nrofsimsteps):
        for i in range(shape[0]):
            for j in range(shape[1]):
                farmtiles = nr_of_farmtiles(new_map, j, i, shape)
                if new_map[i][j] == live:
                    if farmtiles < starvationLimit:
                        temp_map[i][j] = dead
                    if farmtiles > overpopLimit:
                        temp_map[i][j] = dead
                else:
                    if farmtiles == birthNumber:
                        temp_map[i][j] = live
        new_map = temp_map

    return new_map

def nr_of_farmtiles(old_map, x, y, shape):
    farmtiles = 0
    if y > 0 and x > 0:
        farmtiles += old_map[y-1][x-1]
    if y > 0:
        farmtiles += old_map[y-1][x]
    if y > 0 and x < shape[1]-1:
        farmtiles += old_map[y-1][x+1]
    if x > 0:
        farmtiles += old_map[y][x-1]
    if x < shape[1]-1:
        farmtiles += old_map[y][x+1]
    if y < shape[0]-1 and x > 0:
        farmtiles += old_map[y+1][x-1]
    if y < shape[0]-1:
        farmtiles += old_map[y+1][x]
    if y < shape[0]-1 and x < shape[1]-1:
        farmtiles += old_map[y+1][x+1]
    
    #print("finished farmlands")
    return farmtiles

def save_to_rgb_image(map, colors):
    shape = map.shape
    img = numpy.ones(shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            img[i][j] = colors[img[i][j]]
            
    imageio.imwrite('image.png', img)

def save_to_greyscale_image(map):
    shape = map.shape
    img = numpy.ones(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            img[i][j] = map[i][j]*255
            
    imageio.imwrite('image.png', img)