import random
import noise
import numpy
import imageio

def createmap(sizex, sizey, scale, octaves, persistence, lacunarity):
    img = numpy.zeros((sizey, sizex))
    water = [65,105,225]
    grass = [34,139,34]
    forest = [0, 255, 12]
    farmland = [245, 222, 179]
    beach = [238, 214, 175]
    for i in range(sizey):
        for j in range(sizex):
            img[i][j] = noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=0)
    set_image = numpy.zeros(img.shape)
    for i in range(sizey):
        for j in range(sizex):
            if img[i][j] < -0.05:
                set_image[i][j] = 0
            elif img[i][j] < 0:
                set_image[i][j] = 1
            elif img[i][j] < 1.0:
                set_image[i][j] = 2
    flood_img = cellular_automata(sizex, sizey)
    color_image = numpy.zeros(img.shape+(3,))
    for i in range(sizey):
        for j in range(sizex):
            if set_image[i][j] == 0:
                color_image[i][j] = water
            elif set_image[i][j] == 1:
                color_image[i][j] = beach
            elif set_image[i][j] == 2:
                if flood_img[i][j] == 0:
                    color_image[i][j] = forest
                elif flood_img[i][j] == 1:
                    color_image[i][j] == farmland

    imageio.imwrite('noise.png', color_image)

def cellular_automata(sizex, sizey):
    shape = (sizey, sizex)
    Forest = 0
    Farm = 1
    forestsize = 0.4

    new_map = numpy.ones(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            choice = random.uniform(0, 1)
            new_map[i][j] = Forest if choice < forestsize else Farm

    # run for 6 generations
    nrofsimsteps = 7
    starvationLimit = 4
    overpopLimit = 6
    birthNumber = 4
    temp_map = numpy.ones(shape)
    for simstep in range(nrofsimsteps):
        for i in range(shape[0]):
            for j in range(shape[1]):
                farmtiles = nr_of_farmtiles(new_map, j, i, shape)
                if new_map[i][j] == Farm:
                    if farmtiles < starvationLimit:
                        temp_map[i][j] = Forest
                    if farmtiles > overpopLimit:
                        temp_map[i][j] = Forest
                else:
                    if farmtiles == birthNumber:
                        temp_map[i][j] = Farm

        new_map = temp_map

    colored = numpy.ones(shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            colored[i][j] = [0, 255, 12] if new_map[i][j] == Forest else [245, 222, 179]
    imageio.imwrite('colored.png', colored)
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
