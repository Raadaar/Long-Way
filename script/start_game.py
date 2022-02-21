import script.guide
import sys
from random import randint
# sys.path[0]
import pygame as pg

pg.font.init()
pg.init()
win = pg.display.set_mode((1360, 768))
icon = pg.image.load(script.guide.path + "\\aset\\icon.png").convert()
pg.display.set_icon(icon)
f1 = pg.font.Font(script.guide.path + "\\Fonts\\Gabriola One.ttf", 26)