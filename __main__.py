from menu import Menu
from game import Game
from control import Control
from settings import settings

import pygame as pg
import sys

pg.init()
pg.font.init()

app = Control(**settings)
state_dict = {
    'menu': Menu(),
    'game': Game()
}

app.setup_states(state_dict, 'menu')
app.main_game_loop()
pg.quit()
sys.exit()