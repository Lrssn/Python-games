import sys, pygame, random, pyganim
from pygame.locals import *
pygame.init()
from utils.createmap import *


class Window:
    width = 800
    height = 600
    bg_color = 0, 0, 0

class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(40, 40, 20, 20)

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

    sprite =  pygame.image.load("player.png")

# Nice class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)
        
class flag:
    pos = [0, 0]
    sprite =  pygame.image.load("flag.png")
    finished = False

window = Window()
player = Player()
endFlag = flag()
screen = pygame.display.set_mode([window.width, window.height])

clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Player() # Create the player

# Holds the level layout in a list of strings.
level = []
nroflevels = 10
for i in range(nroflevels):
    level.append(createMap(window.width//20, window.height//20))
#[
#"WWWWWWWWWWWWWWWWWWWW",
#"W                  W",
#"W         WWWWWW   W",
#"W   WWWW       W   W",
#"W   W        WWWW  W",
#"W WWW  WWWW        W",
#"W   W     W W      W",
#"W   W     W   WWW WW",
#"W   WWW WWW   W W  W",
#"W     W   W   W W  W",
#"WWW   W   WWWWW W  W",
#"W W      WW        W",
#"W W   WWWW   WWW   W",
#"W     W    E   W   W",
#"WWWWWWWWWWWWWWWWWWWW",
#]

# Parse the level string above. W = wall, E = exit

currentlevel = 0
def newmap(newlevel):
    walls=[]
    x = y = 0
    for row in newlevel:
        for col in row:
            if col == "W":
                walls.append(Wall((x, y)))
            x += 20
        y += 20
        x = 0
    return walls
def setend(newlevel):
    x = y = 0
    for row in newlevel:
        for col in row:
            if col == "E":
                return pygame.Rect(x, y, 20, 20)
            x += 20
        y += 20
        x = 0
nroflevels = 10
running = True
createMap(10, 10)
maploaded = False
while running:
    if maploaded == False:
        walls = newmap(level[currentlevel])
        end_rect = setend(level[currentlevel])
        maploaded = True
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); sys.exit()


    #handle input
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] or keys[K_a]:
        player.move(-2, 0)
    if keys[K_RIGHT] or keys[K_d]:
        player.move(2, 0)
    if keys[K_UP] or keys[K_w]:
        player.move(0, -2)
    if keys[K_DOWN] or keys[K_s]:
        player.move(0, 2)

    if player.rect.colliderect(end_rect):
        if currentlevel == nroflevels - 1:
            print("you win")
            running = False
        else:
            currentlevel = currentlevel + 1
            walls = newmap(level[currentlevel])
            end_rect = setend(level[currentlevel])

    screen.fill(window.bg_color)         
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    #pygame.draw.rect(screen, (255, 200, 0), player.rect)
    screen.blit(player.sprite, player.rect)
    #pygame.draw.rect(screen, (255, 0, 0), end_rect)
    screen.blit(endFlag.sprite, end_rect)
    pygame.display.flip()
    pygame.event.pump()

pygame.quit()
sys.exit()
