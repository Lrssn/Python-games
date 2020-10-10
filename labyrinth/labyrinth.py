# system imports
import sys, pygame, random, pyganim
from pygame.locals import *

# custom imports
from player import *
from map import * 
from utils.createmap import *
from utils.text_renderer import *

# system init
pygame.init()
class Window:
    width = 800
    height = 600
    bg_color = 0, 0, 0

class Camera:
    position = [100, 100]
    scalenumber = 10
    boxsize = 100
    
    def __init__(self, sizex, sizey, mapsize):
        self.sizex = sizex
        self.sizey = sizey
        self.scalex = self.sizex / self.boxsize
        self.scaley = self.sizey / self.boxsize
        self.mapsize = mapsize

    def move(self, xdiff, ydiff):
        if (self.position[0]+xdiff) > 0 and (self.position[0]+xdiff) < (self.mapsize[0]*self.boxsize)-self.sizex:
            self.position[0] += xdiff
        if self.position[1]+ydiff > 0 and self.position[1]+ydiff < (self.mapsize[1]*self.boxsize)-self.sizey:
            self.position[1] += ydiff
    def move_to(self, xpos, ypos):
        self.position[0] = xpos
        self.position[1] = ypos
    def changescale(self, newscale):
        self.boxsize = newscale
        self.scalex = self.sizex / self.boxsize
        self.scaley = self.sizey / self.boxsize

        #updatemap?

mapsize = (100, 100)
window = Window()
camera = Camera(window.width, window.height, mapsize)
screen = pygame.display.set_mode([window.width, window.height])
clock = pygame.time.Clock()

# game init

player = Player(camera.boxsize)
map = Map(window, camera, mapsize[0], mapsize[1])
text = Text_renderer()

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
    if keys[K_u]:
        camera.changescale(50)
        player.rescale_sprites(camera.boxsize)
        map.rescale_sprites(camera.boxsize)
    if keys[K_i]:
        camera.changescale(100)
        player.rescale_sprites(camera.boxsize)
        map.rescale_sprites(camera.boxsize)


    if movement[0] != 0 or movement[1] != 0:
        player.move(movement[0], movement[1], deltatime, camera)

    # render
    screen.fill(window.bg_color)
    
    prerendertime  = pygame.time.get_ticks()
    map.render(camera, screen)
    afterrendertime = pygame.time.get_ticks() - prerendertime
        
    player.render(screen)

    #text/ui
    # TODO: make class handle text
    pygame.draw.rect(screen, (255, 255, 255), ui_rect)
    pygame.draw.rect(screen, (125, 125, 0), level_rect)
    pygame.draw.rect(screen, (255, 0, 0), close_rect)
    text.render(screen, clock.get_fps(), (close_rect.left, close_rect.top ))
    text.render(screen, afterrendertime, (level_rect.left, level_rect.top ))
    
    pygame.display.flip()
    pygame.event.pump()

pygame.quit()
sys.exit()
