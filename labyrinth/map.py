import pygame
from mapsquare import *

class Map(object):
    def __init__(self, window, camera, sizeX, sizeY):
        self.window_width = window.width
        self.window_height = window.height
        self.squarewidth = int(camera.boxsize)
        self.squareheight = int(camera.boxsize)

        
        for j in range(sizeY):
            subSquares = []
            for i in range(sizeX):
                x = Mapsquare(i, j)
                subSquares.append(x)
            self.mapsquares.append(subSquares)
    
    def render(self, camera, screen):        
        for j in range(round(camera.scaley)):
            for i in range(round(camera.scalex)):
                pos=camera.position
                rect = pygame.Rect(i*self.squarewidth, j*self.squareheight, self.squarewidth, self.squareheight)
                self.mapsquares[int(pos[1]/self.squareheight)+j][int(pos[0]/self.squarewidth)+i].render(screen, rect)


    
    mapsquares = []