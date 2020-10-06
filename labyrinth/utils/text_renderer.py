import pygame
from pygame.locals import *
import pygame.font
class Text_renderer(object):
    def __init__(self, font = 'arial', fontsize = 30 ):
        pygame.font.init()
        self.font = pygame.font.SysFont(font, fontsize)
    
    def render(self, screen, text, position):
        text = self.font.render(str(text), True, (0, 0, 0))
        screen.blit(text, position)

    def setfont(self, font, fontsize = 30):
        self.font = pygame.font.SysFont(font, fontsize)