import pygame

pygame.init()

# colors
black = (0, 0, 0)

# display size
display_width = 800
display_height = 600

# display
gameDisplay = pygame.display.set_mode((display_width,display_height))

# window name
pygame.display.set_caption('Template')

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

    # updates display every tick
    pygame.display.update()

    # tick rate
    clock.tick(60)

# run game
game_loop()