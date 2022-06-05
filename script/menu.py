from datetime import datetime
from script.start_game import win, pg
import script.guide
# script.guide.path
from script.radota_text import Text, pla, text
from script.inven import *
from script.player_modile import pleeer
from script.modile_interface import showing_properties, gr, display_abilities
from script.enemy import *
from script.skill import *
ramka_inventar = pg.image.load(script.guide.path + "\\aset\\men\\ramka_inven.png").convert_alpha()
pati = [pleeer, ]
pleeer.spells.append(class_magic.magic_dictionary['Водный поток'])
pleeer.spells.append(class_magic.magic_dictionary['Святое проклятье'])
pleeer.adility.append(class_ability.ability_dictionary['Удар кинжалом'])
pleeer.adility.append(class_ability.ability_dictionary['Удар ногой'])
class class_fps:
    def __init__(self) -> None:
        self.fps = 0
        self.fps_pro = 0
        self.min_max = [300, 0]
        self.cr_data = datetime.now().second 
    def output(self):
        self.fps += 1
        if self.fps == 300:
            self.fps = 299
        win.blit(f1.render(str(self.fps_pro), True, (23, 128, 109)), (0, 0))
        nis = datetime.now().second
        if self.cr_data != nis:
            self.cr_data = nis
            self.fps_pro = self.fps
            if self.fps_pro < self.min_max[0]:
                self.min_max[0] = self.fps_pro
            elif self.fps_pro > self.min_max[1]:
                self.min_max[1] = self.fps_pro
            self.fps = 0 
