# Import modules for game development
import pygame
import sys
import itertools
import random
from pygame.sprite import Sprite
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Display Colors
white=(255,255,255)
black = (0,0,0)

# Set Display Height and Width
fps = 30
display_width = 1000
display_height = 800
cellSize = 50

#Directions
UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

# Player Width
x = 50
y = 50
bg = "Bkgr.png"

# Set Game Window
global gameDisplay
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Caption in top by Python 3.4 etc.
pygame.display.set_caption("Dodgem")

# FPS Clock
clock = pygame.time.Clock()

# Player Images
bgimage = pygame.image.load("Bkgr.png")
playerImage = pygame.image.load("filler.png")
enemyImage = pygame.image.load("enemy.png")

#Background
def backgroud():
    gameDisplay.blit(bg,(1000,800))
    
# Player Sprite
def player (x,y):
    gameDisplay.blit(playerImage,(100,200))

# Enemy
def enemy():
    gameDisplay.blit(enemyImage,(800,500))

def enemymove(enemy):
    newCell = {'x':enemy[0]['x']+1, 'y':enemy[0]['y']}
    del enemy[-1]
    enemy.insert(0,newCell)


def runGame():
    # Image Display
    startx = 3
    starty = 3
    coords = [{'x': startx, 'y': starty}]
    enemycoords1 = [{'x':15, 'y':15}]
    direction = RIGHT

    
    isAlive = 'yes'

    #x_change = 0
    #y_change = 0

    # Logic Statement
    gameExit = False

    while not gameExit:
    
    #while True:

        while isAlive == 'yes':

            # Quit Logic
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                # Movement
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        direction = LEFT
                        #x_change = -5
                    elif event.key == pygame.K_RIGHT:
                        direction = RIGHT
                        #x_change = 5
                    elif event.key == pygame.K_UP:
                        direction = UP
                        #y_change = 5
                    elif event.key == pygame.K_DOWN:
                        direction = DOWN
                        #y_change = -5

            if direction == UP:
                player = {'x':coords[0]['x'], 'y':coords[0]['y']-1}

            elif direction == DOWN:
                player = {'x':coords[0]['x'], 'y':coords[0]['y']+1}

            elif direction == LEFT:
                player = {'x':coords[0]['x']-1, 'y':coords[0]['y']}

            elif direction == RIGHT:
                player = {'x':coords[0]['x']+1, 'y':coords[0]['y']}

            del coords[-1]


            coords.insert(0, player)
            gameDisplay.fill(black)

            enemymove(enemycoords1)
            
            player(coords)
            enemy(enemycoords1)
            
            pygame.display.update()
            #fpsTime.tick(fps)

                # Stop Movement
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0

            #x += x_change
            #y += y_change
            #gameDisplay.fill(black)
            #player(x,y)
            #pygame.display.flip()
            #clock.tick(30)


            enemymove(enemycoords1)

            player(coords)
            enemy(enemycoords1)

            if (player['x'] < 0 or player['y'] < 0 or player['x'] > 0 or player['y'] > 0):
                isAlive = 'no'

        #msgSurface ('Game Over', red)


def drawCell(coords):
    for coord in coords:
        x = coord['x'] * cellSize
        y = coord['y'] * cellSize
        makeCell = pygame.Rect(x, y, cellSize, cellSize)
        pygame.draw.rect(gameDisplay, white, makeCell)

while True:
    global fpsTime
    #global gameDisplay

    fpsTime = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    runGame()

#runGame()
# Quit
pygame.quit()
quit()
