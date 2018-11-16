# Import modules for game development
import pygame
import sys
import itertools
import random
from pygame.sprite import Sprite
import MainMenu

# Set up Pygame Sound Mixer
pygame.mixer.pre_init(44100, -16, 2, 2048)

# Initialize Pygame
pygame.init()

# Set Display Height and Width
display_width = 800
display_height = 600

# Player Width
player_width = 50
player_height = 50

# Display Colors
black = (0,0,0)
white=(255,255,255)

# Set Game Window
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Caption in top by Python 3.4 etc.
pygame.display.set_caption("Greedy Goblin!")

# FPS Clock
clock = pygame.time.Clock()

#game background
bkgrnd= pygame.image.load('images/background.png')

# Player Image
playerImage = pygame.image.load("images/hero.png")

# Boulder Images
rockImage = pygame.image.load("images/rock.png")
rock2Image = pygame.image.load("images/rock2.png")

# Score Item Images
GoldCoinImage = pygame.image.load('images/GoldCoin.png')
SilverCoinImage = pygame.image.load('images/SilverCoin.png')
BlueDiamondImage = pygame.image.load('images/BlueDiamond.png')
EmeraldImage = pygame.image.load('images/GreenEmerald.png')
RubyImage = pygame.image.load('images/RedRuby.png')

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text, (0,0))
    
# Falling Rock Classes (Obstacles)
def rock(rockx, rocky, rockw, rockh):
    gameDisplay.blit(rockImage, (rockx,rocky))

def rock2(rockx, rocky, rockw, rockh):
    gameDisplay.blit(rock2Image, (rockx,rocky))

# Pick-up Items
def GoldCoin(GoldCoinx, GoldCoiny, GoldCoinw, GoldCoinh):
    gameDisplay.blit(GoldCoinImage, (GoldCoinx,GoldCoiny))

def SilverCoin(SilverCoinx, SilverCoiny, SilverCoinw, SilverCoinh):
    gameDisplay.blit(SilverCoinImage, (SilverCoinx,SilverCoiny))

def Diamond(Diamondx, Diamondy, Diamondw, Diamondh):
    gameDisplay.blit(BlueDiamondImage, (Diamondx,Diamondy))

def Emerald(Emeraldx, Emeraldy, Emeraldw, Emeraldh):
    gameDisplay.blit(EmeraldImage, (Emeraldx,Emeraldy))

def Ruby(Rubyx, Rubyy, Rubyw, Rubyh):
    gameDisplay.blit(RubyImage, (Rubyx,Rubyy))

# Player Sprite
def player(x,y):
    gameDisplay.blit(playerImage,(x,y))

