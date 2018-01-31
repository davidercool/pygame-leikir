import pygame
import time
import random
pygame.init()
whiter = (255, 255, 255)
white = (155, 155, 155)
black = (0, 0, 0)
gray = (50,50,50)

display_width = 800
display_height = 600

dice = ["Images/sd0.png","Images/sd1.png","Images/sd2.png","Images/sd3.png","Images/sd4.png","Images/sd5.png","Images/sd6.png"]
dx = [display_width/2-150,display_width/2+50,display_width*0.2,display_width*0.45,display_width*0.7]
dy = [display_height*0.2,display_height*0.2,display_height*0.5,display_height*0.5,display_height*0.5]
listofdie = []

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Dice Roller 9000')

clock = pygame.time.Clock()

dices = pygame.image.load(dice[0])

def button(msg,x,y,w,h,i,a,action=None):
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

def text_object(text, font):
    textSurf = font.render(text, True, black)
    return textSurf, textSurf.get_rect()

def die(x,y):
    gameDisplay.blit(dices,(x,y))

def randdie(x,y):
    gameDisplay.blit(pygame.image.load(dice[random.randint(1,5)]),(x,y))

def roll():
    for x in range(5):
        die(dx[x],dy[x])

def reroll():
    for x in range(5):
        randdie(dx[x],dy[x])
    print("YO")
gameDisplay.fill(black)
def game_loop():
    z = 0
    yes = True
    roll()
    while yes:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    z+=1

            if z == 0:
                button("Roll", 350, 450, 100, 100, gray, white, reroll)
            elif z == 1:
                button("Final Roll", 350, 450, 100, 100, gray, white, reroll)
                print("in")
            else:
                button("No more Rolls", 350, 450, 100, 100, black, black)
        pygame.display.update()
        clock.tick(144)

game_loop()