fps = class_fps()
def maping(pati): # mapping  
    for pleeer in pati:     
        pg.draw.rect(win, (36, 255, 24), (63, 388, 1 + round(pleeer.SP * (80 // pleeer.MaxSP)), 50))
        pg.draw.rect(win, (24, 70, 255), (63, 450, 1 + round(pleeer.MP * (130 // pleeer.MaxMP)), 50))
        pg.draw.rect(win, (255, 24, 82), (63, 505, 1 + round(pleeer.HP * (210 // pleeer.MaxHP)), 50))
class spreadsheet:
    def __init__(self, s, n_r=(0,0), p_r=(0,0), s_r='', g_r=(0,0), tab=[[[0,], ], False], prin_tab='', text=(('', (0, 0, 0), (0, 0)), ), inactive_display='', dop_ot=lambda x, c: x, additional_functionality=(), additional_value=(), dop_sprai=[['', ],], additional_tap=lambda x: x, ak = False) -> None:
        self.sprait = s # Спрайт
        self.dop_spait = dop_sprai
        self.sprait_ram = s_r # Спрайт рамки
        self.start_coordinates = n_r # Начальные координаты рамки
        self.moving_coordinates = p_r # координаты передвежения рамки
        self.p = 0 # Выбор предмета в списке + передвежение рамки
        self.p1 = g_r # Границы передвежения рамки
        self.p2 = '' # Границф
        self.list_getting_table = tab # Таблица с которой надо работать ((преобразующие функии/словари), начальный аргумент)
        self.prin_tab = prin_tab # Принцип отрисовки таблицы
        self.ak = ak # Активность таблицы
        self.additional_functionality = additional_functionality
        self.dop_ot = dop_ot
        self.inactive_display = inactive_display
        self.additional_value = additional_value
        self.additional_key = False
        self.additional_tap = additional_tap
        if s_r == '':
            self.ak = None
            if ak == True:
                self.ak = False
    @property
    def table_list(self): # Нужно для состовления нужного списка для таблицы
        x = self.list_getting_table[0]
        b = self.list_getting_table[1]
        for i in x:
            if isinstance(i, dict) and b != False:
                b = i[b]
            elif b == False and str(b) != '0':
                b = i
            else:
                b = i(b)
        return b
    # self.start_coordinates=(560, 75), self.moving_coordinates=(285, 25), self.p1=(1360, 500)
    def draw(self):
        if self.ak == True:
            kol_pr = self.p
            y = self.start_coordinates[1]
            number_cells_length = (self.p1[0] - self.start_coordinates[0]) // self.moving_coordinates[0]
            if number_cells_length <= 0:
                print('Отрицательное число number_cells_length')
            while kol_pr >= number_cells_length:
                kol_pr -= number_cells_length
                y += self.moving_coordinates[1]
            win.blit(self.sprait_ram, (self.start_coordinates[0] + self.moving_coordinates[0] * kol_pr, y))
    def peredwe(self, kyda):
        if self.additional_key == True:
            self.additional_tap(kyda)
        else:
            x = (self.start_coordinates[0] - self.p1[0]) // self.moving_coordinates[0]
            slow = {'Низ': -x, 'Верх': x, 'Право': 1, 'Лево': -1}
            if self.p + slow[kyda] >= 0:
                self.p += slow[kyda]
            print(self.p)
    def output(self):
        #self.dop_ot(self, fps) 04.06 дата изменения
        if self.inactive_display != '':
            self.inactive_display[0](self.inactive_display[1], self)
        win.blit(self.sprait, (0, 0))
        self.dop_ot(self, fps) # 04.06 дата изменения
        if len(self.dop_spait[0]) > 1:
            for pak in self.dop_spait:
                win.blit(pak[0], pak[1])
        if self.sprait_ram != '':
            if self.ak != None:
                self.prin_tab(self.table_list)
        if self.ak == True:
            self.draw()
            [ad_fun((self.table_list, self.p)) for ad_fun in self.additional_functionality]
men_os = pg.image.load(script.guide.path + "\\aset\\men\\oc_okn.png").convert_alpha()
ram_cn = pg.image.load(script.guide.path + "\\aset\\men\\ram_cn.png").convert_alpha()
x = (
    (('Низ', 'Верх'), 7),
    (
        spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Back.png").convert_alpha()),
    ),
    (
        spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Items.png").convert_alpha()),
    (
        # (s(), ),
        (('Право', 'Лево'), 3),
        (
            spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\men_ive_items.png").convert_alpha(), s_r=ramka_inventar, n_r=(560, 75), p_r=(266, 25), g_r=(1360, 500), tab=((iventar.sorti, ), 0), prin_tab=iventar.otrisovka)
        ,), 
        (
            spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\men_ive_equipment.png").convert_alpha(), s_r=ramka_inventar, n_r=(560, 75), p_r=(266, 25), g_r=(1360, 500), tab=((iventar.sorti, ), 1), prin_tab=iventar.otrisovka)
        ,),  
        (
            spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\men_ive_important.png").convert_alpha(), s_r=ramka_inventar, n_r=(560, 75), p_r=(266, 25), g_r=(1360, 500), tab=((iventar.sorti, ), 2), prin_tab=iventar.otrisovka)
        ,)
    )
    ),
    (
        spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Quests.png").convert_alpha()),
    ),
    (
        spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Equipment.png").convert_alpha()),
    (
        (('Низ', 'Верх'), 8),
        (
            spreadsheet(s=men_os, s_r=ram_cn, n_r=(0, 484), p_r=(136, 28), g_r=(1360, 768), tab=((iventar.equipment_sorti, ), (armor,'Голова')), prin_tab=gr.rendering_interface, inactive_display=(showing_properties, (pleeer, 'Голова')), additional_functionality=(showing_properties,), additional_value=('Голова',))
        ,),
        (
            spreadsheet(s=men_os, s_r=ram_cn, n_r=(0, 484), p_r=(136, 28), g_r=(1360, 768), tab=((iventar.equipment_sorti, ), (armor,'Туловище')), prin_tab=gr.rendering_interface, inactive_display=(showing_properties, (pleeer, 'Туловище')), additional_functionality=(showing_properties,), additional_value=('Туловище',))
        ,),
        (
            spreadsheet(s=men_os, s_r=ram_cn, n_r=(0, 484), p_r=(136, 28), g_r=(1360, 768), tab=((iventar.equipment_sorti, ), (armor,'Ноги')), prin_tab=gr.rendering_interface, inactive_display=(showing_properties, (pleeer, 'Ноги')), additional_functionality=(showing_properties,), additional_value=('Ноги',))
        ,),
        (
            spreadsheet(s=men_os, s_r=ram_cn, n_r=(0, 484), p_r=(136, 28), g_r=(1360, 768), tab=((iventar.equipment_sorti, ), (arms,'Оружие_0')), prin_tab=gr.rendering_interface, inactive_display=(showing_properties, (pleeer, 'Оружие_0')), additional_functionality=(showing_properties,), additional_value=('Оружие_0',))
        ,),
        (
            spreadsheet(s=men_os, s_r=ram_cn, n_r=(0, 484), p_r=(136, 28), g_r=(1360, 768), tab=((iventar.equipment_sorti, ), (arms,'Оружие_1')), prin_tab=gr.rendering_interface, inactive_display=(showing_properties, (pleeer, 'Оружие_1')), additional_functionality=(showing_properties,), additional_value=('Оружие_1',))
        ,),
        (
            spreadsheet(s=men_os, s_r=ram_cn, n_r=(0, 484), p_r=(136, 28), g_r=(1360, 768), tab=((iventar.equipment_sorti, ), (ring,'Кольцо_0')), prin_tab=gr.rendering_interface, inactive_display=(showing_properties, (pleeer, 'Кольцо_0')), additional_functionality=(showing_properties,), additional_value=('Кольцо_0',))
        ,),
        (
            spreadsheet(s=men_os, s_r=ram_cn, n_r=(0, 484), p_r=(136, 28), g_r=(1360, 768), tab=((iventar.equipment_sorti, ), (ring,'Кольцо_1')), prin_tab=gr.rendering_interface, inactive_display=(showing_properties, (pleeer, 'Кольцо_1')), additional_functionality=(showing_properties,), additional_value=('Кольцо_1',))
        ,),
        (
            spreadsheet(s=men_os, s_r=ram_cn, n_r=(0, 484), p_r=(136, 28), g_r=(1360, 768), tab=((iventar.equipment_sorti, ), (ring,'Кольцо_2')), prin_tab=gr.rendering_interface, inactive_display=(showing_properties, (pleeer, 'Кольцо_2')), additional_functionality=(showing_properties,), additional_value=('Кольцо_2',))
        ,),
    )
    ),
    (
        spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Saving.png").convert_alpha()),
    ),
    (
        spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Loading.png").convert_alpha()),
    ),
    (
        spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Exit.png").convert_alpha()), 
    )
)
# iventar.sorti(pleeer.equipment['Голова']) ((pleeer.equipment, iventar.sorti), 'Голова')
men_ = spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Back.png").convert_alpha(),
                s_r=pg.image.load(script.guide.path + "\\aset\\men\\ramka.png").convert_alpha(),
                n_r=(400, 400), p_r=(10, 10), g_r=(800, 800))
akt_fn = None
class meni:
    def __init__(self, spis) -> None:
        self._spis = spis
        self.pyt = []
        self.ataw = 1
        self.ataw_fun = 0
        self.aktv = False
    @property
    def spis(self):
        ost_pyt = self._spis
        if len(self.pyt) != 0:
            for i in self.pyt:
                ost_pyt = ost_pyt[i]
        return ost_pyt        
    def fkl(self):
        ost_pyt = self.spis
        if ost_pyt[self.ataw][0].additional_key == True:
            ost_pyt[self.ataw][0].additional_key = False
        elif ost_pyt[self.ataw][0].ak == True:
            ost_pyt[self.ataw][0].ak = False
            ost_pyt[self.ataw][0].p = 1
        elif self.aktv == False and sum(i.aktv for i in men_list) == 0:
            self.aktv = True
        elif battle_men.aktv == True:
            pass
        else:
            if len(self.pyt) != 0:
                if akt_fn == None:
                    self.ataw = self.pyt[-2]
                    self.pyt = self.pyt[:-2]
                else:
                    return None
            else:
                self.aktv = False
                return akt_fn
    def peredwe(self, kyda):
        ost_pyt = self.spis
        if ost_pyt[self.ataw][0].ak == True or ost_pyt[self.ataw][0].additional_key == True:
            ost_pyt[self.ataw][0].peredwe(kyda)
        elif kyda in ost_pyt[0][0]:
            if kyda == ost_pyt[0][0][0]:
                self.ataw += 1
                if self.ataw == ost_pyt[0][1] + 1:
                    self.ataw = 1
            else:
                self.ataw -= 1
                if self.ataw == 0:
                    self.ataw = ost_pyt[0][1]

    def akt(self):
        ost_pyt = self.spis
        if ost_pyt[self.ataw][0].ak == None:
            self.pyt.append(self.ataw)
            self.pyt.append(1)
            self.ataw = 1
        elif ost_pyt[self.ataw][0].ak == True:
            if inven.aktv == True or str(ost_pyt[self.ataw][0].list_getting_table[1]) == '0':
                if ost_pyt[self.ataw][0].p - 1 <= len(ost_pyt[self.ataw][0].table_list):
                    choice_number = [i for i in range(len(iventar.inventory)) if iventar.inventory[i][0] == ost_pyt[self.ataw][0].table_list[ost_pyt[self.ataw][0].p][0]][0]
                    iventar.inventory[choice_number][1] = iventar.inventory[choice_number][1] - 1 # Отнимаем от количество
                    if isinstance(iventar.inventory[choice_number][0], equipment): # Если это equipment то using вернёт предмет что был надет
                        if isinstance(iventar.inventory[choice_number][0], (arms, ring)) and len(ost_pyt[self.ataw][0].additional_value) > 0:
                            cvb = iventar.inventory[choice_number][0]
                            past_subject = iventar.inventory[choice_number][0].using(pleeer, place=ost_pyt[self.ataw][0].additional_value)
                            if isinstance(iventar.inventory[choice_number][0], ring):
                                if past_subject != '':
                                    past_subject.using(pleeer, reverse_application=True)
                                    iventar.dopov([past_subject, 1])
                            else:
                                for i in past_subject:
                                    if i != '':
                                        i.using(pleeer, reverse_application=True)
                                        iventar.dopov([i, 1])                               
                        else:
                            past_subject = iventar.inventory[choice_number][0].using(pleeer)
                            if past_subject != '':
                                past_subject.using(pleeer, reverse_application=True)
                                iventar.dopov([past_subject, 1])
                    else:
                        iventar.inventory[choice_number][0].using(pleeer) # Используем предмет
                    if iventar.inventory[choice_number][1] == 0:
                        del iventar.inventory[choice_number] # Если количество предметов закончилось, он удаляется из инв
                #print(f'{[f"{i[0].title}/{i[1]}" for i in iventar.inventory]} / {[i.title for i in pleeer.equipment.values() if i != ""]}')
        elif battle_men.aktv == True:
            if self.ataw == 1:
                if ost_pyt[self.ataw][0].additional_key == True:
                    self.pyt = []
                    self.ataw = 1
                    ost_pyt[self.ataw][0].additional_key = False
                    batlee.enemy_list[batlee.choise].HP -= pleeer.specifications['Атака']
                    batlee.bat(pati)
                else:
                    ost_pyt[self.ataw][0].additional_key = True
            elif self.ataw == 2:
                if ost_pyt[self.ataw][0].ak == False:
                    ost_pyt[self.ataw][0].ak = True
                elif ost_pyt[self.ataw][0].ak == True and ost_pyt[self.ataw][0].additional_key == False:
                    ost_pyt[self.ataw][0].additional_key = True
                elif ost_pyt[self.ataw][0].ak == True and ost_pyt[self.ataw][0].additional_key == True:
                    if ost_pyt[self.ataw][0].p < len(pleeer.spells):
                        self.pyt = []
                        self.ataw = 1
                        ost_pyt[self.ataw][0].additional_key = False
                        ost_pyt[self.ataw][0].p = 0
                        ost_pyt[self.ataw][0].ak = False
                        pleeer.spells[ost_pyt[self.ataw][0].p].using(pleeer, pati, batlee.enemy_list, batlee.enemy_list[batlee.choise])
                        batlee.bat(pati)   
            elif self.ataw == 3:
                if ost_pyt[self.ataw][0].ak == False:
                    ost_pyt[self.ataw][0].ak = True
                elif ost_pyt[self.ataw][0].ak == True and ost_pyt[self.ataw][0].additional_key == False:
                    ost_pyt[self.ataw][0].additional_key = True
                elif ost_pyt[self.ataw][0].ak == True and ost_pyt[self.ataw][0].additional_key == True:
                    if ost_pyt[self.ataw][0].p < len(pleeer.adility):
                        self.pyt = []
                        self.ataw = 1
                        ost_pyt[self.ataw][0].additional_key = False
                        ost_pyt[self.ataw][0].p = 0
                        ost_pyt[self.ataw][0].ak = False
                        pleeer.adility[ost_pyt[self.ataw][0].p].using(pleeer, pati, batlee.enemy_list, batlee.enemy_list[batlee.choise])
                        batlee.bat(pati)
            elif self.ataw == 5:
                if random.randint(1, 101) > 50:
                    battle_men.aktv = False
                    self.pyt = []
                    self.ataw = 1
                    ost_pyt[self.ataw][0].additional_key = False
                    ost_pyt[self.ataw][0].p = 0
                    ost_pyt[self.ataw][0].ak = False
                else:
                    batlee.bat(pati)
            else:
                ost_pyt[self.ataw][0].ak = True
        elif dialog_men.aktv == True:
            if text.xod == False:
                text.blok += 1
                if text.blok >= len(text.ob_text):
                    dialog_men.aktv = False
                text.stroka = 0
                text.xod = True
            elif text.xod == True:
                text.stroka = len(text.ob_text[text.blok]) -1 
                text.xod == False
        else:
            ost_pyt[self.ataw][0].ak = True
inven = meni(x)
men_batlle_ram = pg.image.load(script.guide.path + "\\aset\\men\\ramka_g_m_b.png").convert_alpha()
men_batlle_v = pg.image.load(script.guide.path + "\\aset\\men\\ramka_p_sc.png").convert_alpha()
men_batlle = pg.image.load(script.guide.path + "\\aset\\men\\oc_m_b.png").convert_alpha()
battle_men = meni(
    (
        (('Низ', 'Верх'), 5),
    (
        spreadsheet(s=men_batlle, dop_sprai=[[men_batlle_ram, (0, 564)],], additional_tap=script.enemy.batlee.peredv, dop_ot=script.enemy.batlee.maping, ak=True, inactive_display=[maping, pati]),
        #spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\men_ive_important.png").convert_alpha(), s_r=ramka_inventar, n_r=(560, 75), p_r=(266, 25), g_r=(1360, 500), tab=((iventar.sorti, ), 2), prin_tab=iventar.otrisovka)
    ),
    (
        spreadsheet(s=men_batlle, s_r=men_batlle_v, dop_sprai=[[men_batlle_ram, (0, 604)],], additional_tap=script.enemy.batlee.peredv, dop_ot=script.enemy.batlee.maping, n_r=(160, 564), p_r=(300, 20), g_r=(1360, 768), prin_tab=display_abilities.rendering_interface, tab=((pleeer.spells, ), False), inactive_display=[maping, pati]),
    ),
    (
        spreadsheet(s=men_batlle, s_r=men_batlle_v, dop_sprai=[[men_batlle_ram, (0, 644)],], additional_tap=script.enemy.batlee.peredv, dop_ot=script.enemy.batlee.maping, n_r=(160, 564), p_r=(300, 20), g_r=(1360, 768), prin_tab=display_abilities.rendering_interface, tab=((pleeer.adility, ), False), inactive_display=[maping, pati]),
    ),
    (
        spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\men_ive_items.png").convert_alpha(), dop_sprai=[[men_batlle, (0,0)], [men_batlle_ram, (0,684)]], dop_ot=script.enemy.batlee.maping, s_r=ramka_inventar, n_r=(560, 75), p_r=(266, 25), g_r=(1360, 500), tab=((iventar.sorti, ), 0), prin_tab=iventar.otrisovka, inactive_display=[maping, pati]),
    ),
    (
        spreadsheet(s=men_batlle, dop_sprai=[[men_batlle_ram, (0, 724)]], ak=True, inactive_display=[maping, pati]),
    ),
    )
    )
dialog_men = meni(
    (
        (('Низ', 'Верх'), 1),
    (
        spreadsheet(s=pla, ak=True, dop_ot=text.otr),
    ),
    )
    )
men_list = [inven, battle_men, dialog_men]