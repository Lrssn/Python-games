import pygame
class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(80, 80, 20, 20)
        self.rotate(0)
    
    def move_to(self, x, y):
        self.pos[0] = x
        self.pos[1] = y
        self.rect.x = int(self.pos[0])
        self.rect.y = int(self.pos[1])

    def move(self, dx, dy, deltatime):
        self.pos[0] += dx*self.movementspeed*deltatime
        self.pos[1] += dy*self.movementspeed*deltatime
        self.rect.x = int(self.pos[0])
        self.rect.y = int(self.pos[1])
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
    
    def get_pos(self):
        return self.pos

    def rotate(self, angle):
        self.rotated_image = pygame.transform.rotate(self.sprite, angle)
        self.angle = angle
    
    def set_movespeed(self, newspeed):
        self.movementspeed = newspeed

    def render(self, screen):
        screen.blit(self.rotated_image, self.rect)
        
    movementspeed = 100
    rotated_image = None
    angle = 0
    pos = [0,0]
    sprite = pygame.image.load("assets/images/player.png")