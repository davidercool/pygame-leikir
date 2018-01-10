import pygame
import time
pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('Cool Game')

clock = pygame.time.Clock()

man = pygame.image.load('guy.png')

def guy(x,y):
    gameDisplay.blit(man,(x,y))


def message_display(text):
    font = pygame.font.SysFont('sysfont.ttf', 115)
    gameDisplay.blit(font.render(text, True, (0, 0, 0)), ((display_width / 2) - len(text) * 25, 0))
    pygame.display.update()
    time.sleep(2)

    game_loop()

def death():
    message_display('YOU DIED!')

guy_width = 81
guy_heigt = 69

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    xmchange = 0
    xpchange = 0
    ymchange = 0
    ypchange = 0
    alive = True

    while alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xmchange = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    xmchange = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    xpchange = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    xpchange = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ymchange = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    ymchange = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ypchange = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    ypchange = 0

        x += xpchange
        x += xmchange
        y += ypchange
        y += ymchange

        gameDisplay.fill(red)
        guy(x,y)

        if x > display_width - guy_width or x < 0 or y > display_height - guy_heigt or y < 0:
            death()

        pygame.display.update()

        clock.tick(60)
game_loop()
pygame.quit()