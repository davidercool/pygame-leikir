import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
dark_red = (150,0,0)
green = (0, 255, 0)
dark_green = (0,150,0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption('Cool Game')

clock = pygame.time.Clock()

man = pygame.image.load('guy.png')

def dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def candy(candyx,candyy,candyw,candyh,color):
    pygame.draw.rect(gameDisplay, color, [candyx,candyy,candyw,candyh])

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

def game_intro():
    intro = True
    text = "cool game"
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        font = pygame.font.SysFont('sysfont.ttf', 115)
        gameDisplay.blit(font.render(text, True, (0, 0, 0)), ((display_width / 2) - len(text) * 22, display_height/2-100))

        mouse = pygame.mouse.get_pos()

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, dark_green, (150,450,100,50))
        if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, dark_red, (550, 450, 100, 50))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect

        pygame.display.update()
        clock.tick(144)



def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    guy_speed = 5
    xmchange = 0
    xpchange = 0

    candy_speed = 7
    candy_width = 100
    candy_height = 100
    candy_startx = random.randrange(0, display_width-candy_width)
    candy_starty = -400
    dodge = 0
    candy_count = 0

    alive = True

    while alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xmchange = -guy_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    xmchange = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    xpchange = guy_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    xpchange = 0

        x += xpchange
        x += xmchange

        gameDisplay.fill(red)

        for x in range(candy_count):
            candy(candy_startx, candy_starty, candy_width, candy_height, blue)

        candy_starty += candy_speed

        guy(x,y)
        dodged(dodge)
        if x > display_width - guy_width or x < 0 or y > display_height - guy_heigt or y < 0:
            death()

        if candy_starty > display_height:
            candy_starty = 0 - candy_height
            candy_startx = random.randrange(0,display_width)
            dodge += 1
            if candy_speed < 15:
                candy_speed+=1
                guy_speed += 1
            if dodge % 5 == 0:
                candy_count += 1

        pygame.display.update()

        if y < candy_starty+candy_height:
            if x > candy_startx and x < candy_startx + candy_width or x + guy_width > candy_startx and x + guy_width < candy_startx+candy_width:
                death()

        clock.tick(144)
game_intro()
game_loop()
pygame.quit()