import pygame
import sys
import itertools
from pygame.sprite import Sprite

pygame.init()

window = pygame.display.set_mode((1000,800))

pygame.display.set_caption("Game Window")

black = (0,0,0)
white=(255,255,255)

x,y=0,0

moveX,moveY=0,0

clock = pygame.time.Clock()

class Sprite:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=50
        self.height=50
        self.i = pygame.image.load("filler.png")
    def render(self):


        window.blit(self.i, (self.x,self.y))

player=Sprite(100,150)
gameLoop=True
while gameLoop:
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False
        if (event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_LEFT):
                    moveX = -5
                if (event.key==pygame.K_RIGHT):
                    moveX = 5
                if (event.key==pygame.K_UP):
                    moveY = -5
                if (event.key==pygame.K_DOWN):
                    moveY = 5
        if (event.type==pygame.KEYUP):
                if (event.key==pygame.K_LEFT):
                    moveX=0
                if (event.key==pygame.K_RIGHT):
                    moveX=0
                if (event.key==pygame.K_UP):
                    moveY=0
                if (event.key==pygame.K_DOWN):
                    moveY=0

    window.fill(black)
                        
    player.x+=moveX
    player.y+=moveY
    player.render()

    clock.tick(50)

    pygame.display.flip()

pygame.quit()
