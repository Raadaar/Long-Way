import sys
import pygame as pg
import os
from datetime import datetime

cr_data = datetime.now().second
fps = 0

pg.font.init()
pg.init()


win = pg.display.set_mode((1360, 768))
pg.display.set_caption("Map editor 'Long Way'")

pg.GL_ACCELERATED_VISUAL = 1
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

    def move(self, vector):
        self.rect[0] += vector[0]
        self.rect[1] += vector[1]

    def draw(self):
        ##  Игрок на самом окне не двигается, двигается мир вокруг него
        pg.draw.rect(win, (0, 100, 0), (680, 384, 50, 50))
        #pg.draw.rect(win, (0, 100, 0), (240, 240, 10, 10))

class object:
    ##  Это какой-нибудь объект, отличный игрока (к примеру враг или дерево)
    def __init__(self, x, y, width, height, RGP=(255, 0, 0), spr=[], py=[]):
        self.rect = pg.Rect(x, y, width, height)
        self.RGP = RGP
        self.sprait = spr
        self.py_sprai = py
    def draw(self):
        ##  Чтобы отрисовка соответствовала позиции объекта его нужно отрисовывать
        ##  на self.rect[0]-camera.rect[0], self.rect[1]-camera.rect[1]
        if self.sprait == []:
            pg.draw.rect(win, self.RGP, (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1], self.rect[2], self.rect[3]), 2)
        else:
            for i in self.sprait:
                win.blit(i, (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1]))
    def vns(self):
        objects.append(sam_object(self.rect[0], self.rect[1], self.rect[2], self.rect[3]))
    def dop(self, v):
        self.sprait = [*self.sprait, v[0]]
        self.py_sprai = [*self.py_sprai, v[1]]
class sam_object:
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)
    def draw(self):
        ##  Чтобы отрисовка соответствовала позиции объекта его нужно отрисовывать
        ##  на self.rect[0]-camera.rect[0], self.rect[1]-camera.rect[1]
        pg.draw.rect(win, (255, 0, 0), (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1], self.rect[2], self.rect[3]))
    def vns(self):
        print('f')
#objects = [object(250, 250, 30, 30)]
fail = [[pg.image.load(sys.path[0] + f"\\aset\\{i}"), f"\\aset\\{i}"] for i in os.listdir('\prog\Long Way\\aset') if '.png' in i]
class archive_image:
    def __init__(self, image_arh):
        self.image_arh = image_arh
        fail_in = []
        x__ = 0
        y__ = 0 
        xis = 0
        for _ in range(7):
            x__ += 25
            for _ in range(13):
                y__ += 25
                if xis == len(fail) - 1:
                    fail_in.append(object(y__, x__, 50 ,50 , spr=[fail[xis][0],], py=fail[xis][1]))
                    xis = -1
                    break
                else:
                    fail_in.append(object(y__, x__, 50 ,50 , spr=[fail[xis][0],], py=fail[xis][1]))
                xis += 1
                y__ += 50
            if xis == -1:
                break
            y__ = 0
            x__ += 50
        self.image_arh_obj = fail_in
    def render(self):
        for i in self.image_arh_obj:
            for d in i.sprait:
                win.blit(pg.transform.scale(d, (i.rect[2], i.rect[3])), (i.rect[0], i.rect[1]))
fail = archive_image(fail)
player = Player(0, 0)
camera = cam(0, 0)
clock = pg.time.Clock()
objects = []
x_ = 350 #int(input('Ширина карты '))
y_ = 350 #int(input('Высота карты '))
tra = pg.image.load(sys.path[0] + "\\aset\\tra.png").convert()
l = pg.image.load(sys.path[0] + "\\aset\\icon.png").convert()
for x in range(x_):
    for y in range(y_):
        objects.append(object(x * 50, y * 50, 50, 50))
        #objects.append(object(x * -50, y * -50, 50, 50))
vs_pr = [tra, "\\aset\\tra.png"]
pok = False
speed = 5
mouse_cursor = ((win.get_width() - l.get_width())/2, (win.get_height() - l.get_height())/2)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key == pg.K_z:
                print(camera.rect[0], camera.rect[1])
            if event.key == pg.K_ESCAPE:
                if pok == True:
                    pok = False
                else:
                    pok = True
            if event.key == 13:
                
                for i in objects:
                    if len(i.sprait) > 0:    
                        print(f'{("_").join(i.py_sprai)} {i.rect[0]}_{i.rect[1]}_{i.rect[2]}_{i.rect[3]}')            
                pg.quit()
                sys.exit()
                name_map = 'game\\' + input('Название карты ')+'.txt'
                with open(name_map, 'w', encoding='utf-8') as file:
                    for i in objects:
                        if len(i.sprait) > 0:
                            s = f'{("_").join(i.py_sprai)} {i.rect[0]}_{i.rect[1]}_{i.rect[2]}_{i.rect[3]}\n'
                            file.writelines(s)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  #  левая кнопка мыши
                doMove = True
            if event.button == 3:  # правая кнопка мыши
                doMove = False
            x, y = pg.mouse.get_pos()
            x -= l.get_width()/2
            y -= l.get_height()/2
            if pok == False:
                for obj in objects:
                    if isinstance(obj, object):
                        if obj.rect.colliderect(pg.Rect((x + 25) + camera.rect[0], (y + 25) + camera.rect[1], 1, 1)):
                            if event.button == 1:
                                if vs_pr not in obj.sprait:
                                    obj.dop(vs_pr)
                            else:
                                if len(obj.sprait) > 0:
                                    obj.sprait.pop()
            else:
                for obj in fail.image_arh_obj:
                    if obj.rect.colliderect(pg.Rect((x + 25), (y + 25), 1, 1)):
                        vs_pr[0] = obj.sprait[-1]
                        vs_pr[1] = obj.py_sprai[-1]
            #objects.append(object((x + 25) + camera.rect[0], (y + 25) + camera.rect[1], 5, 5, RGP=(0, 0, 255)))
    kpressed = pg.key.get_pressed()
    vector = [0, 0]
# считывем движения

    if kpressed[pg.K_UP]:
        vector[1] -= speed
    elif kpressed[pg.K_DOWN]:
        vector[1] += speed
    if kpressed[pg.K_LEFT]:
        vector[0] -= speed
    elif kpressed[pg.K_RIGHT]:
        vector[0] += speed
    ##  Если игрок ходил
    if vector != [0, 0]:
        player.move(vector)
        camera.move(vector)
# делаем фон карты белым
    win.fill((255, 255, 255))
    if False:
        for obj in objects:
            if obj.rect.colliderect(camera.rect):
                obj.draw()
    [obj.draw() for obj in objects if obj.rect.colliderect(camera.rect)]
    #map(.draw, filter(lambda obj: obj.rect.colliderect(camera.rect), objects))
    player.draw()
    fps += 1
    if fps == 144:
        fps = 143
    if cr_data != datetime.now().second:
        cr_data = datetime.now().second
        print(fps)
        fps = 0
    #win.blit(pg.transform.scale(fail[2], (50, 50)), (500, 500))
    if pok == True:
        fail.render()
    #win.blit(fail[4], (0, 0))
    pg.display.flip() ##    = pg.display.update()
    clock.tick(60)
    #pg.time.wait(1)