import pygame

class Mapsquare(object):
    def __init__(self, spriteid = 0):
        self.spriteids = list()
        self.spriteids.append(spriteid)
        self.collider = False
    
    def render(self, screen, rect, sprite):
        #render with correct scale
        self.rect = rect
        screen.blit(sprite, rect)

    def add_layer(self, id):
        self.spriteids.append(id)
    
    def set_collider(self, choice):
        self.collider = choice

    def get_collider(self):
        return self.collider