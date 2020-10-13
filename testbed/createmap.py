from random import randrange, random
import noise
import numpy
import imageio

def createmap(sizex, sizey, scale, octaves, persistence, lacunarity):
    img = numpy.zeros((sizey, sizex))
    water = [65,105,225]
    grass = [34,139,34]
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

    
    color_image = numpy.zeros(img.shape+(3,))
    for i in range(sizey):
        for j in range(sizex):
            if img[i][j] < -0.05:
                color_image[i][j] = water
            elif img[i][j] < 0:
                color_image[i][j] = beach
            elif img[i][j] < 1.0:
                color_image[i][j] = grass
            
            
    imageio.imwrite('noise.png', color_image)