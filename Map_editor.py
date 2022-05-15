import sys
import pygame as pg
import os
from datetime import datetime


cr_data = datetime.now().second
fps = 0
fps_pro = 0
execution = False
pg.font.init()
pg.init()
#prob_ = pg.Surface((1360, 768), flags=pg.SRCALPHA)
surface = 1 # 1, 2, 3 тип поверхности, пол, середина, потолок

win = pg.display.set_mode((1360, 768))#, flags=pg.SRCALPHA)
pg.display.set_caption("Map editor 'Long Way'")
f0 = pg.font.Font(sys.path[0] + "\\Fonts\\Gabriola One.ttf", 28)

sl_2 = []

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
        self.surface = ['', '', '']
        self.execution = False
        self.dop_sprait = []
    def draw(self):
        ##  Чтобы отрисовка соответствовала позиции объекта его нужно отрисовывать
        ##  на self.rect[0]-camera.rect[0], self.rect[1]-camera.rect[1]
        if str(set(self.surface)) != "{''}":
            if isinstance(self.surface[0], pg.Surface):
                win.blit(self.surface[0], (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1])) 
            if isinstance(self.surface[1], pg.Surface):
                #win.blit(self.surface[surface], (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1]))
                if self.execution != execution:
                    self.execution = True if execution == False else False
                else:
                    sl_2.append([self.surface[1], self.rect])
                #prob_.blit(self.surface[0], (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1])) 
        else:
            pg.draw.rect(win , self.RGP, (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1], self.rect[2], self.rect[3]), 2)
        for i in self.dop_sprait:
            if i.execution == execution:
                i.execution = True if execution == False else False
            else:
                sl_2.append([i.surface[1], i.rect])
    def dop(self, v):
        self.surface[surface - 1] = v[0]
#objects = [object(250, 250, 30, 30)]
fail = [[pg.image.load(sys.path[0] + f"\\aset\\{i}").convert_alpha(), f"\\aset\\{i}"] for i in os.listdir('\prog\Long Way\\aset') if '.png' in i]
tra = pg.image.load(sys.path[0] + f"\\aset\\tra.png").convert()
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

#from script.multip import division_of_work
fail = archive_image(fail)
player = Player(0, 0)
camera = cam(0, 0)
clock = pg.time.Clock()
objects = []
x_ = 100 #int(input('Ширина карты '))
y_ = 100 #int(input('Высота карты '))
tra = pg.image.load(sys.path[0] + "\\aset\\tra.png").convert()
l = pg.image.load(sys.path[0] + "\\aset\\icon.png").convert()
class big_chunk:
    def __init__(self, x, y, width=5000, height=5000) -> None:
        self.rect = pg.Rect(x, y, width, height)
        self.compound = (middle_chunk(x, y), middle_chunk(x + 2500, y), middle_chunk(x, y + 2500), middle_chunk(x + 2500, y + 2500))
class middle_chunk:
    def __init__(self, x, y, width=2500, height=2500) -> None:
        self.rect = pg.Rect(x, y, width, height)
        self.compound = (small_chunk(x, y), small_chunk(x + 1250, y), small_chunk(x, y + 1250), small_chunk(x + 1250, y + 1250))
class small_chunk:
    def __init__(self, x, y, width=1250, height=1250) -> None:
        self.rect = pg.Rect(x, y, width, height)
        self.compound = []
        for x_para in range(25):
            for y_para in range(25):
                self.compound.append(object(x + x_para * 50, y + y_para * 50, 50, 50)) #, spr=(tra, )
        self.compound = tuple(self.compound)   
