#initialize
import pygame
from tkinter import *
from pygame.sprite import Sprite
pygame.init()

#define colors
black = (0,0,0)
white=(255,255,255)
red=(255,0,0)
dark_red=(210,0,0)
dark_green=(0,170,0)
green=(0,230,0)
#define bkgrnd
bkgrnd=pygame.image.load('MenuBackground.png')
#set clock
clock=pygame.time.Clock()

def launch():
    Q=True
    while Q:
#Make close button work (which is not working for some damn reason)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Q=False
#Set menu screen
        menu_width=800 #set window size
        menu_height=600 #set window size
        menuDisplay=pygame.display.set_mode((menu_width,menu_height))#Set window size
        pygame.display.set_caption('Pygame Project')

#Fill background
        background=pygame.Surface(menuDisplay.get_size())
        background=background.convert()
        background.blit(bkgrnd, (0,0))

#Display text
        font= pygame.font.Font(None ,115)
        smallfont=pygame.font.Font(None, 26)
        starttxt= smallfont.render('Start', 1, (white))#define start button txt
        quittxt= smallfont.render('Quit', 1, (white))#define quit button txt
        #title= font.render('Greedy Goblin', 1, (white))#define title text
        #titlepos=title.get_rect()#define title box
        #titlepos.center=((menu_width/2),(menu_height/3))#title position
        #background.blit(title, titlepos)
#highlight buttons when mouse hover
        mouse=pygame.mouse.get_pos()
        if 100+200 > mouse[0] > 100 and 450+50 > mouse[1]> 450:#Highlight green
            pygame.draw.rect(background, green,(100,450,200,50))
        else:
            pygame.draw.rect(background, dark_green,(100,450,200,50))
        if 500+200> mouse[0]>500 and 450+50>mouse[1]>450:#Highlight red
            pygame.draw.rect(background, red, (500,450,200,50))
        else:                         
            pygame.draw.rect(background, dark_red,(500,450,200,50))
        click=pygame.MOUSEBUTTONDOWN
        for event in pygame.event.get():
            if (event.type==pygame.MOUSEBUTTONDOWN):
                if click and 100+200 > mouse[0] > 100 and 450+50 > mouse[1]> 450:
                    import controls
                    controls.game_loop()
                if click and 500+200> mouse[0]>500 and 450+50>mouse[1]>450:#Quit Bt
                    Q=False
        startpos= starttxt.get_rect()#define start box
        quitpos= quittxt.get_rect()#define quit box
        startpos.center=(200,475)#place start text
        quitpos.center=(600,475)#place quit text
        background.blit(quittxt, quitpos)
        background.blit(starttxt, startpos)
#blit everything to Display
        menuDisplay.blit(background, (0,0))
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()
