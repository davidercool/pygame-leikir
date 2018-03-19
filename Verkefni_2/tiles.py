import pygame
class Tile():
    def __init__(self, display):
        self.w = 16
        self.h = 16
        self.display = display

    def draw(self, x, y):
        pygame.draw.rect(self.display, (255,255,255), (x*16, y*16, self.w, self.h))