import pygame
import pyganim
import map
class Player(object):
    
    def __init__(self, size, bufferzone):
        self.squaresize = size
        self.rect = pygame.Rect(120, 120, size, size)
        self.images = pyganim.getImagesFromSpriteSheet("assets/images/test player.png", rects = self.rects)
        self.rescale_sprites(size)
        self.bufferzone = bufferzone
    
    def move_to(self, x, y):
        self.pos[0] = x
        self.pos[1] = y
        self.rect.x = int(self.pos[0])
        self.rect.y = int(self.pos[1])

    def move(self, dx, dy, deltatime, camera, map):
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

        xdiff = dx*self.movementspeed*deltatime
        ydiff = dy*self.movementspeed*deltatime

        #move camera
        camera_xdiff = 0
        camera_ydiff = 0
        camera_size = (camera.sizex, camera.sizey)

        if dx == -1 and self.pos[0] <= self.bufferzone:
            camera_xdiff = xdiff
        elif dx == 1 and self.pos[0] >= camera_size[0]-self.bufferzone:
            camera_xdiff = xdiff
        if dy == -1 and self.pos[1] <= self.bufferzone:
            camera_ydiff = ydiff
        elif dy == 1 and self.pos[1] >= camera_size[1]-self.bufferzone:
            camera_ydiff = ydiff
        
        if camera_xdiff != 0 or camera_ydiff != 0:
            camera.move(camera_xdiff, camera_ydiff)
             
            # get player worldpos
            # check if right has collider
            # check if player collides with right
            # move rigth out
            # do the same for up, down and left
            # something like this:  
            #if dx > 0 and self.rect.colliderect(map.mapsquares[int(self.pos[0]+camera.position[0])][int(self.pos[1]+camera.position[1])].rect):: # Moving right; Hit the left side of the wall
                #self.rect.right = wall.rect.left
                
        self.pos[0] += (xdiff - camera_xdiff)
        self.pos[1] += (ydiff - camera_ydiff)
        self.rect.x = int(self.pos[0])
        self.rect.y = int(self.pos[1])

    def get_pos(self):
        return self.pos

    def rotate(self, angle):
        if self.angle != angle:
            self.angle = angle
            #this is stupid but it works TODO: make better i guess
            tempanim = pyganim.PygAnimation(self.frames)
            tempanim.play()
            tempanim._playingStartTime = self.animObj._playingStartTime
            tempanim.rotate(angle)
            self.animObj = tempanim
        
    
    def set_movespeed(self, newspeed):
        self.movementspeed = newspeed

    def render(self, screen):
        self.animObj.blit(screen, self.rect)
    
    def rescale_sprites(self, new_squaresize):
        scalechange = new_squaresize / self.squaresize
        self.move_to(self.pos[0]*scalechange, self.pos[1]*scalechange)
        self.movementspeed *= scalechange
        self.squaresize = new_squaresize
        self.scaled_sprites = []
        for i in range(len(self.images)):
            image = pygame.transform.scale(self.images[i], (self.squaresize, self.squaresize))
            self.scaled_sprites.append(image.convert_alpha())
        
        self.frames = list(zip(self.scaled_sprites, [1000, 1000, 1000, 1000]))
        self.animObj = pyganim.PygAnimation(self.frames)
        self.animObj.play()
        self.rotate(0)

    movementspeed = 1000
    angle = 0
    pos = [120,120]
    rects = [(0, 0, 16, 16),
            (16, 0, 16, 16),
            (0, 16, 16, 16),
            (16, 16, 16, 16)]
    animObj = None