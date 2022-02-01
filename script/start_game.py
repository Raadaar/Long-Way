import os
import sys
from random import randint

import pygame as pg

pg.font.init()
pg.init()
win = pg.display.set_mode((1360, 768))
icon = pg.image.load(sys.path[0] + "\\aset\\icon.png").convert()
pg.display.set_icon(icon)
f1 = pg.font.Font(sys.path[0] + "\\Fonts\\Gabriola One.ttf", 26)