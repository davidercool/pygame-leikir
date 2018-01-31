import pygame

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

def text_object(text, font):
    textSurf = font.render(text, True, black)
    return textSurf, textSurf.get_rect()

def button(x,y,w,h,i,a,action=None,msg=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, a, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, i, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = ((x + (w / 2), (y + (h / 2))))
    gameDisplay.blit(textSurf, textRect)

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
        gameDisplay.fill(white)
        button(450,450,100,100,gray,white)

    # updates display every tick
    pygame.display.update()

    # tick rate
    clock.tick(60)

# run game
game_loop()