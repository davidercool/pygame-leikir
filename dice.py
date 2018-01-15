import pygame
import time
import random

pygame.init()

black = (0, 0, 0)

display_width = 800
display_height = 600

dice = ["Images/sd0.png","Images/sd1.png","Images/sd2.png","Images/sd3.png","Images/sd4.png","Images/sd5.png","Images/sd6.png"]
dx = [display_width*0.32,display_width*0.58,display_width*0.2,display_width*0.45,display_width*0.7]
dy = [display_height*0.3,display_height*0.3,display_height*0.6,display_height*0.6,display_height*0.6]
listofdie = []

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Dice Roller 9000')

clock = pygame.time.Clock()

dices = pygame.image.load(dice[0])

randomdie = pygame.image.load(dice[random.randint(1,5)])

def die(x,y):
    gameDisplay.blit(dices,(x,y))

def randdie(x,y):
    gameDisplay.blit(randomdie,(x,y))

def roll():
    for x in range(5):
        die(dx[x],dy[x])

def reroll():
    for x in range(5):
        randdie(dx[x],dy[x])

def game_loop():
    z = 0
    yes = True
    while yes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                z+=1
        gameDisplay.fill(black)
        if z == 0:
            roll()
        if z > 0:
            reroll()
        pygame.display.update()
        print(z)
        clock.tick(1)

game_loop()