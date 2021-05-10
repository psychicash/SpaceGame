from player import Player
from state import States

import pygame as pg

class Game(States):
    def __init__(self):
        States.__init__(self)

        self.next = 'menu'
    def cleanup(self):
        print('cleaning up Game state stuff')
    def startup(self):
        self.player = Player()
        print('starting Game state stuff')
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                # Up
                self.player.pos.y += 1
            elif event.key == pg.K_s:
                # Down
                self.player.pos.y += 1
            elif event.key == pg.K_a:
                # Left
                self.player.pos.x += -1
            elif event.key == pg.K_d:
                # Right
                self.player.pos.x += 1
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True
    def update(self, screen, dt):
        self.player.draw(screen)
        self.draw(screen)
    def draw(self, screen):
        screen.fill((0,0,255))