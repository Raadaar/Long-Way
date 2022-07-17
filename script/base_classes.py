#if __name__ == '__main__':
import random
from script.start_game import win, pg
import script.guide
pleer = pg.image.load(script.guide.path + "\\aset\\pleer.png").convert_alpha()
class cam:
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, 1360, 768)
        #self.rect = pg.Rect(x, y, 1360, 768)

    def move(self, vector):
        self.rect[0] += vector[0]
        self.rect[1] += vector[1]

class Player:
    def __init__(self, x, y):
        self.rect = pg.Rect(x, y, 10, 10)
        self.route = 'down'
        self.hero_atlas = [[], [], [], []]
        self.hero_atlas_ = {'down': 0, 'left': 1, 'right': 2, 'up': 3}
        self.hero_test_area = {'down': (0, 50, 50, 100), 'left': (-100, 0, 100, 50), 'right': (50, 0, 100, 50), 'up': (0, -100, 50, 100)}
        self.vpr = 1
        for x in range(len(self.hero_atlas)):
            for y in range(3):
                c = pg.Surface((50, 50), flags=pg.SRCALPHA)
                c.blit(pleer, (y * -50, x * -50, 50, 50))
                self.hero_atlas[x].append(c)

    def move(self, vector, fps):
        if fps % 10 == 0:
            self.vpr = self.vpr + 1 if self.vpr < 2 else 0
        self.rect[0] += vector[0]
        self.rect[1] += vector[1]

    def test_area(self):    
        b = self.hero_test_area[self.route]
        return pg.Rect(680 + b[0], 384 + b[1], self.rect[2] + b[2], self.rect[3] + b[3])
    def draw(self):
        ##  Игрок на самом окне не двигается, двигается мир вокруг него
        #pg.draw.rect(win, (0, 100, 0), (680, 384, 50, 50))
        win.blit(self.hero_atlas[self.hero_atlas_[self.route]][self.vpr], (680, 384, 50, 50))
        #win.blit(self.hero_atlas[0][1], (680, 384, 50, 50))
        #pg.draw.rect(win, (0, 100, 0), (240, 240, 10, 10))
camera = cam(0,0)
player = Player(0,0)
class object:
    ##  Это какой-нибудь объект, отличный игрока (к примеру враг или дерево)
    def __init__(self, x, y, width, height, RGP=(255, 0, 0), spr=[], py=[]):
        self.rect = pg.Rect(x, y, width, height)
        self.RGP = RGP
        self.sprait = spr
    def draw(self):
        ##  Чтобы отрисовка соответствовала позиции объекта его нужно отрисовывать
        ##  на self.rect[0]-camera.rect[0], self.rect[1]-camera.rect[1]
        if self.sprait == []:
            pg.draw.rect(win, self.RGP, (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1], self.rect[2], self.rect[3]), 2)
        else:
            for i in self.sprait:
                win.blit(i, (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1]))
