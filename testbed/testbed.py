import sys, pygame
from pygame.locals import *

pygame.init()
class Window:
    width = 800
    height = 600
    bg_color = 0, 0, 0

window = Window()
screen = pygame.display.set_mode([window.width, window.height])
clock = pygame.time.Clock()
rect = pygame.Rect(0, 0, window.width, window.height)
running = True
while running:
    # system
    deltatime  = float(clock.get_time()/1000) #newtime - oldtime
    clock.tick()


    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    #renderloop
    pygame.draw.rect(screen, (0, 255, 255), rect)
    
    pygame.display.flip()
    pygame.event.pump()

pygame.quit()
sys.exit()