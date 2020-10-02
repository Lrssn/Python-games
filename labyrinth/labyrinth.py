# system imports
import sys, pygame, random, pyganim
from pygame.locals import *
import pygame.font

# custom imports
from utils.createmap import *
from player import *
from map import * 

# system init
pygame.init()
class Window:
    width = 800
    height = 600
    bg_color = 0, 0, 0

class Camera:
    position = [50, 50]
    scale = 10
    def move(self, xdiff, ydiff):
        self.position[0] += xdiff
        self.position[1] += ydiff
    def move_to(self, xpos, ypos):
        self.position[0] = xpos
        self.position[1] = ypos
    def changescale(self, newscale):
        self.scale = newscale
        #updatemap?


window = Window()
camera = Camera()
screen = pygame.display.set_mode([window.width, window.height])
pygame.font.init()
myfont = pygame.font.SysFont('arial', 30)
clock = pygame.time.Clock()

# game init
player = Player()
map = Map(window, camera, 100, 100)


# UI setup
ui_rect = pygame.Rect(0, 0, window.width, 40)
level_rect = pygame.Rect(0, 0, window.width//4, 40)
close_rect = pygame.Rect(window.width-60, 0, 60, 40)

running = True
while running:
    # system
    deltatime  = float(clock.get_time()/1000) #newtime - oldtime
    clock.tick()
    
    #handle input
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #process mouseclicks
            pos = pygame.mouse.get_pos()
            if close_rect.collidepoint(pos):
                pygame.quit() 
                sys.exit()
    #process player movement
    movement = [0, 0]
    if keys[K_LEFT] or keys[K_a]:
        movement[0] -= 1
    if keys[K_RIGHT] or keys[K_d]:
        movement[0] += 1
    if keys[K_UP] or keys[K_w]:
        movement[1] -= 1
    if keys[K_DOWN] or keys[K_s]:
        movement[1] += 1
    if keys[K_DOWN] or keys[K_u]:
        camera.move_to(10,10)
    if keys[K_DOWN] or keys[K_i]:
        camera.move_to(50,50)


    if movement[0] != 0 or movement[1] != 0:
        player.move(movement[0], movement[1], deltatime, camera)
        
    fpstext = myfont.render(str(clock.get_fps()), True, (0, 0, 0))


    # render
    screen.fill(window.bg_color)
    
    prerendertime  = pygame.time.get_ticks()
    map.render(camera, screen)
    afterrendertime = pygame.time.get_ticks() - prerendertime
    rendertext = myfont.render(str(afterrendertime), True, (0, 0, 0))
    
    player.render(screen)

    #text/ui
    pygame.draw.rect(screen, (255, 255, 255), ui_rect)
    pygame.draw.rect(screen, (125, 125, 0), level_rect)
    pygame.draw.rect(screen, (255, 0, 0), close_rect)
    screen.blit(fpstext, (close_rect.left, close_rect.top ))
    screen.blit(rendertext, (level_rect.left, level_rect.top ))
    
    pygame.display.flip()
    pygame.event.pump()

pygame.quit()
sys.exit()
