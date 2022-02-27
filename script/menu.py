from script.start_game import win, pg
import script.guide
# script.guide.path
from script.inven import *
from script.player_modile import pleeer
from script.modile_interface import showing_properties, gr
ramka_inventar = pg.image.load(script.guide.path + "\\aset\\men\\ramka_inven.png").convert_alpha()
class spreadsheet:
    def __init__(self, s, n_r=(0,0), p_r=(0,0), s_r='', g_r=(0,0), tab=[], prin_tab='', text=(('', (0, 0, 0), (0, 0)), ), inactive_display='') -> None:
        self.sprait = s # Спрайт
        self.sprait_ram = s_r # Спрайт рамки
        self.start_coordinates = n_r # Начальные координаты рамки
        self.moving_coordinates = p_r # координаты передвежения рамки
        self.p = 1 # Выбор предмета в списке + передвежение рамки
        self.p1 = g_r # Границы передвежения рамки
        self.p2 = '' # Границф
        self.list_getting_table = tab # Таблица с которой надо работать ((преобразующие функии/словари), начальный аргумент)
        self.prin_tab = prin_tab # Принцип отрисовки таблицы
        self.ak = False # Активность таблицы
        self.inactive_display = ''
        if s_r == '':
            self.ak = None
    @property
    def table_list(self): # Нужно для состовления нужного списка для таблицы
        x = self.list_getting_table[0]
        b = self.list_getting_table[1]
        for i in x:
            if isinstance(i, dict):
                b = i[b]
            else:
                b = i(b)
        return b
    # self.start_coordinates=(560, 75), self.moving_coordinates=(285, 25), self.p1=(1360, 500)
    def draw(self):
        if self.ak == True:
            kol_pr = self.p
            y = self.start_coordinates[1]
            while kol_pr >= 3:
                kol_pr -= 3
                y += self.moving_coordinates[1]
            win.blit(self.sprait_ram, (self.start_coordinates[0] + self.moving_coordinates[0] * kol_pr, y))
    def peredwe(self, kyda):
        x = (self.start_coordinates[0] - self.p1[0]) // self.moving_coordinates[0]
        slow = {'Низ': -x, 'Верх': x, 'Право': 1, 'Лево': -1}
        if self.p + slow[kyda] > 0:
            self.p += slow[kyda]
        print(self.p)
men_os = pg.image.load(script.guide.path + "\\aset\\men\\oc_okn.png").convert_alpha()
ram_cn = pg.image.load(script.guide.path + "\\aset\\men\\ram_cn.png").convert_alpha()
x = (
    (('Низ', 'Верх'), 7),
    (spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Back.png").convert_alpha()), ),
    (spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Items.png").convert_alpha()), (
        # (s(), ),
        (('Право', 'Лево'), 3),
        (spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\men_ive_items.png").convert_alpha(), s_r=ramka_inventar, n_r=(560, 75), p_r=(285, 25), g_r=(1360, 500), tab=((iventar.sorti, ), 0), prin_tab=iventar.otrisovka), ), 
        (spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\men_ive_equipment.png").convert_alpha(), s_r=ramka_inventar, n_r=(560, 75), p_r=(285, 25), g_r=(1360, 500), tab=((iventar.sorti, ), 1), prin_tab=iventar.otrisovka), ),  
        (spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\men_ive_important.png").convert_alpha(), s_r=ramka_inventar, n_r=(560, 75), p_r=(285, 25), g_r=(1360, 500), tab=((iventar.sorti, ), 2), prin_tab=iventar.otrisovka), ))),
    (spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Quests.png").convert_alpha()), ),
    (spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Equipment.png").convert_alpha()), (
        (('Низ', 'Верх'), 8),
        (spreadsheet(s=men_os, s_r=ram_cn, n_r=(484, 0), p_r=(136, 28), g_r=(1360, 768), tab=((pleeer.equipment, iventar.sorti), 'Голова'), prin_tab=gr.rendering_interface, inactive_display=(showing_properties, pleeer.equipment['Голова'])), ), )),
    (spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Saving.png").convert_alpha()), ),
    (spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Loading.png").convert_alpha()), ),
    (spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Exit.png").convert_alpha()), )
)
# iventar.sorti(pleeer.equipment['Голова']) ((pleeer.equipment, iventar.sorti), 'Голова')
men_ = spreadsheet(s=pg.image.load(script.guide.path + "\\aset\\men\\Back.png").convert_alpha(),
                s_r=pg.image.load(script.guide.path + "\\aset\\men\\ramka.png").convert_alpha(),
                n_r=(400, 400), p_r=(10, 10), g_r=(800, 800))
akt_fn = None
class meni:
    def __init__(self, spis) -> None:
        self.spis = spis
        self.pyt = []
        self.ataw = 1
        self.ataw_fun = 0
        self.aktv = False
    def fkl(self):
        ost_pyt = self.spis
        if len(self.pyt) != 0:
            for i in self.pyt:
                ost_pyt = ost_pyt[i]
        if ost_pyt[self.ataw][0].ak == True:
            ost_pyt[self.ataw][0].ak = False
            ost_pyt[self.ataw][0].p = 1
        elif self.aktv == False:
            self.aktv = True
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
        if len(self.pyt) != 0:
            for i in self.pyt:
                ost_pyt = ost_pyt[i]
        if ost_pyt[self.ataw][0].ak == True:
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
        if len(self.pyt) != 0:
            for i in self.pyt:
                ost_pyt = ost_pyt[i]
        if ost_pyt[self.ataw][0].ak == None:
            self.pyt.append(self.ataw)
            self.pyt.append(1)
            self.ataw = 1
        elif ost_pyt[self.ataw][0].ak == True and len(ost_pyt[self.ataw]) == 1:
            if ost_pyt[self.ataw][0].p - 1 <= len(ost_pyt[self.ataw][0].table_list):
                choice_number = [i for i in range(len(iventar.inventory)) if iventar.inventory[i][0] == ost_pyt[self.ataw][0].table_list[ost_pyt[self.ataw][0].p - 1][0]][0]
                iventar.inventory[choice_number][1] = iventar.inventory[choice_number][1] - 1
                iventar.inventory[choice_number][0].using(pleeer)
                if iventar.inventory[choice_number][1] == 0:
                    del iventar.inventory[choice_number]
            print(f'Пусто! {[f"{i[0].title}/{i[1]}" for i in iventar.inventory]}')
        else:
            ost_pyt[self.ataw][0].ak = True
inven = meni(x)