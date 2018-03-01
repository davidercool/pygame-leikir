import pygame
import random

try: from DiceGame.Button import *
except ImportError: from Button import *
pygame.init()

rollBFont = pygame.font.SysFont('Arial', 80)

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
dices = [Button(pygame.Rect(dicex[0], dicey[0], 100, 100), Button.lock, str("./Images/sd0.png")),
         Button(pygame.Rect(dicex[1], dicey[1], 100, 100), Button.lock, str("./Images/sd0.png")),
         Button(pygame.Rect(dicex[2], dicey[2], 100, 100), Button.lock, str("./Images/sd0.png")),
         Button(pygame.Rect(dicex[3], dicey[3], 100, 100), Button.lock, str("./Images/sd0.png")),
         Button(pygame.Rect(dicex[4], dicey[4], 100, 100), Button.lock, str("./Images/sd0.png"))]
rollbutton = Button(pygame.Rect((display_width-200)/2, 450, 200, 100), Button.reroll, hover=(200,200,200))
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

        for x in dices:
            x.draw(gameDisplay)
            x.clickEntered()
        rollbutton.draw(gameDisplay)
        gameDisplay.blit(rollBFont.render("Reroll", True, (0, 0, 255)), (rollbutton.x+15, rollbutton.y))
        rollbutton.clickEntered()

        # updates display every tick
        pygame.display.update()

        # tick rate
        clock.tick(60)

# run game
game_loop()