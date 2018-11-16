import pygame
import sys
import random
import itertools
#from helpers import *
from pygame.sprite import Sprite

#class Bkgr(pygame.sprite.Sprite):
#    def __init__(self, i):                      
#        pygame.sprite.Sprite.__init__(self)
#        self.i, self.rect = pygame.image.load("Bkgr.png")
        #self.i = pygame.image.load("Bkgr.png")
#        self.dx = -5
#        self.reset(i)

#    def update(self, i):
#        self.rect.top += self.dx
#        if i == 1:
#           if self.rect.top <= -600:
#                self.__init__(i) 
#        else:
#            if self.rect.top <= -1200:
#                self.__init__(i) 

#    def reset(self, i):
#        if i == 1:
#            self.rect.top = 1
#        else:
#            self.rect.top = 300

class Player:
    #def __init__(self,x,y):
    #    self.x=x
    #    self.y=y
    #    self.width=50
    #    self.height=50
    #    self.i = pygame.image.load("filler.png")
    #def render(self):

    #    window.blit(self.i, (self.x,self.y))

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        #self.image, self.rect = load_image('filler.png', -1)
        self.image = pygame.image.load("filler.png")
        self.rect = pygame.Rect(100, 150, 50, 50)
        self.x_dist = 5
        self.y_dist = 5
        self.width=50
        self.height=50
        #self.lasertimer = 0
        #self.lasermax = 5
        self.centery = 400
        self.centerx = 400

    def update(self):
        key = pygame.key.get_pressed()

        # Movement
#        if key[K_UP]:
#            self.rect.centery += -5
#        if key[K_DOWN]:
#            self.rect.centery += 5
#        if key[K_RIGHT]:
#            self.rect.centerx += 5
#        if key[K_LEFT]:
#            self.rect.centerx += -5

class Enemy(pygame.sprite.Sprite):
    def __init__(self, centerx):
        pygame.sprite.Sprite.__init__(self)
        #self.image, self.rect = pygame.load.image("enemy.png", -1)
        self.image = pygame.image.load("enemy.png")
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.dy = 8
        self.reset()

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > 600:
            self.reset()

        # Player Collisions
        if pygame.sprite.groupcollide(enemySprites, playerSprite, 1, 1):
           explosionSprites.add(EnemyExplosion(self.rect.center))
           explosionSprites.add(PlayerExplosion(self.rect.center))

    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(0, 600)
        self.dy = random.randrange(5, 10)
        self.dx = random.randrange(-2, 2)

class EnemyExplosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        #self.image, self.rect = load_image("enemyexplosion.png", -1)
        self.image = pygame.image.load("enemyexplosion.png")
        self.rect.center = pos        
        self.counter = 0
        self.maxcount = 10

    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()

class PlayerExplosion(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        #self.image, self.rect = pygame.load.image("enemyexplosion.png", -1)
        self.image = pygame.image.load("enemyexplosion.png")
        self.rect.center = pos        
        self.counter = 0
        self.maxcount = 10

    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()
            exit()

#def main():
pygame.init()

screen = pygame.display.set_mode((1000,800))

pygame.display.set_caption("Game Window")

    #black = (0,0,0)
    #white=(255,255,255)

    #x,y=0,0

    #moveX,moveY=0,0

    #clock = pygame.time.Clock()

    # Create The Backgound

background = pygame.Surface(screen.get_size())

background = pygame.image.load("Bkgr.png").convert()

background.fill((000, 000, 000))

# Display The Background

screen.blit(background, [0, 0])

pygame.display.flip()
    
#Initialize Game Objects
global clock

clock = pygame.time.Clock()
    #backgroundpygame.image.load

i = 0
i += 1

#bkgr = Bkgr(i)

global player

player = Player()


# Render Objects
    # Background
#bkgr = pygame.sprite.RenderPlain((bkgr))

    # Player
#global playerSprite   
#playerSprite = pygame.sprite.RenderPlain((player))

    # Enemy
global enemySprites
enemySprites = pygame.sprite.RenderPlain(())
enemySprites.add(Enemy(200))
enemySprites.add(Enemy(300))
enemySprites.add(Enemy(400))    

    # Collisions   
global enemyExplosion
screen.blit(background, [0, 0])
#enemyExplosion = pygame.sprite.RenderPlain(())
global playerExplosion
#playerExplosion = pygame.sprite.RenderPlain(())
global explosionSprites
#explosionSprites = pygame.sprite.RenderPlain(())


#player=Sprite(100,150)
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

        #window.fill(black)
                        
#    player.x+=moveX
#    player.y+=moveY
#    player.render()

    clock.tick(50)

#    bkgr.update(i)
    player.update()
    enemySprites.update()
    enemyExplosion.update()
    playerExplosion.update()
    explosionSprites.update()



    screen.blit(background, (0, 0))


        # Draw
#    bkgr.draw(screen)          
    playerSprite.draw(screen)
    enemySprites.draw(screen)
    enemyExplosion.draw(screen)
    playerExplosion.draw(screen)
    explosionSprites.draw(screen)


    pygame.display.flip()
    
pygame.quit()

#if __name__ == '__main__':

#main()
