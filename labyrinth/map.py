import pygame, json
from mapsquare import *
from utils.map_utils import *
from utils.createmap import *
import random

class Map(object):
    def __init__(self, window, camera):
        #init variables
        self.mapsquares = list()
        self.layer0 = list()
        self.layer0_scaled = list()
        self.layer1 = list()
        self.layer1_scaled = list()
        #set variables
        #sx = 100
        #map_img = createmap(sizex = 800, sizey = 600, scale = 200, octaves = 6, persistence = 0.5, lacunarity = 2.0)
        #cellular = cellular_automata(sx,sx)
        #layer1 = numpy.zeros((sx, sx))
        #for i in range(sx):
        #    subSquares = []
        #    for j in range(sx):
        #        x = Mapsquare(int(map_img[i][j]))
        #        if map_img[i][j] == 2 and cellular[i][j] == 1:
        #            x.add_layer(1)
        #        else:
        #            x.add_layer(0)
        #        subSquares.append(x)
                
        #    self.mapsquares.append(subSquares)
        #self.sizex = sx
        #self.sizey = sx
        #self.save_map(1)
        mapjson = loadmap("map1.map")
        self.sizex = mapjson['sizex']
        self.sizey = mapjson['sizey']
        self.window_width = window.width
        self.window_height = window.height
        self.squaresize = int(camera.boxsize)
        #load sprites
        self.layer0.append(pygame.image.load("assets/images/ground0.png").convert())
        self.layer0.append(pygame.image.load("assets/images/ground1.png").convert())
        self.layer0.append(pygame.image.load("assets/images/ground2.png").convert())
        self.layer1.append(pygame.image.load("assets/images/flag.png").convert_alpha())
        #create map
        #load layer0
        
        map_string0 = parsemap(mapjson['layer0'], mapjson['sizex'], mapjson['sizey'])
        map_string1 = parsemap(mapjson['layer1'], mapjson['sizex'], mapjson['sizey'])

        for j in range(self.sizey):
            subSquares = []
            for i in range(self.sizex):
                x = Mapsquare(map_string0[j][i])
                #add objects
                if map_string1[i][j] == 1:
                    x.add_layer(0)
                    x.borders[0] = 1
                    x.borders[1] = 1
                    x.borders[2] = 1
                    x.borders[3] = 1
                subSquares.append(x)
            self.mapsquares.append(subSquares)


        
        #set correct scale
        self.rescale_sprites(self.squaresize)
        
    
    def render_background(self, camera, screen):        
        for j in range(-1,round(camera.scaley)+1):
            for i in range(-1,round(camera.scalex)+1):
                mapsquare = None
                pos=camera.position
                rect = pygame.Rect(i*self.squaresize - pos[0] % camera.boxsize, j*self.squaresize - pos[1] % camera.boxsize, self.squaresize, self.squaresize)
                #layer 0
                mapsquare = self.mapsquares[int(pos[1]/self.squaresize)+j][int(pos[0]/self.squaresize)+i]
                mapsquare.render(screen, rect, self.layer0_scaled[mapsquare.spriteids[0]])
                
                #layer 1
                if len(mapsquare.spriteids) >= 2:
                    mapsquare.render(screen, rect, self.layer1_scaled[mapsquare.spriteids[1]])
                    # if layer 2 


    def render(self, camera, screen):
        self.render_background(camera, screen)

    def rescale_sprites(self, new_squaresize):
        self.squaresize = new_squaresize
        self.layer0_scaled = []
        self.layer1_scaled = []
        #rescale layer0
        for i in range(len(self.layer0)):
            image = pygame.transform.scale(self.layer0[i], (self.squaresize, self.squaresize))
            self.layer0_scaled.append(image)
        #rescale layer1
        for i in range(len(self.layer1)):
            image = pygame.transform.scale(self.layer1[i], (self.squaresize, self.squaresize))
            self.layer1_scaled.append(image)

    def save_map(self, level):
        mapname = "map" + str(level) + ".map"
        savemap(mapname, self.mapsquares, self.sizex, self.sizey)
        print("map "  + str(mapname) +  " saved")
    
    
    