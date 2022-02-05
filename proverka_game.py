from script.start_game import win, pg, sys, randint, f1
# Название игры
pg.display.set_caption('Long Way')
from script.base_classes import player, object, camera
# делаем слепки обьектов, наверное) 
#player = Player(0, 0)
#camera = cam(0, 0)
# "D:/prog/game/aset/derevo.png"
with open(r'D:\\prog\\f.txt', 'r', encoding='utf-8') as file:
    objects = [object(int(i[1][0]), int(i[1][1]), int(i[1][2]), int(i[1][3]), spr=[pg.image.load(sys.path[0] + i[0][0]).convert_alpha(), ]) for i in (list(map(lambda x: [i.split('_') for i in x.split()], list(map(str.strip, file.readlines())))))]
# Загрузка спрайтов
men_iven =  [pg.image.load(sys.path[0] + "\\aset\\men\\men_ive_items.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\men_ive_equipment.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\men_ive_important.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\men_ive.png").convert_alpha()]
ramka = pg.image.load(sys.path[0] + "\\aset\\men\\ramka.png").convert_alpha()

pleer = pg.image.load(sys.path[0] + "\\aset\\pleer.png").convert_alpha()
battle_sprait_men = [pg.image.load(sys.path[0] + "\\aset\\men\\oc_m_b.png").convert_alpha()]
battle_sprait = [pg.image.load(sys.path[0] + "\\aset\\men\\sac_b_les.png").convert_alpha()]
battle_sprait_vragi = [pg.image.load(sys.path[0] + "\\aset\\men\\vrag.png").convert_alpha()] 
battle_ramka_g = [pg.image.load(sys.path[0] + "\\aset\\men\\ramka_g_m_b.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\ramka_p_sc.png").convert_alpha()]
vi = pg.image.load(sys.path[0] + "\\aset\\men\\vi.png").convert_alpha()
men_sn_ok = [pg.image.load(sys.path[0] + "\\aset\\men\\oc_okn.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\dop_okn.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\dop_okn_n.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\dop_okn_v.png").convert_alpha()]
ramk = pg.image.load(sys.path[0] + "\\aset\\men\\ramka_e.png").convert_alpha()
ramk_ = pg.image.load(sys.path[0] + "\\aset\\men\\ramka_m.png").convert_alpha()
f0 = pg.font.Font(sys.path[0] + "\\Fonts\\HATTEN.ttf", 20)
text1 = f1.render('Игра ещё не готова, что ты тут делаешь?', True, (0, 180, 0))
animation_set = [pg.image.load(sys.path[0] + f"\\aset\\GuttyKreumNatureTilesvol1_v2\\AnimationFrames\\Bush/bush32x32transparentanimated{i}.png").convert_alpha() for i in range(1, 14)]
from script.modile_interface import *
# Название, трата по мане, урон, тип, масовое или нет заклинание
list_spells = (('Магический удар', 2, 10, ('Воздушный'), False),
                 ('fairbol', 3, 9, ('Огненый', 'Воздушный'), True))
# Название, трата по очками способностей, тип, масовое или нет способность
list_adility = (('Удар с ноги', 1, 6, ('Пронзающий'), False),
                 ('Круговой удар', 2, 9, ('Дробящий'), True))
# inventory_class
from script.items import *
from script.inven import *
from script.player_modile import *
for i in thing.list_of_items.values():
    iventar.dopov((i, 1))
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
#################################################################################################################################
from script.menu import inven      
men_list = [inven, ]
#################################################################################################################################
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
                akt_fn = inven.fkl()
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
                print(kno)  

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
    #floor(Map, camera.rect[0], camera.rect[1], frame)
    win.blit(animation_set[frame // 12], (100 - camera.rect[0], 20 - camera.rect[1]))
    frame += 1
    # скорость анимации
    if frame == 60:
        frame = 0
    # показывает кавадрат на фоне персоонажа, этот же квадрат, показывает границу колизии
    #player.draw()
    pg.draw.rect(win, (255, 0, 0), (battle_son[0][0] - camera.rect[0], battle_son[0][1] - camera.rect[1], battle_son[0][2], battle_son[0][3]), 2)
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
        if i.aktv == True:
            men_ive_gl = True 
            ost_pyt = i.spis
            for d in i.pyt:
                ost_pyt = ost_pyt[d]
            win.blit(ost_pyt[i.ataw][0].sprait, (0, 0))
            if ost_pyt[i.ataw][0].ak != None:
                ost_pyt[i.ataw][0].prin_tab(ost_pyt[i.ataw][0].tab)
            if ost_pyt[i.ataw][0].ak == True:
                ost_pyt[i.ataw][0].draw()
    # проверка, ативированно ли меню снарежения
    if men_sn[0] == True:
        obw_od.rendering_interface(pleeer.items.values())
        dressed_item_specifications.rendering_interface(pleeer.items[ibi[kno]][2][0])
        dressed_item_chances.rendering_interface(pleeer.items[ibi[kno]][2][1])
        dressed_item_resistance.rendering_interface(pleeer.items[ibi[kno]][2][2])
        win.blit(ramk_, (50, 30 + 50 * (kno + 1)))
        if men_sn[1] == True:
            gr.rendering_interface([(i[0][0], i[1]) for i in iventar.sorti(kno + 10)])
            #
            #
            #
            #
            #
            #
            gr.rendering_frame(ramk, kno)
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
# 0.17
