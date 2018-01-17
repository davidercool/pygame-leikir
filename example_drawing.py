import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

pygame.draw.line(gameDisplay, blue, (100,200), (300,450),5)

pygame.draw.rect(gameDisplay, red, (400,400,50,50))

pygame.draw.circle(gameDisplay, white, (150,150), 75)

pygame.draw.polygon(gameDisplay, green, ((25,75),(76,123),(250,375),(400,25),(60,540)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()