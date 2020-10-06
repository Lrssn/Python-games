import pygame
from mapsquare import *

class Map(object):
    def __init__(self, window, camera, sizeX, sizeY):
        self.window_width = window.width
        self.window_height = window.height
        self.squarewidth = int(self.window_width/camera.scale)
        self.squareheight = int(self.window_height/camera.scale)

        
        for j in range(sizeY):
            subSquares = []
            for i in range(sizeX):
                x = Mapsquare(i, j)
                subSquares.append(x)
            self.mapsquares.append(subSquares)
    
    def render(self, camera, screen):
        #pygame.draw.rect(screen, (0, 255, 0), self.rect)
        for j in range(camera.position[1], camera.position[1] + camera.scale):
            for i in range(camera.position[0], camera.position[0] + camera.scale):
                rect = pygame.Rect((i-camera.position[0])*self.squarewidth, (j-camera.position[1])*self.squareheight, self.squarewidth, self.squareheight)
                self.mapsquares[j][i].render(screen, rect)


    squaresize = 40
    mapsquares = []