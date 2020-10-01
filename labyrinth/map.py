import pygame

class MapSquare(object):
    def __init__(self, posX, posY, sizeX, sizeY):


class Map(object):
    def __init__(self, sizeX, sizeY):
        self.rect = pygame.Rect(0, 0, sizeX, sizeY)
    
    def render(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)

    squaresize = 40
    mapsquares[][] = None