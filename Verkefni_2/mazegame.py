import pygame
try: from Verkefni_2.tiles import *
except ImportError: from tiles import *
pygame.init()

# colors
black = (0, 0, 0)
white = (255, 255, 255  )
red =   (255, 0, 0)
green = (0, 255, 0)
blue =  (0, 0, 255)

# display size
display_width = 1200
display_height = 672

# display
gameDisplay = pygame.display.set_mode((display_width,display_height))

# window name
pygame.display.set_caption('Maze')

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
        wall = Tile(gameDisplay)
        for x in range(42):
            wall.draw(x, x)
        # updates display every tick
        pygame.display.update()

        # tick rate
        clock.tick(60)

# run game
game_loop()