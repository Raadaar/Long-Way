from math import e
import os
import sys
from random import randint

import pygame as pg

pg.font.init()
pg.init()
win = pg.display.set_mode((1360, 768))
# Название игры
pg.display.set_caption('Long Way')
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
    def __init__(self, x, y, width, height):
        self.rect = pg.Rect(x, y, width, height)

    def draw(self):
        ##  Чтобы отрисовка соответствовала позиции объекта его нужно отрисовывать
        ##  на self.rect[0]-camera.rect[0], self.rect[1]-camera.rect[1]
        pg.draw.rect(win, (255, 0, 0), (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1], self.rect[2], self.rect[3]), 2)
# фунцкия для отображение фоновых спрайтов и дополнительно оболочек для колизии этих спрайтов
def floor(m, v1, v2, o, horizon=False):
    # m = карта, v1, v2 = camera.rect[0], camera.rect[1], horizon выбор спрайтов, False пола(земля, дорога), True поверх пола(деревья, дома)
    if horizon == False:
        x_ = 0
        y_ = 0
        for i in range(len(m)):
            x_ = 0
            for d in range(len(m[i])):
                b = pg.Rect(x_, y_, 50, 50)
                if b.colliderect(camera.rect):
                #if v1 - 50 < x_ < v1 + 1360 and v2 - 50 < y_ < v2 + 768:
                    if m[i][d] == '*':
                        win.blit(tra, (x_ - v1, y_ - v2))
                    elif m[i][d] == '^':
                        win.blit(dor, (x_ - v1, y_ - v2))
                    if m[i][d] == '$':
                        win.blit(tra, ((x_) - v1, (y_ ) - v2))
                    elif m[i][d] == '*!':
                        win.blit(tra, (x_ - v1, y_ - v2))
                        win.blit(tra1[(o) // 24], (x_ - v1, y_ - v2))
                x_ += 50
            y_ += 50 
    elif horizon == True:
        spic = [(0, 0, 0, 0)]      
        x_ = 0
        y_ = 0
        for i in range(len(m)):
            x_ = 0
            for d in range(len(m[i])):
                b = pg.Rect(x_, y_, 50, 50)
                c = pg.Rect(camera.rect[0] - 100 , camera.rect[1] - 100, camera.rect[2] + 200, camera.rect[3] + 200)
                if b.colliderect(c):
                    if m[i][d] == '$':
                        win.blit(dre, ((x_) - v1, (y_ - 100) - v2))
                        #spic.append([(x_) - v1, (y_ - 100) - v2])
                    elif m[i][d] == '!':
                        win.blit(tra, (x_ - v1, y_ - v2))
                        spic.append(pg.Rect((x_ - v1) - 40, (y_ - v2) - 40, 90, 90)) # нужно допольнительно отнимать 40 и 90, дабы был чёткий квадрат
                x_ += 50
            y_ += 50
        return spic
# делаем слепки обьектов, наверное) 
player = Player(0, 0)
camera = cam(0, 0)
# "D:/prog/game/aset/derevo.png"
objects = [object(250, 250, 30, 30)]
# Загрузка спрайтов
#dre = pg.Surface((100, 200), flags=pg.SRCALPHA)
# "D:/prog/game/aset/dre.png")
men_iven =  [pg.image.load(sys.path[0] + "\\aset\\men\\men_ive_items.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\men_ive_equipment.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\men_ive_important.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\men_ive.png").convert_alpha()]
ramka = pg.image.load(sys.path[0] + "\\aset\\men\\ramka.png").convert_alpha()
dre = pg.image.load(sys.path[0] + "\\aset\\dre.png").convert_alpha()
pla = pg.image.load(sys.path[0] + "\\aset\\pla.png").convert()
dereo = pg.image.load(sys.path[0] + "\\aset\\derevo.png").convert_alpha()
icon = pg.image.load(sys.path[0] + "\\aset\\icon.png").convert()
pg.display.set_icon(icon)
dor = pg.image.load(sys.path[0] + "\\aset\\dor.png").convert_alpha()
pla = pg.image.load(sys.path[0] + "\\aset\\pla.png").convert_alpha()
pleer = pg.image.load(sys.path[0] + "\\aset\\pleer.png").convert_alpha()
inte = pg.image.load(sys.path[0] + "\\aset\\men\\Back.png").convert_alpha()
# Трава
battle_sprait_men = [pg.image.load(sys.path[0] + "\\aset\\men\\oc_m_b.png").convert_alpha()]
# sac_b_les
battle_sprait = [pg.image.load(sys.path[0] + "\\aset\\men\\sac_b_les.png").convert_alpha()]
#
battle_sprait_vragi = [pg.image.load(sys.path[0] + "\\aset\\men\\vrag.png").convert_alpha()] 
#
battle_ramka_g = [pg.image.load(sys.path[0] + "\\aset\\men\\ramka_g_m_b.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\ramka_p_sc.png").convert_alpha()]
#
tra = pg.image.load(sys.path[0] + "\\aset\\tra1.png").convert()
tra1 = [pg.image.load(sys.path[0] + f"\\aset\\GuttyKreumNatureTilesvol1_v2\\AnimationFrames\\Flower\\flower32x32transparentanimated{i}.png").convert_alpha() for i in range(1, 14)]
#
vi = pg.image.load(sys.path[0] + "\\aset\\men\\vi.png").convert_alpha()
#
men_sn_ok = [pg.image.load(sys.path[0] + "\\aset\\men\\oc_okn.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\dop_okn.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\dop_okn_n.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\dop_okn_v.png").convert_alpha()]
#
ramk = pg.image.load(sys.path[0] + "\\aset\\men\\ramka_e.png").convert_alpha()
ramk_ = pg.image.load(sys.path[0] + "\\aset\\men\\ramka_m.png").convert_alpha()
#
f0 = pg.font.Font(sys.path[0] + "\\Fonts\\HATTEN.ttf", 20)
f1 = pg.font.Font(sys.path[0] + "\\Fonts\\Gabriola One.ttf", 26)
text1 = f1.render('Игра ещё не готова, что ты тут делаешь?', True, (0, 180, 0))
animation_set = [pg.image.load(sys.path[0] + f"\\aset\\GuttyKreumNatureTilesvol1_v2\\AnimationFrames\\Bush/bush32x32transparentanimated{i}.png").convert_alpha() for i in range(1, 14)]
meny = [pg.image.load(sys.path[0] + "\\aset\\men\\Back.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\Items.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\Quests.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\Equipment.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\Saving.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\Loading.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\Exit.png").convert_alpha()]
# Загрузка карты
Map_ = open("/prog/game/map/map.txt", 'r', encoding='utf-8')
Map = list(map(lambda x: x.split(), list(map(str.strip, Map_.readlines()))))
Map_.close()
# 
#GAME_FONT = pygame.freetype.Font("C:\Windows\Fonts\sylfaen.ttf", 24)
#
# Название, трата по мане, урон, тип, масовое или нет заклинание
list_spells = (('Магический удар', 2, 10, ('Воздушный'), False),
                 ('fairbol', 3, 9, ('Огненый', 'Воздушный'), True))
# Название, трата по очками способностей, тип, масовое или нет способность
list_adility = (('Удар с ноги', 1, 6, ('Пронзающий'), False),
                 ('Круговой удар', 2, 9, ('Дробящий'), True))
# inventory_class
class inventory_class:
    # Создаёт обект инвенторя, inve это лист, rasmer максимальная длина
    def __init__(self, inve, rasmer):
        #self.inv = inve, rasmer
        
        self.size = rasmer
        self.inventory = inve
    # создаёт новый сортированный список для отображения в инвенторе uslow = активная вкладка
    def sorti(self, uslow):
        #print(iventar.inv[0])
        sort_spik = []
        if uslow == 0:
            sor = ['Еда']
        elif uslow == 1:
            sor = ['Голова', 'Туловище', 'Ноги', 'Оружие', 'Щит', 'Кольцо_0', 'Кольцо_1', 'Кольцо_2']
        else:
            sor = ['Еда', 'Голова', 'Туловище', 'Ноги', 'Оружие', 'Щит', 'Кольцо_0', 'Кольцо_1', 'Кольцо_2']
        if uslow > 9:
            if uslow > 14:
                sor = ['Кольцо_0', 'Кольцо_1', 'Кольцо_2']
            else:
                sor = ibi[uslow % 10]
        for i in self.inventory:
            if i[0][1] in sor:
                sort_spik.append(i)
        return sort_spik
    # Добовляет предмет в инвентарь, если такой уже есть, добовляет к количеству существующего
    def dopov(self, pr):
        prov = False
        for i in range(len(self.inventory)):
            if self.inventory[i][0] == pr[0]:
                prov = True       
                self.inventory[i][1] += pr[1]
        if prov == False:
            self.inventory.append(pr)
    # Отрисовывает название вещей в инвенторе
    def otrisovka(self, spis):
        visata = 93
        dlina = 350
        perexod = 0
        for i in spis:
            perexod += 1
            if perexod == 3:
                dlina -= 10
            win.blit(f1.render(str(i[0][0]), True, (180, 0, 0)), (dlina, visata)) 
            dlina += 300
            if perexod == 1:
                dlina += 15
            elif perexod == 3:
                dlina -= 20
            win.blit(f1.render(str(i[1]), True, (180, 0, 0)), (dlina, visata))            
            dlina += 65
            if perexod == 1:
                dlina -= 15
            elif perexod == 3:
                perexod = 0
                visata += 25
                dlina = 350
predmeti = (('Яблоко', 'Еда', 3), ('Хлеб', 'Еда', 4),
            ('Ржавый мечь новичка', 'Оружие', [(('Атака', 3), ('Ловкость', 2)), (("Попадание", -5), ('Критическое', -5)), (('', ''), ('', ''))]),
            ('Ножик', 'Оружие', [(('Атака', 2), ('Ловкость', 1), ('Сноровка', 1)), (('Критическое', 5), ('Уворот', 5)), (('', ''), ('', ''))]),
            ('Кольчуга', 'Туловище', [(('Защита', 5), ('Ловкость', -1)), (('', ''), ('', '')), (('Пронзающий', 10), ('Стрелковый лёгкий', 40), ('Огненый', -20))]),
            ('Рубаха', 'Туловище', [(('Защита', 3), ('Ловкость', 1)), (('', ''), ('', '')), (('Огненый', -50), ('', ''))]),
            ('Шляпа', 'Голова', [(('Защита', 1), ('', '')),(('', ''), ('', '')), (('', ''), ('', ''))]),
            ('Кепка', 'Голова', [(('Ловкость', 1), ('', '')), (('Критическое', 5), ('Уворот', 10)), (('Дробящий', 5), ('', ''))]),
            ('Палка', 'Оружие', [(('Атака', 1), ('Ловкость', 1), ('Защита', 1)), (('Критическое', -10), ("Попадание", 30)), (('', ''), ('',''))]),
            ('Тапки', 'Ноги', [(('Сноровка', 2), ('Ловкость', 1)), (('', ''), ('', '')), (('Пронзающий', 10), ('Стрелковый лёгкий', 10), ('Огненый', -10))]),
            ('Сапоги', 'Ноги', [(('Ловкость', 1), ('Защита', 2)), (('', ''), ('', '')), (('Огненый', -10), ('', ''))]),
            ('Маг, к, с', 'Кольцо_0', [(('Магия', 3), ('', '')), (('', ''), ('', '')), (('', ''), ('', ''))]),
            ('Маг, к, л', 'Кольцо_1', [(('Ловкость', 3), ('', '')), (('', ''), ('', '')), (('', ''), ('', ''))]),
            ('Маг, к, з', 'Кольцо_2', [(('Защита', 3), ('', '')), (('', ''), ('', '')), (('', ''), ('', ''))]),
            ('Маг, к, в', 'Кольцо_0', [(('Воля', 3), ('', '')), (('', ''), ('', '')), (('', ''), ('', ''))]),
            ('Маг, к, с', 'Кольцо_1', [(('Сноровка', 3), ('', '')), (('', ''), ('', '')), (('', ''), ('', ''))]),
            ('Маг, к, а', 'Кольцо_2', [(('Атака', 3), ('', '')), (('', ''), ('', '')), (('', ''), ('', ''))]),
            )
iventar = inventory_class([], 33)
iventar.dopov([predmeti[1], 3])
iventar.dopov([predmeti[2], 1])
iventar.dopov([predmeti[3], 1])
iventar.dopov([predmeti[4], 1])
iventar.dopov([predmeti[5], 1])
iventar.dopov([predmeti[6], 1])
iventar.dopov([predmeti[7], 1])
iventar.dopov([predmeti[8], 1])
iventar.dopov([predmeti[9], 1])
iventar.dopov([predmeti[10], 1])
iventar.dopov([predmeti[11], 1])
iventar.dopov([predmeti[12], 1])
iventar.dopov([predmeti[13], 1])
iventar.dopov([predmeti[12], 1])
iventar.dopov([predmeti[13], 1])
iventar.dopov([predmeti[14], 1])
iventar.dopov([predmeti[15], 1])
iventar.dopov([predmeti[16], 1])
# 340 разница
# скорость персоонажа 
#
class Pleeer:
    def __init__(self, name, maxhp, maxmp, msp, ataka, pro, mag, wil, agil, dext,
        accuracy = 80, critic = 5, dodg = 5, mag_dodge = 0, counte_str = 0, counte_str_mag = 0,
        cru = 100, cu = 100, pie = 100, sh_l = 100, sh_h = 100, ea = 100, wa = 100, fi = 100,
        ai = 100, lig = 100, da = 100):
        #0 Имя игрока незнаю зачем нужно, ведь в сюжете оно не будет использоватся, но если что вырежу
        self.name = name
        #1 Хп что на данный момент имеется у игрока
        self.HP = maxhp
        #2 Мана что на данный момент имеется у игрока
        self.MP = maxmp
        #3 Очки способностей что на данный момент имеются у игрока
        self.SP = 0
        #4 Максимальное возможное количество хп у игрока
        self.MaxHP = maxhp
        #5 Максимальное возможное количество маны у игрока
        self.MaxMP = maxmp
        #6 Максимальное возможное количество очков способностей у игрока
        self.MaxSP = msp
        #=-\
            # Характиристики        
        #7 Урон что будет сумироватся с оружием
        #8 Защита, будет сумироватся с бронёй
        #9 Магический урон, будет сумироватся с эфектом заклинания: Защитой, Уроном и т.д
        #10 Воля, наверное самая редко используемая характеристка, будет влиять на контроль и испуг
        #11 Ловкость будет влиять на те или иные способности 
        #12 Сноровка, будет влиять на шанс наподения противников опять таки возможно на те или иные способности
        #=-/
        self.specifications = {'Атака': ataka, 'Защита': pro, 'Магия': mag, 'Воля': wil, 'Ловкость': agil, 'Сноровка': dext}
        #=-\
            # Шансы       
        #13 Шанс попадание атакой, комисия по балансу игры ещё решает будет ли это влиять на заклинания
        #14 Шанс критического попадания тут всё понятно, скорее всего будет в двое меньшем шансе работать на способности # Способности всё ещё в разработке
        #15 Шанс уворота от атак/способностей
        #16 Шанс уворота от заклинаний
        #17 Шанс контр атаки/способности 
        #18 Шанс контр заклинании
        #=-/
        self.chances = {"Попадание": accuracy, 'Критическое': critic, 'Уворот': dodg, 'Магический уворот': mag_dodge, 'Контр атака': counte_str, 'Контр заклинание': counte_str_mag}
        #=-\
            # Сопротивления        
        #19 Дробящее сопротивление
        #20 Режущее сопротивление
        #21 Пронзающее сопротивление
        #22 Стрелковое лёгкое сопротивление
        #23 Стрелковое тяжолое сопротивление
        #24 Земляное сопротивление
        #25 Водное сопротивление
        #26 Огненое сопротивление
        #27 Воздушное сопротивление
        #28 Святое сопротивление
        #29 Тёмное сопротивление
        #=-/
        # Словарь сопротивлений
        self.resistance = {'Дробящий': cru, 'Режущий': cu, 'Пронзающий': pie, 'Стрелковый лёгкий': sh_l,
         'Стрелковый тяжолый': sh_h, 'Земленой': ea, 'Водный': wa, 'Огненый': fi, 'Воздушный': ai,
         'Святой': lig, 'Тёмный': da}
        # Словарь заклинаний
        self.spells = {}
        # Словарь способностей
        self.adility = {}
        # Оружие и вещи
        self.items = {'Голова': ('', '', [(('', ''), ('', '')),(('', ''), ('', '')),(('', ''), ('', ''))]), 'Туловище': ('', '', [(('', ''), ('', '')),(('', ''), ('', '')),(('', ''), ('', ''))]), 'Ноги': ('', '', [(('', ''), ('', '')),(('', ''), ('', '')),(('', ''), ('', ''))]),
         'Оружие': ('', '', [(('', ''), ('', '')),(('', ''), ('', '')),(('', ''), ('', ''))]), 'Щит': ('', '', [(('', ''), ('', '')),(('', ''), ('', '')),(('', ''), ('', ''))]), 'Кольцо_0': ('', '', [(('', ''), ('', '')),(('', ''), ('', '')),(('', ''), ('', ''))]),
          'Кольцо_1': ('', '', [(('', ''), ('', '')),(('', ''), ('', '')),(('', ''), ('', ''))]), 'Кольцо_2': ('', '', [(('', ''), ('', '')),(('', ''), ('', '')),(('', ''), ('', ''))])}
    # Функция надевание и снимание вещей
    def don(self, inven, don):
        # Удаляет старые характиристики
        for i in self.items[inven[0][1]][2][0]:
            if i[0] in [i for i in self.specifications.keys()]:
                self.specifications[i[0]] -= i[1]
        for i in self.items[inven[0][1]][2][1]:
            if i[0] in [i for i in self.chances.keys()]:
                self.chances[i[0]] -= i[1]        
        for i in self.items[inven[0][1]][2][2]:
            if i[0] in [i for i in self.resistance.keys()]:
                self.resistance[i[0]] -= i[1]
        # добовляет новые
        for i in inven[0][2][0]:
            if i[0] in [i for i in self.specifications.keys()]:
                self.specifications[i[0]] += i[1]
        for i in inven[0][2][1]:
            if i[0] in [i for i in self.chances.keys()]:
                self.chances[i[0]] += i[1]        
        for i in inven[0][2][2]:
            if i[0] in [i for i in self.resistance.keys()]:
                self.resistance[i[0]] += i[1]
        # Если предмета у игрока не было
        if self.items[inven[0][1]][0] != '':
            iventar.dopov([self.items[inven[0][1]], 1])
        del iventar.inventory[iventar.inventory.index(inven)]
        self.items[inven[0][1]] = inven[0]
#
def attack(attacking, attacked):
    if randint(0, attacking.chances["Попадание"]) > attacked.chances['Уворот']:
        if randint(0, 100) <= attacking.chances['Критическое']:
            damage = randint(round(attacking.specifications['Атака'] * 1.5), round(attacking.specifications['Атака'] * 2.5))
            if damage > attacked.specifications['Защита']:
                damage -= attacked.specifications['Защита']
            else:
                damage = 0
        else:
            damage = randint(attacking.specifications['Атака'] // 2, attacking.specifications['Атака'])
            if damage > attacked.specifications['Защита']:
                damage -= attacked.specifications['Защита']
            else:
                damage = 0
        print(damage)
        attacked.HP -= damage
    else:
        damage = 'Промах'
    return damage
#
def attack_magic(attacking, spe, attacked):
    attacking.MP -= spe[1]
    if randint(0, 100) > attacked.chances['Магический уворот']:
        if type(spe[3]) == tuple:
            damage = round((randint(round(spe[2] / 1.5), spe[2]) / 100) * sum([attacked.resistance[i] for i in spe[3]]) // len(spe[3]))
        else:
            damage = round((randint(round(spe[2] / 1.5), spe[2]) / 100) * attacked.resistance[spe[3]])
        attacked.HP -= damage
    else:
        damage = 'Магический промах'
    print(damage)
    return damage    
#
pleeer = Pleeer('Pler', 20, 10, 3, 5, 3, 2, 3, 5, 2)
vrag = Pleeer('Vrag', 20, 10, 3, 5, 3, 2, 3, 5, 2, dodg=30)
#
pleeer.spells[list_spells[0][0]] = list_spells[0]
pleeer.spells[list_spells[1][0]] = list_spells[1]
pleeer.adility[list_adility[0][0]] = list_adility[0]
pleeer.adility[list_adility[1][0]] = list_adility[1]
#
speed = 5
#
kno_m_s = 0
#
kno = 0
# Освещение кнопок в инвенторе и сортировки предметов
men_ive_kno = 0
# освещение вещей в инвенторе
v_m_p = [350, 93]
# выбор предмета в инвенторе
vpr_pr = 0
#
frame_coo = [0, 484]

# FPS

clock = pg.time.Clock()
#
battle_cycle = 0
# Включает главное меню
men_ive_gl = False
# Включает выбор вкладок в инвенторе
men_ive = False
# Включает выбор предметов в вкладке инвенторя
per_men_iv = False
# пустое значение
per_men_iv_pr = False
# Меню снарежения
men_sn = [False, # Активация снарежения
          False, # Активация выбора предмета в снарежение
          False] # Пустое значение
# Меню начала боя
per_re_batl = [False, # Проверка попадает ли игрок в зону боя, если да, то запускается радном по наподению врага
               False, # Запускается окно боя, и включается передвежение основеых кнопок
               False, # Происходить атака
               False, # Активируется рамка выбора магии
               False] # Активация магии
kno_battle = [1, 0]
# Список боевых зон
battle_son = [pg.Rect(0, 0, 300, 300)]

frame = 0
attack_delay = 0

ibi = ['Голова', 'Туловище', 'Ноги', 'Оружие', 'Щит', 'Кольцо_0', 'Кольцо_1', 'Кольцо_2']
while  1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                # Если включен выбор предмета выключает его, если меню инвенторя то его выключает
                if men_sn[1] == True:
                    men_sn[1] = False
                elif men_sn[0] == True:
                    men_ive_gl = True
                    men_sn[0] = False 
                elif per_men_iv == True:
                    per_men_iv = False
                elif men_ive == True:
                    men_ive = False
                # Включает меню, если включенно, выключает
                elif men_ive_gl == False:
                    men_ive_gl = True
                elif men_ive_gl == True:
                    men_ive_gl = False
                #
                if per_re_batl[3] == True:
                    per_re_batl[3] = False
                    kno_battle[1] = 0
                # 
                kno = 0
                men_ive_kno = 0
                v_m_p = [350, 93]
                vpr_pr = 0
            # Освещение кнопок в меню
            if event.key == pg.K_RIGHT:
                if men_ive == True and per_men_iv == False and men_sn[1] == False and men_ive_gl == True:
                    if men_ive_kno < 3:
                        men_ive_kno += 1
                        if men_ive_kno == 3:
                            men_ive_kno = 0
                # Освещение вкладок в меню инвенторя
                elif per_men_iv == True:
                    if v_m_p[0] < 1030:
                        v_m_p[0] += 340 
                    vpr_pr += 1
                elif men_sn[1] == True:
                    if frame_coo[0] < 1215:
                        frame_coo[0] += 135
                        kno_m_s += 1
                elif per_re_batl[3] == True:
                    kno_battle[1] += 1
                    if kno_battle[1] > 40:
                        kno_battle[1] -= 40
            if event.key == pg.K_LEFT:
                # Освещение вкладок инвенторя
                if men_ive == True and per_men_iv == False and men_sn[1] == False and men_ive_gl == True:
                    if men_ive_kno > -1:
                        men_ive_kno -= 1
                        if men_ive_kno == -1:
                            men_ive_kno = 2
                # Освещение вкладок предметов
                elif per_men_iv == True:
                    if v_m_p[0] > 350:
                        v_m_p[0] -= 340 
                    vpr_pr -= 1
                elif men_sn[1] == True:
                    if frame_coo[0] > 0:
                        frame_coo[0] -= 135
                        kno_m_s -= 1
                elif per_re_batl[3] == True:
                    kno_battle[1] -= 1
                    if kno_battle[1] < 0:
                        kno_battle[1] += 40
            if event.key == pg.K_UP:
                if men_ive_gl == True and per_men_iv == False:
                    kno -= 1
                    if kno < 0:
                        kno = 6
                if men_sn[0] == True and men_sn[1] == False:
                    kno -= 1
                    if kno < 0:
                        kno = 7                    
                # Освещение вкладок в меню инвенторя
                elif per_men_iv == True:
                    if v_m_p[1] > 75:
                        v_m_p[1] -= 25 
                    vpr_pr -= 3
                elif men_sn[1] == True:
                    if frame_coo[1] > 484:
                        frame_coo[1] -= 28
                        kno_m_s -= 10
                elif per_re_batl[1] == True and per_re_batl[3] == False:
                    kno_battle[0] -= 1
                    if kno_battle[0] < 1:
                        kno_battle[0] = 5
                elif per_re_batl[3] == True:
                    kno_battle[1] -= 4
                    if kno_battle[1] < 0:
                        kno_battle[1] += 40
            if event.key == pg.K_DOWN:
                if men_ive_gl == True and per_men_iv == False:
                    kno += 1
                    if kno > 6:
                        kno = 0
                if men_sn[0] == True and men_sn[1] == False:
                    kno += 1
                    if kno > 7:
                        kno = 0
                # Освещение вкладок в меню инвенторя
                elif per_men_iv == True:
                        if v_m_p[1] < 825:
                            v_m_p[1] += 25 
                        vpr_pr += 3
                elif men_sn[1] == True:
                    if frame_coo[1] < 752:
                        frame_coo[1] += 28
                        kno_m_s += 10
                elif per_re_batl[1] == True and per_re_batl[3] == False:
                    kno_battle[0] += 1
                    if kno_battle[0] > 6:
                        kno_battle[0] = 1
                elif per_re_batl[3] == True:
                    kno_battle[1] += 4
                    if kno_battle[1] > 40:
                        kno_battle[1] -= 40
        # Нужно всю это вереницу if-ов убрать навиг, в один и там проверят наличие тех, или иных активов
        # Активации кнопок, 13 = ENTER
            if event.key == 13: 
                if kno==6 and men_sn[0] == False:
                    pg.quit()
                    sys.exit()
                elif men_sn[0] == False:
                    if kno == 3:
                        men_sn[0] = True
                        men_ive_gl = False                
                    elif kno == 1:
                        men_ive = True
                    elif False:
                        men_ive_kno = 3
                    elif per_men_iv == True:
                        if -1 < vpr_pr < len(iventar.sorti(men_ive_kno)):
                            if iventar.sorti(men_ive_kno)[vpr_pr][0][1] in ['Голова', 'Туловище', 'Ноги', 'Оружие', 'Щит', 'Кольцо_0', 'Кольцо_1', 'Кольцо_2']:
                                pleeer.don(iventar.sorti(men_ive_kno)[vpr_pr], 'f')
                                #per_men_iv_pr = True   
                    elif men_ive == True:                     
                        per_men_iv = True
                    kno = 0
                elif men_sn[0] == True:
                    men_sn[1] = True
                if per_re_batl[1] == True:
                    if per_re_batl[2] == False and kno_battle[0] == 1:
                        battle_cycle += 1
                        per_re_batl[2] = True
                    if per_re_batl[3] == True:
                        per_re_batl[4] = True
                    elif kno_battle[0] == 3: 
                        per_re_batl[3] = True
                            
            if event.key == pg.K_z:
                print('men_ive_gl', '=',men_ive_gl, '\n',
                    'men_ive', '=',men_ive,'\n',
                    'per_men_iv', '=',per_men_iv,'\n',
                    'men_sn[0]', '=',men_sn[0], '\n',
                    'men_sn[1]', '=',men_sn[1], '\n',
                    'men_sn[2]', '=',men_sn[2], '\n',
                    'kno', '=', kno)      

    if men_ive_gl == False and men_sn[0] == False and per_re_batl[1] == False: 
        vector = [0, 0]

        kpressed = pg.key.get_pressed()

    # считывем движения

        if kpressed[pg.K_UP]:
            for border in spic:
                # 680 и 384 это центр камеры, там стоит игрок и так как обьекты отображаются относительно камеры, эти кординаты надо отнимать для правильной колизии игрока и этих обьектов
                border = pg.Rect(border[0] - 680, border[1] - 384, border[2], border[3])
                # Вот тут я сам хз почему нулевые кординаты, но 1 нужен для проверки колизии)
                testRect = pg.Rect(Player(0, -speed))  
                if testRect.colliderect(border):
                    # Если найден обьект мешающий пройти, кордината онуляется 
                    vector[1] += speed
                    break
            vector[1] -= speed
        elif kpressed[pg.K_DOWN]:
            for border in spic:
                border = pg.Rect(border[0] - 680, border[1] - 384, border[2], border[3])
                testRect = pg.Rect(Player(0, speed))  
                if testRect.colliderect(border):
                    vector[1] -= speed
                    break
            vector[1] += speed

        if kpressed[pg.K_LEFT]:
            for border in spic:
                border = pg.Rect(border[0] - 680, border[1] - 384, border[2], border[3])
                testRect = pg.Rect(Player(-speed, 0))  
                if testRect.colliderect(border):
                    vector[0] += speed
                    break
            vector[0] -= speed

        elif kpressed[pg.K_RIGHT]:
            for border in spic:
                border = pg.Rect(border[0] - 680, border[1] - 384, border[2], border[3])
                testRect = pg.Rect(Player(speed, 0))  
                if testRect.colliderect(border):
                    vector[0] -= speed
                    break
            vector[0] += speed
        # Вр зоны
        for border in battle_son:
            border = pg.Rect(border[0] - 680, border[1] - 384, border[2], border[3])
            testRect = pg.Rect(player.rect[0], player.rect[1], 40, 40)
            if testRect.colliderect(border):
                per_re_batl[0] = True
            else:
                per_re_batl[0] = False


        ##  Если игрок ходил
        if vector != [0, 0]:
            player.move(vector)
            camera.move(vector)
            if per_re_batl[0] == True:
                if randint(0, 1000) > 990:
                    per_re_batl[1] = True
# делаем фон карты белым
    win.fill((255, 255, 255))
# показывем игрока
    # показывают пол
    floor(Map, camera.rect[0], camera.rect[1], frame)
    win.blit(animation_set[frame // 12], (100 - camera.rect[0], 20 - camera.rect[1]))
    frame += 1
    # скорость анимации
    if frame == 60:
        frame = 0
    # показывает кавадрат на фоне персоонажа, этот же квадрат, показывает границу колизии
    #player.draw()
    pg.draw.rect(win, (255, 0, 0), (battle_son[0][0] - camera.rect[0], battle_son[0][1] - camera.rect[1], battle_son[0][2], battle_son[0][3]), 2)
    # показывает спрайт персоонажа
    win.blit(pleer, (680, 384))
    # показывает второй уровень пока
    spic = floor(Map, camera.rect[0], camera.rect[1], frame, horizon=True)
#        text_surface, rect = GAME_FONT.render("Hello World!", (0, 0, 0))
#        win.blit(text_surface, (40, 250))
# другие обькты
    for obj in objects:
        ##  Если объект на экране, отрисовать его
        if obj.rect.colliderect(camera.rect):
            #obj.draw()
            pass
    #win.blit(dereo, (1400 - camera.rect[0], 768 - camera.rect[1]))
    #win.blit(pla, (vector[0], 512 - vector[1]))
    #win.blit(text1, (50, 600))
        #
    if men_ive_gl == True:
        # Показывает кнопки меню
        win.blit(meny[kno], (0, 0))
        if men_ive == True:
            # Отрисовывает меню и кнопки в зависемости от men_ive_kno
            win.blit(men_iven[men_ive_kno], (0, 0))
            # Сортирует инвентарь в зависемости от вкладки men_ive_kno
            iventar.otrisovka(iventar.sorti(men_ive_kno))
            # Если включен выбор вещей то per_men_iv = True
            if per_men_iv == True:
                # Осещает выбор предметов
                win.blit(men_iven[3], (0, 0))
                # Показывает рамку для оринтации в выборе предмета
                win.blit(ramka, (v_m_p[0], v_m_p[1]))
                if per_men_iv_pr == True:
                    win.blit(vi, (0, 0))
                    #print(iventar.sorti(men_ive_kno)[vpr_pr][0][0])
                    win.blit(f1.render(str(iventar.sorti(men_ive_kno)[vpr_pr][0][0]), True, (180, 100, 100)), (680, 384))
    # проверка, ативированно ли меню снарежения
    if men_sn[0] == True:
        win.blit(men_sn_ok[0], (0, 0))
        x = 80
        for i in pleeer.items:
            # 
            if len(str(i)) > 5:
                win.blit(f1.render(str(i)[:5], True, (180, 0, 0)), (0, x))
            else:
                win.blit(f1.render(str(i), True, (180, 0, 0)), (0, x))
            v = pleeer.items[i]
            win.blit(f1.render(f'{v[0]} {(" ").join([f"{b[0][:2]} {b[1]}" for b in v[2][0]])} {(" ").join([f"{b[0][:2]} {b[1]}" for b in v[2][1]])} {(" ").join([f"{b[0][:2]} {b[1]}" for b in v[2][2]])}', True, (180, 180, 0)), (50, x))
            x += 50
        win.blit(men_sn_ok[2], (0, 0))
        dop_perexod = 0
        for s in pleeer.items[ibi[kno]][2]:
            dop_perexod += 1
            visata = 130
            dlina = 165 + 300 * dop_perexod
            perexod = 0
            if s[0][0] == '':
                continue
            for i in s:
                #print(i, visata, dlina)
                perexod += 1
                win.blit(f0.render(str(i[0]), True, (180, 0, 0)), (dlina, visata))
                dlina += 115
                win.blit(f0.render((str(i[1]).rjust(3)), True, (180, 0, 0)), (dlina, visata))
                dlina += 37
                if perexod == 2:
                    perexod = 0
                    dlina = 165 + 300 * dop_perexod
                    visata += 25
        win.blit(ramk_, (50, 30 + 50 * (kno + 1)))
        if men_sn[1] == True:
            win.blit(men_sn_ok[1], (0, 0))
            if pleeer.items[ibi[kno]][1] != '':
                visata = 484
                dlina = 1
                perexod = 0
                for i in iventar.sorti(kno + 10):
                    perexod += 1
                    win.blit(f0.render(str(i[0][0]), True, (180, 0, 0)), (dlina, visata))
                    dlina += 110
                    win.blit(f0.render((str(i[1]).rjust(3)), True, (180, 0, 0)), (dlina, visata))
                    dlina += 25
                    if perexod == 10:
                        perexod = 0
                        visata += 33
            win.blit(ramk, (frame_coo[0], frame_coo[1]))
            if len(iventar.sorti(kno + 10)) > kno_m_s:
                win.blit(men_sn_ok[3], (0, 0))               
                dop_perexod = 0
                for s in iventar.sorti(kno + 10)[kno_m_s][0][2]:
                    dop_perexod += 1
                    visata = 330
                    dlina = 165 + 300 * dop_perexod
                    perexod = 0
                    if s[0][0] == '':
                        continue
                    for i in s:
                        perexod += 1
                        win.blit(f0.render(str(i[0]), True, (180, 0, 0)), (dlina, visata))
                        dlina += 115
                        win.blit(f0.render((str(i[1]).rjust(3)), True, (180, 0, 0)), (dlina, visata))
                        dlina += 37
                        if perexod == 2:
                            perexod = 0
                            dlina = 165 + 300 * dop_perexod
                            visata += 25 
    # Показывает главное меню боя  
    if per_re_batl[1] == True:
        if vrag.HP <= 0:
            battle_cycle = 0
            per_re_batl[1] = False
        # Во время боя реднерится ещё мир за ним, нужно пофиксить
        win.blit(battle_sprait[0], (0, 0))
        #
        #pg.draw.rect(win, (0, 100, 0), (680, 384, 50, 50)    
        pg.draw.rect(win, (36, 255, 24), (63, 388, 1 + round(pleeer.SP * (80 // pleeer.MaxSP)), 50))
        pg.draw.rect(win, (24, 70, 255), (63, 450, 1 + round(pleeer.MP * (130 // pleeer.MaxMP)), 50))
        pg.draw.rect(win, (255, 24, 82), (63, 505, 1 + round(pleeer.HP * (210 // pleeer.MaxHP)), 50))
        win.blit(f0.render(str(pleeer.HP) + '/' + str(pleeer.MaxHP), True, (158, 22, 34)), (96, 510))
        #
        win.blit(battle_sprait_men[0], (0, 0))
        win.blit(battle_sprait_vragi[0], (0, 0))
        win.blit(battle_ramka_g[0], (0, 524 + kno_battle[0] * 40))
        visata = 544
        for i in ['Атака', 'Навыки', 'Магия', 'Вещи', 'Назад']:
            visata += 40
            win.blit(f0.render(i, True, (225, 135, 86)), (0, visata))
        if per_re_batl[2] == True: 
            attack_delay += 1
            if attack_delay == 40:
                attack_delay = 0
                per_re_batl[2] = False
            elif attack_delay == 1:
                damage = str(attack(pleeer, vrag))
            else:
                win.blit(f0.render(damage, True, (184, 5, 16)), (750 + attack_delay // 2, 180 - attack_delay // 2))
        if kno_battle[0] == 2:
            x = 0
            dlina = 160
            visata = 564
            for i in list(pleeer.adility.values()):
                win.blit(f0.render(i[0], True, (22, 156, 130)), (dlina + 300 * x, visata))
                win.blit(f0.render(str(i[1]), True, (22, 156, 52)), ((dlina + 280) + 300 * x, visata))
                x += 1
                if x == 4:
                    visata += 20
                    x = 0
        if kno_battle[0] == 3:
            x = 0
            dlina = 160
            visata = 564
            for i in list(pleeer.spells.values()):
                win.blit(f0.render(i[0], True, (22, 129, 156)), (dlina + 300 * x, visata))
                win.blit(f0.render(str(i[1]), True, (22, 80, 156)), ((dlina + 280) + 300 * x, visata))
                x += 1
                if x == 4:
                    visata += 20
                    x = 0
        if per_re_batl[3] == True:
            win.blit(battle_ramka_g[1], (160 + 300 * (kno_battle[1] % 4), 564 + 20 * (kno_battle[1] // 4)))   
            if kno_battle[1] < len(pleeer.spells) and [i for i in pleeer.spells.values()][kno_battle[1]][1] <= pleeer.MP:
                if per_re_batl[4] == True: 
                    attack_delay += 1
                    if attack_delay == 40:
                        attack_delay = 0
                        per_re_batl[4] = False
                    elif attack_delay == 1:
                        damage = str(attack_magic(pleeer, [i for i in pleeer.spells.values()][kno_battle[1]], vrag))
                    else:
                        win.blit(f0.render(damage, True, (184, 5, 16)), (750 + attack_delay // 2, 180 - attack_delay // 2))       
    #win.blit(dre, (50 - camera.rect[0], 600 - camera.rect[1]))
    pg.display.flip() ##    = pg.display.update()
    clock.tick(60)
    pg.time.wait(1)
# 0.15 # Удаленны некоторые коментарии