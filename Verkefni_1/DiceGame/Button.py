import pygame
class Button():
    def __init__(self, rect, func, img=None, color=(255,255,255), hover=(255,255,255),locked=False):
        self.func = func
        self.img = pygame.image.load(img) if img is not None else None
        self.rect = rect
        self.orColor = color
        self.color = color
        self.hover = hover
        self.locked = locked
        self.__prevClick = False

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
        if pygame.mouse.get_pressed()[0] and self.hovering() and not self.__prevClick:
            print("click entered")
            self.func(self)
            self.__prevClick = True
            return True
        elif not (pygame.mouse.get_pressed()[0] and self.hovering()):
            self.__prevClick = False
        return False

    def click(self):
        if pygame.mouse.get_pressed()[0] and self.hovering():
            print("clicked")
            self.func(self)
            return True
        return False

    def lock(self):
        if self.locked:
            self.locked = False
            print("unlocked")
        elif not self.locked:
            print("locked")
            self.locked = True

    def reroll(self):
        for x in dices:
            if x.locked:
                print("noroll")
            elif not x.locked:
                print("reroll")