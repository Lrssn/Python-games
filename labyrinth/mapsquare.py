import pygame

class Mapsquare(object):
    def __init__(self, spriteid = 0):
        self.spriteids = list()
        self.spriteids.append(spriteid)
        self.borders = [0, 0, 0, 0]
    
    def render(self, screen, rect, sprite):
        #render with correct scale
        screen.blit(sprite, rect)

    def add_layer(self, id):
        self.spriteids.append(id)
    
    def set_borders(self, borders):
        self.borders = borders