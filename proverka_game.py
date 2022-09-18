from script.start_game import win, pg, sys, randint, f1
import script.guide
from script.map import prop_objects, recursion_otr, card, moving
# Название игры
pg.display.set_caption('Long Way')
from script.base_classes import player, object, camera, Player, cam
# делаем слепки обьектов, наверное) 
#player = Player(0, 0)
#camera = cam(0, 0)
doroga = pg.image.load(script.guide.path + "\\aset\\patch32x32transparent.png").convert_alpha()
men_iven =  [pg.image.load(script.guide.path + "\\aset\\men\\men_ive_items.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\men_ive_equipment.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\men_ive_important.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\men_ive.png").convert_alpha()]
ramka = pg.image.load(script.guide.path + "\\aset\\men\\ramka.png").convert_alpha()
zvet = pg.image.load(script.guide.path + "\\aset\\grassi32x32transparent.png").convert_alpha()#grassi32x32transparent
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
from script.quest import turn, interaction_zones, activation_zones
from script.items import *
from script.inven import *
from script.player_modile import *
from script.enemy import *
for i in thing.list_of_items.values():
    iventar.dopov([i, 1])
from script.sound import sound, leaves
######################################################
from script.menu import inven, battle_men, men_list, fps, dialog_men, text
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
# Доп блоки
# Не пересекаемый 

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
son_sond = pg.Surface((200, 200))
battle_men_son = [pg.Rect(0, 0, 300, 300)]
camera.rect[0], camera.rect[1] = 500, 500
player.rect[0], player.rect[1] = 500, 500
frame = 0
attack_delay = 0
bj = False
bj_ = False
ibi = ['Голова', 'Туловище', 'Ноги', 'Оружие', 'Щит', 'Кольцо_0', 'Кольцо_1', 'Кольцо_2']
while  1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                if sum(i.activity for i in men_list) == 0:
                    men_list[0].activity = True
                    men_list[0].single()
                else:
                    for i in [i.relevance() for i in men_list]:
                        if i.activity == True:
                            i.control('обратно')
            if event.key == pg.K_RIGHT:
                for i in men_list:
                    if i.activity == True:
                        i.control('Право')
            if event.key == pg.K_LEFT:
                for i in men_list:
                    if i.activity == True:
                        i.control('Лево')
            if event.key == pg.K_UP:
                for i in men_list:
                    if i.activity == True:
                        i.control('Верх')
            if event.key == pg.K_DOWN:
                for i in men_list:
                    if i.activity == True:
                        i.control('Низ')
            if event.key == 13: 
                if sum(i.activity for i in men_list) == 0:
                    bj_ = True    
                    bj = player.test_area()
                    #[print(i[2]) for i in card.interaction_layer if bj.colliderect(i[0])]    
                for i in men_list:
                    if i.activity == True:
                        i.control('вперёд')
   
            if event.key == pg.K_z:
                print([i.HP for i in batlee.enemy_list])  
                print(pleeer.HP, batlee.enemy_list[0].condition)

    if men_ive_gl == False: 
        vector = [0, 0]

        kpressed = pg.key.get_pressed()

    # считывем движения
        for i in prop_objects:
            if i.rect.colliderect(camera.rect):
                for d in i.compound:
                    if d.rect.colliderect(camera.rect):
                        for v in d.compound:
                            if v.rect.colliderect(camera.rect):
                                [obj.interaction_check_bar(card) for obj in v.compound if obj.rect.colliderect(camera.rect)]
        if kpressed[pg.K_UP]:
            player.route = 'up'
            for border in card.layer_barriers: 
                testRect = pg.Rect(680, 384 - speed, 50, 50) 
                # 680 и 384 это центр камеры, там стоит игрок и так как обьекты отображаются относительно камеры, эти кординаты надо отнимать для правильной колизии игрока и этих обьектов
                #border = pg.Rect(border[0] - 680, border[1] - 384, border[2], border[3])
                # Вот тут я сам хз почему нулевые кординаты, но 1 нужен для проверки колизии)
                if testRect.colliderect(border):
                   # Если найден обьект мешающий пройти, кордината онуляется 
                   vector[1] += speed
                   break
            vector[1] -= speed
        elif kpressed[pg.K_DOWN]:
            player.route = 'down'
            for border in card.layer_barriers: 
                testRect = pg.Rect(680, 384 + speed, 50, 50)  
                if testRect.colliderect(border):
                    vector[1] -= speed
                    break
            vector[1] += speed
        if kpressed[pg.K_LEFT]:
            player.route = 'left'
            for border in card.layer_barriers:
                testRect = pg.Rect(680- speed, 384 , 50, 50)  
                if testRect.colliderect(border):
                    vector[0] += speed
                    break
            vector[0] -= speed
        elif kpressed[pg.K_RIGHT]:
            player.route = 'right'
            for border in card.layer_barriers:
                testRect = pg.Rect(Player(speed, 0)) 
                testRect = pg.Rect(680 + speed, 384 , 50, 50)
                if testRect.colliderect(border):
                    vector[0] -= speed
                    break
            vector[0] += speed
        #if kpressed[pg.K_UP]:
        #    player.route = 'up'
        #    vector[1] -= speed
#
        #elif kpressed[pg.K_DOWN]:
        #    player.route = 'down'
        #    vector[1] += speed
#
        #if kpressed[pg.K_LEFT]:
        #    player.route = 'left'
        #    vector[0] -= speed
