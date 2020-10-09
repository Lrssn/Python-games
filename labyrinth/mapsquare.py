import pygame

class Mapsquare(object):
    def __init__(self, posX, posY):
        self.value = (posX+posY)%255
    
    def render(self, screen, rect, sprite):
        #render with correct scale
        screen.blit(sprite, rect)
    
    spriteid=0