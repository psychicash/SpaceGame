from state import States
from colors import *
from settings import settings

import pygame as pg
import sys

class Menu(States):
    def __init__(self):
        States.__init__(self)
        self.font_size = 32
        self.font = pg.font.Font('freesansbold.ttf', self.font_size)
        self.next = 'game'
        self.selected = 0
        self.menu_items = [(self.start, "Start"), (self.exit, "Exit")]
    def cleanup(self):
        print('cleaning up Menu state stuff')
    def startup(self):
        print('starting Menu state stuff')
    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                self.selected = (self.selected - 1) % len(self.menu_items)
            elif event.key == pg.K_s:
                self.selected = (self.selected + 1) % len(self.menu_items)
            elif event.key == pg.K_RETURN:
                self.menu_items[self.selected][0]()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.selected = (self.selected + 1) % len(self.menu_items)
            elif event.button == 5:
                self.selected = (self.selected - 1) % len(self.menu_items)
    def exit(self):
        pg.display.quit()
        pg.quit()
        sys.exit()
    def start(self):
        self.done = True
    def update(self, screen, dt):
        self.draw(screen)
    def draw(self, screen):
        for idx, (_, text) in enumerate(self.menu_items):
            bg = white if self.selected == idx else blue
            fg = red if self.selected == idx else green
            text = self.font.render(text, True, fg, bg)
            text_rect = text.get_rect()
            x, y = settings['size']
            text_rect.center = (x // 2, y // 2 + idx * self.font_size)
            screen.blit(text, text_rect)
        # screen.fill((255,0,0))