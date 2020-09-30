import pygame
import pyganim
class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(80, 80, 20, 20)
        self.images = pyganim.getImagesFromSpriteSheet("assets/images/test player.png", rects = self.rects)
        self.frames = list(zip(self.images, [400, 400, 400, 400]))
        self.animObj = pyganim.PygAnimation(self.frames)
        self.animObj.play()
        self.rotate(0)
    
    def move_to(self, x, y):
        self.pos[0] = x
        self.pos[1] = y
        self.rect.x = int(self.pos[0])
        self.rect.y = int(self.pos[1])

    def move(self, dx, dy, deltatime):
        # rotation
        if dx == 1 and dy == 0:
            self.rotate(-90)
        elif dx == 1 and dy == 1:
            self.rotate(-135)
        elif dx == 1 and dy == -1:
            self.rotate(-45)
        elif dx == -1 and dy == 0:
            self.rotate(90)
        elif dx == -1 and dy == 1:
            self.rotate(135)
        elif dx == -1 and dy == -1:
            self.rotate(45)
        elif dx == 0 and dy == 1:
            self.rotate(180)
        elif dx == 0 and dy == -1:
            self.rotate(0)
        self.pos[0] += dx*self.movementspeed*deltatime
        self.pos[1] += dy*self.movementspeed*deltatime
        self.rect.x = int(self.pos[0])
        self.rect.y = int(self.pos[1])
    
    def get_pos(self):
        return self.pos

    def rotate(self, angle):
        #self.rotated_image = pygame.transform.rotate(self.sprite, angle)
        if self.angle != angle:
            #this is stupid but it works TODO: make better i guess
            tempanim = pyganim.PygAnimation(self.frames)
            tempanim.play()
            #self.animObj.rotate(-self.angle)
            self.angle = angle
            tempanim.rotate(angle)
            self.animObj = tempanim
        
    
    def set_movespeed(self, newspeed):
        self.movementspeed = newspeed

    def render(self, screen):
        self.animObj.blit(screen, self.rect)
        
        
    movementspeed = 100
    angle = 0
    pos = [80,80]
    rects = [(0, 0, 16, 16),
            (16, 0, 16, 16),
            (0, 16, 16, 16),
            (16, 16, 16, 16)]
    drawrect = pygame.Rect(80, 80, 20, 20)
    animObj = None