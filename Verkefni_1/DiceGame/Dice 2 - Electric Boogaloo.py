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

dicex = [150, 250, 350, 450, 550]
dicey = [300, 100, 300, 100, 300]
dicew = 100
diceh = 100

teljari = 0
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

        for x in range(5):
            d1 = Button(pygame.Rect(dicex[x], dicey[x], 500, 500), Button.lock, str("./Images/sd0.png"))
            d1.draw(gameDisplay)


        roll = Button(pygame.Rect(350, 450, 100, 100), int, gray)

        roll.draw(gameDisplay)
        if d1.click():
            pass


        # updates display every tick
        pygame.display.update()

        # tick rate
        clock.tick(60)

# run game
game_loop()