def game_loop():
    # Image Display
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    #Music
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.40)

    # Rock Random Generation (Start, speed)
    rock_startx = random.randrange(0, display_width)
    rock_starty = -600
    rock_speed = 7
    rock_height = 70
    rock_width = 70

    # Rock 2 Generation
    rock2_startx = random.randrange(0, display_width)
    rock2_starty = -300
    rock2_speed = 4
    rock2_height = 70
    rock2_width = 70

    # GoldCoin Generation
    GoldCoin_startx = random.randrange(0, display_width)
    GoldCoin_starty = -300
    GoldCoin_speed = 3
    GoldCoin_height = 20
    GoldCoin_width = 20

    # SilverCoin Generation
    SilverCoin_startx = random.randrange(0, display_width)
    SilverCoin_starty = -300
    SilverCoin_speed = 3
    SilverCoin_height = 20
    SilverCoin_width = 20

    # Dimaond Generation
    Diamond_startx = random.randrange(0, display_width)
    Diamond_starty = -900
    Diamond_speed = 8
    Diamond_height = 20
    Diamond_width = 20

    # Emerald Generation
    Emerald_startx = random.randrange(0, display_width)
    Emerald_starty = -600
    Emerald_speed = 5
    Emerald_height = 20
    Emerald_width = 20

    # Ruby Generation
    Ruby_startx = random.randrange(0, display_width)
    Ruby_starty = -900
    Ruby_speed = 6
    Ruby_height = 20
    Ruby_width = 20

    scored = 0

    # Logic Statement
    gameExit = False

    while not gameExit:

        # Quit Logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            # Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10

            # Stop Movement
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.blit(bkgrnd,(0,0))

        #rock(rockx, rocky, rockw, rockh)
        rock(rock_startx, rock_starty, rock_width, rock_height)
        rock_starty += rock_speed

        #rock2(rock2x, rock2y, rock2w, rock2h)
        rock2(rock2_startx, rock2_starty, rock2_width, rock2_height)
        rock2_starty += rock2_speed

        #GoldCoin(GoldCoinx, GoldCoiny, GoldCoinw, GoldCoinh)
        GoldCoin(GoldCoin_startx, GoldCoin_starty, GoldCoin_width, GoldCoin_height)
        GoldCoin_starty += GoldCoin_speed

        #SilverCoin(SilverCoinx, SilverCoiny, SilverCoinw, SilverCoinh)
        SilverCoin(SilverCoin_startx, SilverCoin_starty, SilverCoin_width, SilverCoin_height)
        SilverCoin_starty += SilverCoin_speed

        #Diamond(Diamondx, Diamondy, Diamondw, Diamondh)
        Diamond(Diamond_startx, Diamond_starty, Diamond_width, Diamond_height)
        Diamond_starty += Diamond_speed

        #Emerald(Emeraldx, Emeraldy, Emeraldw, Emeraldh)
        Emerald(Emerald_startx, Emerald_starty, Emerald_width, Emerald_height)
        Emerald_starty += Emerald_speed

        #Ruby(Rubyx, Rubyy, Rubyw, Rubyh)
        Ruby(Ruby_startx, Ruby_starty, Ruby_width, Ruby_height)
        Ruby_starty += Ruby_speed

        score(scored)
        
        player(x,y)

        # L/R Boundary Statement
        if x > display_width - player_width or x < 0:
            gameExit = True
            pygame.mixer.music.stop()

        # Rock Spawn Logic Statements
        if rock_starty > display_height:
            rock_starty = 0 - rock_height
            rock_startx = random.randrange(0, display_width)
            scored += 1
            rock_speed += 0.1
    
        if rock2_starty > display_height:
            rock2_starty = 0 - rock2_height
            rock2_startx = random.randrange(0, display_width)
            scored += 1
            rock2_speed += 0.2

        # Score Items Spawn Logic Statements

        # GoldCoin Logic
        if GoldCoin_starty > display_height:
            GoldCoin_starty = 0 - rock2_height
            GoldCoin_startx = random.randrange(0, display_width)

        # SilverCoin Logic
        if SilverCoin_starty > display_height:
            SilverCoin_starty = 0 - rock2_height
            SilverCoin_startx = random.randrange(0, display_width)

        # Diamond Spawn Logic
        if Diamond_starty > display_height:
            Diamond_starty = 0 - rock2_height
            Diamond_startx = random.randrange(0, display_width)

        # Emerald Spawn Logic
        if Emerald_starty > display_height:
            Emerald_starty = 0 - rock2_height
            Emerald_startx = random.randrange(0, display_width)

        # Ruby Spawn Logic
        if Ruby_starty > display_height:
            Ruby_starty = 0 - rock2_height
            Ruby_startx = random.randrange(0, display_width)
            
        # Collision Logic Statements
        
        # Rock 1 Collision ( Faster Rock )
        if y < rock_starty+rock_height:
            if x > rock_startx and x < rock_startx+rock_width or x+player_width > rock_startx and x + player_width < rock_startx+rock_width:
                gameExit = True
                pygame.mixer.music.stop()
        # Rock 2 Collision ( Slower Rock )
        if y < rock2_starty+rock2_height:
            if x > rock2_startx and x < rock2_startx+rock2_width or x+player_width > rock2_startx and x + player_width < rock2_startx+rock2_width:
                gameExit = True
                pygame.mixer.music.stop()
        pygame.display.flip()
        clock.tick(60)

    MainMenu.launch()



