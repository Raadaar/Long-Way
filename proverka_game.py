
from script.start_game import win, pg, sys, randint, f1
import script.guide
# Название игры
pg.display.set_caption('Long Way')
from script.base_classes import player, object, camera
# делаем слепки обьектов, наверное) 
#player = Player(0, 0)
#camera = cam(0, 0)
# "D:/prog/game/aset/derevo.png"
with open(r'D:\\prog\\f.txt', 'r', encoding='utf-8') as file:
    objects = [object(int(i[1][0]), int(i[1][1]), int(i[1][2]), int(i[1][3]), spr=[pg.image.load(script.guide.path + i[0][0]).convert_alpha(), ]) for i in (list(map(lambda x: [i.split('_') for i in x.split()], list(map(str.strip, file.readlines())))))]
# Загрузка спрайтов
men_iven =  [pg.image.load(script.guide.path + "\\aset\\men\\men_ive_items.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\men_ive_equipment.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\men_ive_important.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\men_ive.png").convert_alpha()]
ramka = pg.image.load(script.guide.path + "\\aset\\men\\ramka.png").convert_alpha()

pleer = pg.image.load(script.guide.path + "\\aset\\pleer.png").convert_alpha()
battle_men_sprait_men = [pg.image.load(script.guide.path + "\\aset\\men\\oc_m_b.png").convert_alpha()]
battle_men_ramka_g = [pg.image.load(script.guide.path + "\\aset\\men\\ramka_g_m_b.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\ramka_p_sc.png").convert_alpha()]
vi = pg.image.load(script.guide.path + "\\aset\\men\\vi.png").convert_alpha()
men_sn_ok = [pg.image.load(script.guide.path + "\\aset\\men\\oc_okn.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\dop_okn.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\dop_okn_n.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\dop_okn_v.png").convert_alpha()]
ramk = pg.image.load(script.guide.path + "\\aset\\men\\ramka_e.png").convert_alpha()
ramk_ = pg.image.load(script.guide.path + "\\aset\\men\\ramka_m.png").convert_alpha()
f0 = pg.font.Font(script.guide.path + "\\Fonts\\HATTEN.ttf", 20)
text1 = f1.render('Игра ещё не готова, что ты тут делаешь?', True, (0, 180, 0))
animation_set = [pg.image.load(script.guide.path + f"\\aset\\GuttyKreumNatureTilesvol1_v2\\AnimationFrames\\Bush/bush32x32transparentanimated{i}.png").convert_alpha() for i in range(1, 14)]
from script.modile_interface import *
# inventory_class
from script.items import *
from script.inven import *
from script.player_modile import *
from script.enemy import *
for i in thing.list_of_items.values():
    iventar.dopov([i, 1])
######################################################
from script.menu import inven, battle_men, men_list, fps   
######################################################
#beginning_battle
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

clock = pg.time.Clock()
#
battle_men_cycle = 0
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
kno_battle_men = [1, 0]
# Список боевых зон
battle_men_son = [pg.Rect(0, 0, 300, 300)]

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
                if sum(i.aktv for i in men_list) == 0:
                    akt_fn = inven.fkl()
                else:
                    for i in men_list:
                        if i.aktv == True:
                            i.fkl()
            if event.key == pg.K_RIGHT:
                for i in men_list:
                    if i.aktv == True:
                        i.peredwe('Право')
            if event.key == pg.K_LEFT:
                for i in men_list:
                    if i.aktv == True:
                        i.peredwe('Лево')
            if event.key == pg.K_UP:
                for i in men_list:
                    if i.aktv == True:
                        i.peredwe('Верх')
            if event.key == pg.K_DOWN:
                for i in men_list:
                    if i.aktv == True:
                        i.peredwe('Низ')
            if event.key == 13: 
                for i in men_list:
                    if i.aktv == True:
                        i.akt()
            if event.key == pg.K_z:
                print([i.HP for i in batlee.enemy_list])  
                print(pleeer.HP, batlee.enemy_list[0].condition)

    if men_ive_gl == False: 
        vector = [0, 0]

        kpressed = pg.key.get_pressed()

    # считывем движения

        if kpressed[pg.K_UP]:

            vector[1] -= speed
        elif kpressed[pg.K_DOWN]:

            vector[1] += speed

        if kpressed[pg.K_LEFT]:

            vector[0] -= speed

        elif kpressed[pg.K_RIGHT]:

            vector[0] += speed
        # Вр зоны
        for border in enemy_combat_zone:
            border_test = pg.Rect(border.re[0] - 680, border.re[1] - 384, border.re[2], border.re[3])
            testRect = pg.Rect(player.rect[0], player.rect[1], 40, 40)
            if testRect.colliderect(border_test):
                print(border)
                border.beginning_battle(batlee)
                akt_fn = battle_men.fkl()


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
    #floor(Map, camera.rect[0], camera.rect[1], frame)
    win.blit(animation_set[frame // 12], (100 - camera.rect[0], 20 - camera.rect[1]))
    frame += 1
    # скорость анимации
    if frame == 60:
        frame = 0
    # показывает кавадрат на фоне персоонажа, этот же квадрат, показывает границу колизии
    #player.draw()
    pg.draw.rect(win, (255, 0, 0), (battle_men_son[0][0] - camera.rect[0], battle_men_son[0][1] - camera.rect[1], battle_men_son[0][2], battle_men_son[0][3]), 2)
    # показывает спрайт персоонажа
    
    # показывает второй уровень пока
    #spic = floor(Map, camera.rect[0], camera.rect[1], frame, horizon=True)
#        text_surface, rect = GAME_FONT.render("Hello World!", (0, 0, 0))
#        win.blit(text_surface, (40, 250))
# другие обькты
    for obj in objects:
        ##  Если объект на экране, отрисовать его
        if obj.rect.colliderect(camera.rect):
            obj.draw()
    win.blit(pleer, (680, 384))
    #win.blit(dereo, (1400 - camera.rect[0], 768 - camera.rect[1]))
    #win.blit(pla, (vector[0], 512 - vector[1]))
    #win.blit(text1, (50, 600))
    for i in men_list:
        ost_pyt = i.spis
        if i.aktv == True:
            men_ive_gl = True 
            ost_pyt[i.ataw][0].output()
    if sum(i.aktv for i in men_list) == 0:
        men_ive_gl = False
    fps.output()
    #win.blit(dre, (50 - camera.rect[0], 600 - camera.rect[1]))
    pg.display.flip() ##    = pg.display.update()
    clock.tick(60)
    pg.time.wait(1)
# 0.17
