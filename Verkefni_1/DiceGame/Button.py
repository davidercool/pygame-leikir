import pygame
import random
class Button():
    def __init__(self, rect, func, img=None, color=(255,255,255,0.15), hover=(0,86,224),locked=False, dicelist=None):
        self.func = func
        self.img = pygame.image.load(img) if img is not None else None
        self.rect = rect
        self.orColor = color
        self.color = color
        self.hover = hover
        self.locked = locked
        self.__prevClick = False
        self.dicelist = dicelist
        self.randimg = [pygame.image.load("./Images/sd1.png"),pygame.image.load("./Images/sd2.png"),pygame.image.load("./Images/sd3.png"),pygame.image.load("./Images/sd4.png"),pygame.image.load("./Images/sd5.png"),pygame.image.load("./Images/sd6.png")]
        self.counter = 3
        self.lookforclick = True

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
        if self.hovering:
            self.color=self.hover
        else:
            self.color = self.orColor
        return self.rect[0] <= pygame.mouse.get_pos()[0] <= self.rect[0] + self.rect[2] and self.rect[1] <= pygame.mouse.get_pos()[1] <= self.rect[1] + self.rect[3]

    def draw(self, dest: pygame.Surface):
        if self.img is None:
            pygame.draw.rect(dest, self.color, self.rect)
        else:
            dest.blit(self.img, self.rect)

    def clickEntered(self):
        if self.lookforclick:
            if pygame.mouse.get_pressed()[0] and self.hovering() and not self.__prevClick:
                self.func(self)
                self.__prevClick = True
                return True
            elif not (pygame.mouse.get_pressed()[0] and self.hovering()):
                self.__prevClick = False
            return False

    def click(self):
        if pygame.mouse.get_pressed()[0] and self.hovering():
            self.func(self)
            return True
        return False

    def lock(self):
        if self.locked:
            self.locked = False
        elif not self.locked:
            self.locked = True

    def donothing(self):
        pass

    def reroll(self):
        for x, elem in enumerate(self.dicelist):
            if elem.locked:
                pass
            elif not elem.locked:
                self.dicelist[x].img = self.randimg[random.randint(0, 5)]
        self.counter -= 1
        if self.counter == 0:
            self.lookforclick = False

