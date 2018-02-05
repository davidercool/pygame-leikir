import pygame
import random

from Verkefni_1.DiceGame.Button import *
from Verkefni_1.DiceGame.rolldice import *
pygame.init()

# colors
black = (0, 0, 0)
gray = (200,200,200)
white = (200,200,200)

# display size
display_width = 800
display_height = 600

# display
gameDisplay = pygame.display.set_mode((display_width,display_height))

# window name
pygame.display.set_caption('YATZEE')

# necessary for ticks
clock = pygame.time.Clock()

# game loop
def game_loop():
    # the loop where everything happens
    running = True
    while running:
        for event in pygame.event.get():
            # checks for events caused by user
            if event.type == pygame.QUIT:
                # what happens if you try pressing the close window button
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        d1 = Button(pygame.Rect(150, 300, 100, 100), int, pygame.image.load("Images/sd0.png"))
        d2 = Button(pygame.Rect(250, 100, 100, 100), int, pygame.image.load("Images/sd0.png"))
        d3 = Button(pygame.Rect(350, 300, 100, 100), int, pygame.image.load("Images/sd0.png"))
        d4 = Button(pygame.Rect(450, 100, 100, 100), int, pygame.image.load("Images/sd0.png"))
        d5 = Button(pygame.Rect(550, 300, 100, 100), int, pygame.image.load("Images/sd0.png"))
        roll = Button(pygame.Rect(350, 450, 100, 100), int, gray)
        d1.draw(gameDisplay)
        d2.draw(gameDisplay)
        d3.draw(gameDisplay)
        d4.draw(gameDisplay)
        d5.draw(gameDisplay)
        roll.draw(gameDisplay)
        if d1.click():
            pass


        # updates display every tick
        pygame.display.update()

        # tick rate
        clock.tick(60)

# run game
game_loop()