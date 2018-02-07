import pygame
class Button():
    def __init__(self, rect, func, img=None, color=(255,255,255), hover=(255,255,255),locked=False):
        self.func = func
        self.img = pygame.image.load("Images/sd0.png").convert()
        self.rect = rect
        self.color = color
        self.hover = hover
        self.locked = locked

    @property
    def x(self):
        return self.rect[0]

    @property
    def y(self):
        return self.rect[1]

    @property
    def width(self):
        return self.rect[2]

    @property
    def height(self):
        return self.rect[3]

    def hovering(self):
        return self.rect[0] <= pygame.mouse.get_pos()[0] <= self.rect[0] + self.rect[2] and self.rect[1] <= pygame.mouse.get_pos()[1] <= self.rect[1] + self.rect[3]

    def draw(self, dest):
        if self.img is None:
            pygame.draw.rect(dest, self.color, self.rect)
        else:
            #gameDisplay.blit(pygame.image.load(dice[random.randint(1, 5)]), (x, y))
            """print(self.rect[0])
            print(self.rect[1])
            print(self.rect[2])
            print(self.rect[3])
            print("-----------")"""
            dest.blit(self.img, (self.width,self.height))
    def click(self):
        if pygame.mouse.get_pressed()[0] and self.hovering():
            self.func()

    def lock(self):
        if self.locked == False:
            self.locked=True
        else:
            self.locked=False