prop_objects = []
for x in range(x_ // 100):
    for y in range(y_ // 100):
        prop_objects.append(big_chunk(x * 5000, y * 5000))
def otr():
    x = []
    for i in prop_objects:
        if i.rect.colliderect(camera.rect):
            for d in i.compound:
                if d.rect.colliderect(camera.rect):
                    for v in d.compound:
                        if v.rect.colliderect(camera.rect):
                            [(obj.draw(), faj.append(obj)) for obj in v.compound if obj.rect.colliderect(camera.rect)]
                            if False:
                                for ob in v.compound:
                                    x.append(ob)
                                    ob.draw()
    return x
def recursion_otr(spis, ind):
    if isinstance(spis[0], object):
        [(obj.draw(), faj.append(obj)) for obj in spis if obj.rect.colliderect(camera.rect)]
        #[([obj.draw(surface=i) for i in range(3)], faj.append(obj)) for obj in [obj for obj in spis if obj.rect.colliderect(camera.rect)]]
        return
    elif spis[ind].rect.colliderect(camera.rect):
        recursion_otr(spis[ind].compound, 0)
    ind += 1
    if ind == len(spis):
        return
    return recursion_otr(spis, ind)
#[ob.draw() for ob in [v for v in [d for d in [i for i in prop_objects if i.rect.colliderect(camera.rect)][0].compound if d.rect.colliderect(camera.rect)][0].compound if v.rect.colliderect(camera.rect)] if ob.rect.colliderect(camera.rect)]
if False:
    for x in range(x_):
        for y in range(y_):
            objects.append(object(x * 50, y * 50, 50, 50))
            #objects.append(object(x * -50, y * -50, 50, 50))
vs_pr = [tra, "\\aset\\tra.png"]

vaj = []
pok = False
speed = 5
faj = []
mouse_cursor = ((win.get_width() - l.get_width())/2, (win.get_height() - l.get_height())/2)
min_max = [300, 0]
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print(f'Минамальный фпс - {min_max[0]}')
            print(f'Максимальный фпс - {min_max[1]}')
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key == pg.K_z:
                print(sl_2)
            if event.key == pg.K_ESCAPE:
                if pok == True:
                    pok = False
                else:
                    pok = True
            if event.key == 13:
                
                for i in objects:
                    if len(i.sprait) > 0:    
                        print(f'{("_").join(i.py_sprai)} {i.rect[0]}_{i.rect[1]}_{i.rect[2]}_{i.rect[3]}')            
     
                
                data = [[], ]
                for i in prop_objects:
                    data_str = [[i.rect[0], i.rect[1], i.rect[2],  i.rect[3]], ]
                    for d in i.compound:
                        data_str.append([d.rect[0], d.rect[1], d.rect[2], d.rect[3]])
                        for v in d.compound:
                            data_str.append([v.rect[0], v.rect[1], v.rect[2], v.rect[3]])
                            peremen_0 = [[[obj.rect[0], obj.rect[1], obj.rect[2], obj.rect[3], ('_').join(obj.py_sprai)], data[0].extend(obj.py_sprai)] for obj in v.compound if len(obj.py_sprai) > 0] # 
                            for peremen_1 in peremen_0:
                                data_str.append(peremen_1[0])
                    print(data_str)
                    data.append(('_').join([(', ').join([str(d) for d in i]) for i in data_str]))
                data[0] = list(set(data[0]))
                name_map = input('Название карты ') + '.txt'
                with open(name_map, 'w', encoding='utf-8') as file:
                    file.writelines((' ').join([('_').join(data[0]), str(len(data) - 1)]) + '\n')
                    for s in data[1:]:
                        file.writelines(str(s) + '\n')
                pg.quit()
                sys.exit()
            if event.key == pg.K_1:
                surface = 1
            elif event.key == pg.K_2:
                surface = 2
            elif event.key == pg.K_3:
                surface = 3
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  #  левая кнопка мыши
                doMove = True
            if event.button == 3:  # правая кнопка мыши
                doMove = False
            x, y = pg.mouse.get_pos()
            x -= l.get_width()/2
            y -= l.get_height()/2
            if pok == False:

                for obj in faj:
                    if isinstance(obj, object):
                        odj_r = pg.Rect(obj.rect[0] - camera.rect[0], obj.rect[1] - camera.rect[1], obj.rect[2], obj.rect[3])
                        if odj_r.colliderect(pg.Rect(x + 25,  y + 25, 1, 1)):
                            if event.button == 1:
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
    sl_2 = []
# делаем фон карты белым
    win.fill((255, 255, 255))
    #sur_0.fill((255, 255, 255))
    if False:
        for obj in objects:
            if obj.rect.colliderect(camera.rect):
                obj.draw()
    faj = []
    #faj = otr()
    [recursion_otr(i.compound, 0) for i in prop_objects if i.rect.colliderect(camera.rect)]
    [win.blit(i[0], (i[1][0] - camera.rect[0], i[1][1] - camera.rect[1])) for i in sl_2] #(i[0].get_width() - i[1][0] - camera.rect[0], i[0].get_height() - i[1][1] - camera.rect[1])
    #x -= l.get_width()/2 i[0].get_width() - 
    #y -= l.get_height()/2 i[0].get_height() - 
    #[obj.draw(surface=2) for obj in faj]
    #[obj.draw() for obj in objects if obj.rect.colliderect(camera.rect)]
    #map(.draw, filter(lambda obj: obj.rect.colliderect(camera.rect), objects))
    player.draw()
    #win.blit(prob_, (0 , 0))
    fps += 1
    if fps == 300:
        fps = 299
    win.blit(f0.render(str(fps_pro), True, (23, 128, 109)), (0, 0))
    nis = datetime.now().second
    if cr_data != nis:
        cr_data = nis
        fps_pro = fps
        if fps_pro < min_max[0]:
            min_max[0] = fps_pro
        elif fps_pro > min_max[1]:
            min_max[1] = fps_pro
        fps = 0
    execution = True if execution == False else False
    #win.blit(pg.transform.scale(fail[2], (50, 50)), (500, 500))
    pg.draw.rect(win, (0, 0, 0), (x + 25,  y + 25, 5, 5) , 5)
    win.blit(f0.render(str(surface), True, (47, 79, 79)), (1332, 740))
    #pg.draw.rect(win, (0, 0, 0), (x + 25 - player.rect[0] + camera.rect[0], y + 25 + player.rect[1] - camera.rect[1], 5, 5), 5)
    if pok == True:
        fail.render()
    #win.blit(fail[4], (0, 0))
    #pg.display.update()
    pg.display.flip() ##    = pg.display.update()
    clock.tick(300)
    pg.time.wait(1)