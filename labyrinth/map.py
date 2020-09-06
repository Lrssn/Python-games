import pygame

class Map(object):
    def __init__(self, sizeX, sizeY):
        self.rect = pygame.Rect(0, 0, sizeX, sizeY)
    
    def render(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)