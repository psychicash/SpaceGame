from colors import *
from vector import Vector

import pygame as pg

class Player:
    def __init__(self):
        self.pos = Vector(0, 0)
        self.dir = 0
        self.vel = Vector(0, 0)
        self.color = cyan # Change to texture later
    
    def update(self):
        pass

    def draw(self, screen):
        pg.draw.line(screen, self.color, (60, 80), (130, 100))
        pg.display.flip()

    def rotate(self, screen):
        pass