#
        #elif kpressed[pg.K_RIGHT]:
        #    player.route = 'right'
        #    vector[0] += speed
        # Вр зоны
        for border in enemy_combat_zone:
            border_test = pg.Rect(border.re[0] - 680, border.re[1] - 384, border.re[2], border.re[3])
            testRect = pg.Rect(player.rect[0], player.rect[1], 40, 40)
            if testRect.colliderect(border_test):
                per_re_batl[0] = True
            else:
                per_re_batl[0] = False


        ##  Если игрок ходил
        if vector != [0, 0]:
            player.move(vector, fps.fps)
            camera.move(vector)
            moving.cl_1_sk_sd.blit(moving.cl_1_sk, (vector[0], vector[1]))
            cl_1_sk = moving.cl_1_sk_sd
            if per_re_batl[0] == True:
                if randint(0, 1000) > 990 and False:
                    border.beginning_battle(batlee)
                    akt_fn = battle_men.fkl()
        for i in activation_zones:
            pl = pg.Rect(680, 384, player.rect[2], player.rect[3])
            ix = pg.Rect(i[0] - camera.rect[0], i[1] - camera.rect[1], i[2], i[3])
            if pl.colliderect(ix):
                Quest.search(['область', i])
# делаем фон карты белым
    win.fill((255, 255, 255))
# показывем игрока
    # показывают пол
    #floor(Map, camera.rect[0], camera.rect[1], frame)
    #win.blit(animation_set[frame // 12], (100 - camera.rect[0], 20 - camera.rect[1]))
    frame += 1
    # скорость анимации
    if frame == 300:
        frame = 0
    # показывает кавадрат на фоне персоонажа, этот же квадрат, показывает границу колизии
    #player.draw()
    #pg.draw.rect(win, (255, 0, 0), (battle_men_son[0][0] - camera.rect[0], battle_men_son[0][1] - camera.rect[1], battle_men_son[0][2], battle_men_son[0][3]), 2)
    # показывает спрайт персоонажа
    
    # показывает второй уровень пока
    #spic = floor(Map, camera.rect[0], camera.rect[1], frame, horizon=True)
#        text_surface, rect = GAME_FONT.render("Hello World!", (0, 0, 0))
#        win.blit(text_surface, (40, 250))
# другие обькты
    prop_objects = sorted(prop_objects, key=lambda x: [x.rect[0], x.rect[1]])
    #[recursion_otr(i.compound, 0) for i in prop_objects if i.rect.colliderect(camera.rect)]
    recursion_otr()
   
    if bj_:
        #pg.draw.rect(win, (100, 100, 100), bj)#(bj[0], bj[1], bj[2], bj[3]))
        for i in card.interaction_layer:
            if bj.colliderect(i[0]):
                bf = i[1]()
                if bf != False:
                    dialog_men.aktv = True
                    text.text_update(bf)
        for i in interaction_zones:
            ix = pg.Rect(i[0] - camera.rect[0], i[1] - camera.rect[1], i[2], i[3])
            if bj.colliderect(ix):
                Quest.search(['взаимодействие', i])
        bj_ = False
    win.blit(moving.cl_1_sk, (-320, -116))
    #win.blit(moving.cl_2_sk, (-320, -116)) 680, 384
    card.drawing_layers()
    pg.draw.rect(win, (255, 0, 0), (1000 - camera.rect[0], 1000 - camera.rect[1], 200, 200), 2)
    #win.blit(son_sond, (1000 - camera.rect[0], 1000 - camera.rect[1]))
    son_sound_rect = pg.Rect(1000 - camera.rect[0], 1000 - camera.rect[1], 200, 200)
    if son_sound_rect.colliderect(pg.Rect(680, 384, 50, 50)):
        x_s, y_s = (680 + camera.rect[0]) - 1000, (384 + camera.rect[1]) - 1000
        if sound.effects[0].get_sound() == None:
            sound.effects[0].play(leaves)
        if x_s < 0:
            x_s = 0
        if y_s < 0:
            y_s = 0
        if y_s > 100:
            y_s = (200 % y_s) // 200
        if x_s > 100:
            x_s = 200 % x_s
            #print((x_s + y_s) / 200, (x_s + y_s) / 300)
            sound.effects[0].set_volume((x_s + y_s) / 200, (x_s + y_s) / 250)#(x_s - 15) / 200)
        else:
            sound.effects[0].set_volume((x_s + y_s) / 250, (x_s + y_s) / 200)
    else:
        sound.effects[0].stop()
    #[win.blit(i._surface[0], (i.rect[0] - camera.rect[0], i.rect[1] - camera.rect[1])) for i in prop_objects if i.rect.colliderect(camera.rect)]
    #[win.blit(i._surface[1], (i.rect[0] - camera.rect[0], i.rect[1] - camera.rect[1])) for i in prop_objects if i.rect.colliderect(camera.rect)]
    win.blit(zvet, (750 - camera.rect[0], 750 - camera.rect[1]))
    win.blit(doroga, (4215 - camera.rect[0], 4550 - camera.rect[1]))
    #win.blit(pleer, (680, 384))(750, 750, 50, 50)
    #win.blit(dereo, (1400 - camera.rect[0], 768 - camera.rect[1]))
    #win.blit(pla, (vector[0], 512 - vector[1]))
    #win.blit(text1, (50, 600))
    #if not sound.main_composition.get_busy():
    #    sound.change_main_composition('мир')
    for i in [i.relevance() for i in men_list]:
        if i.activity == True:
            men_ive_gl = True
            i.cycle() 
    if sum(i.activity for i in [i.relevance() for i in men_list]) == 0:
        turn.check([dialog_men, text], [player, camera])
        men_ive_gl = False        
    bar = []
    fps.output()
    #win.blit(dre, (50 - camera.rect[0], 600 - camera.rect[1]))
    pg.display.flip() ##    = pg.display.update()
    clock.tick(60)
    pg.time.wait(1)
# 0.17
