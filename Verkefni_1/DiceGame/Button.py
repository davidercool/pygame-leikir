import pygame
class Button():
    def __init__(self, rect, func, img=None, color=(255,255,255)):
        self.func = func
        self.rect = rect
        self.img = img
        self.color = color

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
    def heigth(self):
        return self.rect[3]

    def hovering(self):
        return self.rect[0] <= pygame.mouse.get_pos()[0] <= self.rect[0] + self.rect[2] and self.rect[1] <= pygame.mouse.get_pos()[1] <= self.rect[1] + self.rect[3]

    def draw(self, dest):
        if self.img is None:
            pygame.draw.rect(dest, self.color, self.rect)
        else:
            dest.blit(pygame.transform.scale(self.img, (self.width, self.heigth)), (self.x, self.y))

    def click(self):
        if pygame.mouse.get_pressed()[0] and self.hovering():
            self.func()