import pygame

class Map(object):
    def __init__(self, sizeX, sizeY):
        self.rect = pygame.Rect(0, 0, sizeX, sizeY)
    
    def render(self, screen):
        

    rect = None