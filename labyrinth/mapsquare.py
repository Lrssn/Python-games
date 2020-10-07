import pygame

class Mapsquare(object):
    def __init__(self, posX, posY):
        self.value = (posX+posY)%255
    
    def render(self, screen, rect):
        pygame.draw.rect(screen, (0, self.value, 0), rect)