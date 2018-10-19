import sys, pygame, random, pyganim
from pygame.locals import *
pygame.init()

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
        walls.append(self)
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
level = [
"WWWWWWWWWWWWWWWWWWWW",
"W                  W",
"W         WWWWWW   W",
"W   WWWW       W   W",
"W   W        WWWW  W",
"W WWW  WWWW        W",
"W   W     W W      W",
"W   W     W   WWW WW",
"W   WWW WWW   W W  W",
"W     W   W   W W  W",
"WWW   W   WWWWW W  W",
"W W      WW        W",
"W W   WWWW   WWW   W",
"W     W    E   W   W",
"WWWWWWWWWWWWWWWWWWWW",
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 20, 20)
        x += 20
    y += 20
    x = 0

running = True
while running:

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
        print("you win")
        running = False
        

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
