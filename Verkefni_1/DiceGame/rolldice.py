import pygame
import random
from Verkefni_1.DiceGame.Button import *
images = ["images/sd1.png","images/sd2.png","images/sd3.png","images/sd4.png","images/sd5.png","images/sd6.png",]
class dice():
    def roll(self):
        if Button.locked == False:
            d1 = Button(random.randrange(1-6))

        