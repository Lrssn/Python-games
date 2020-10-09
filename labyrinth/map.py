import pygame
from mapsquare import *

class Map(object):
    def __init__(self, window, camera, sizeX, sizeY):
        self.window_width = window.width
        self.window_height = window.height
        self.squaresize = int(camera.boxsize)
        self.sprites.append(pygame.image.load("assets/images/flag.png"))
        
        for j in range(sizeY):
            subSquares = []
            for i in range(sizeX):
                x = Mapsquare(i, j)
                subSquares.append(x)
            self.mapsquares.append(subSquares)
        
        self.rescale_sprites(self.squaresize)
    
    def render_background(self, camera, screen):        
        for j in range(-1,round(camera.scaley)+1):
            for i in range(-1,round(camera.scalex)+1):
                pos=camera.position
                rect = pygame.Rect(i*self.squaresize - pos[0] % camera.boxsize, j*self.squaresize - pos[1] % camera.boxsize, self.squaresize, self.squaresize)
                mapsquare = self.mapsquares[int(pos[1]/self.squaresize)+j][int(pos[0]/self.squaresize)+i]
                mapsquare.render(screen, rect, self.scaled_sprites[mapsquare.spriteid])


    def render(self, camera, screen):
        self.render_background(camera, screen)

    def rescale_sprites(self, new_squaresize):
        self.squaresize = new_squaresize
        self.scaled_sprites = []
        for i in range(len(self.sprites)):
            image = pygame.transform.scale(self.sprites[i], (self.squaresize, self.squaresize))
            self.scaled_sprites.append(image)

    
    mapsquares = []
    sprites = []
    scaled_sprites = []