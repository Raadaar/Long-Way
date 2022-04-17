import random
import copy
import script.start_game as sg
import script.guide
from script.skill import skill, class_ability, class_magic
'''
Запуск игры
Загружается карта вместе с ней зоны с врагами
когда игрок передвигается в зоне может начатся бой
Во время боя активируется меню боя. В активный список врагов попадает список состоящий из случайного количество врагов из зоны в которой находился игрок
При совершений игроком конечных действий в меню (удар, применение способности, магии или предмета) ход дайтся врагам. А игрок возвращается в начало меню боя
Враги просмотривая список пати игрока руководствуясь рукописной логикой совершают действие
'''
# Зона боя
class combat_zone:
    def __init__(self, r, v, s) -> None:
        self.re = sg.pg.Rect(r) # Площадь
        self.enemis = v # Список врагов
        self.sprait_fon = s # Фоновый спрайт 
    def beginning_battle(self, sel):        
        sel.enemy_list = [copy.deepcopy(self.enemis[random.randint(0, len(self.enemis) - 1)]) for _ in range(random.randint(1, len(self.enemis)))] # Даёт случайное количество врагов от одного до бесконечности
        sel.sprait_fon = self.sprait_fon 
# Активный бой
class batlee_class:
    def __init__(self) -> None:
        self.enemy_list = [] # Список врагов
        self.sprait_fon = '' # Фоновый спрайт 
        self.choise = 0 # Выбранный враг
    def bat(self, pati):
        if len(self.enemy_list) > 0:
            for i in self.enemy_list:
                i.state_transition()
                if i.HP < 1:
                    del self.enemy_list[self.enemy_list.index(i)]
                else:                
                    i.combat_logic(self.enemy_list, pati)
            for i in pati:
                i.state_transition()
        else:
            pass
    def peredv(self, kyda):
        slow = {'Право': 1, 'Лево': -1}
        if kyda in slow:
            if self.choise + slow[kyda] >= 0:
                self.choise += slow[kyda]
                if self.choise == len(self.enemy_list):
                    self.choise = 0
    def maping(self, bat, fps): # mapping
        fps = fps.fps
        fps = (60 - fps if fps > 30 else fps)
        sg.win.blit(self.sprait_fon, (0, 0))
        p = 1360 // (len(self.enemy_list) + 1)
        x = 0
        for enem in self.enemy_list:
            spr = enemy_class.sprait[enem.name]
            x += p
            center = x - (spr.get_width() // 2)
            if enem == self.enemy_list[self.choise] and bat.additional_key == True:
                #sg.win.blit(spr, (center + fps, 100 + fps))
                sg.win.blit(sg.pg.transform.scale(spr, (spr.get_width() - fps, spr.get_height() - fps)), (center + fps // 2, 100 + fps // 2))
            else:
                sg.win.blit(spr, (center, 100))
            sg.pg.draw.rect(sg.win, (68, 148, 74), (center + 30, 90, round((enem.HP * (100 / enem.MaxHP)) * ((spr.get_width() - 30) / 100)), 10))
        # pg.draw.rect(win, (0, 100, 0), (680, 384, 50, 50))
        # get_width()
pati = []
batlee = batlee_class()
class enemy_class:
    list_of_enemy = {}
    sprait = {}
    '''
    Начальный класс
    '''
    def __init__(self, name, maxhp, maxmp, msp, sprait,
        ataka, pro, mag, wil, agil, dext,
        accuracy=80, critic=5, dodg=5, mag_dodge=0, counte_str= 0, counte_str_mag=0,
        cru=100, cu=100, pie=100, sh_l=100, sh_h=100, ea=100, wa=100, fi=100,
        ai = 100, lig = 100, da = 100):
        self.condition = []
        enemy_class.sprait[name] = sprait
        self.sprait = ''
        self.name = name
        self.HP = maxhp                      #1 Хп что на данный момент имеется у игрока      
        self.MP = maxmp                      #2 Мана что на данный момент имеется у игрока     
        self.SP = 0                          #3 Очки способностей что на данный момент имеются у игрока   
        self.MaxHP = maxhp                   #4 Максимальное возможное количество хп у игрока       
        self.MaxMP = maxmp                   #5 Максимальное возможное количество маны у игрока
        self.MaxSP = msp                     #6 Максимальное возможное количество очков способностей у игрока
        enemy_class.list_of_enemy[name] = self
        self.specifications = {'Атака': ataka, 'Защита': pro, 'Магия': mag, 'Воля': wil, 'Ловкость': agil, 'Сноровка': dext}
        #[self.specifications.pop(i, None) for i in list(filter(lambda x: self.specifications[x] == 0, self.specifications.keys()))]
        self.chances = {"Попадание": accuracy, 'Критическое': critic, 'Уворот': dodg, 'Магический уворот': mag_dodge, 'Контр атака': counte_str, 'Контр заклинание': counte_str_mag}
        #[self.chances.pop(i, None) for i in list(filter(lambda x: self.chances[x] == 0, self.chances.keys()))]
        self.resistance = {'Дробящий': cru, 'Режущий': cu, 'Пронзающий': pie, 'Стрелковый лёгкий': sh_l, 'Стрелковый тяжелый': sh_h, 'Земляной': ea, 'Водный': wa, 'Огненный': fi, 'Воздушный': ai, 'Святой': lig, 'Тёмный': da}
        #[self.resistance.pop(i, None) for i in list(filter(lambda x: self.resistance[x] == 0, self.resistance.keys()))]
        self.ability = []
        self.magic = []
    def state_transition(self):
        for pak in self.condition:
            if pak[0] in ('баф', 'дебаф'):
                if pak[2] > 0:
                    pak[2] -= 1
                else:
                    pak[1](self, False)
                    del self.condition[self.condition.index(pak)]
            elif pak[0] in ('наполнение', 'урон'):
                if pak[2] > 0:
                    pak[2] -= 1
                    pak[1](self)
                else:
                    pak[1](self)
                    del self.condition[self.condition.index(pak)]        

    def combat_logic(self, command, host):
        ch = random.choice(['Атака', 'Магия'])
        if ch == 'Атака':
            host[0].HP -= self.specifications['Атака']
        else:
            random.choice(self.magic).using(self, command, host, 0)
def converting_text_to_enemy_class(ite):
    list_skill = []
    index_dictionary = ['Атака', 'Защита', 'Магия', 'Воля', 'Ловкость', 'Сноровка',
                        "Попадание", 'Критическое', 'Уворот', 'Магический уворот', 'Контр атака', 'Контр заклинание',
                        'Дробящий', 'Режущий', 'Пронзающий', 'Стрелковый лёгкий', 'Стрелковый тяжелый', 'Земляной', 'Водный', 'Огненный', 'Воздушный', 'Святой', 'Тёмный']
    item_class_dictionary = [0 for _ in range(27)]
    for i in range(5, len(ite)):
        if '=' in ite[i]:
            sel = ite[i].split('=')  
            if sel[0] in index_dictionary:
                item_class_dictionary[index_dictionary.index(sel[0])] = int(sel[1])
            else:
                print(f'Ошибка №f4Ht неизвестный параметр _:{i}:_ в предмете {ite[0]}')
        elif ite[i] in skill.skill_dictionary.keys():
            list_skill.append(ite[i])
    enemy_class(ite[0], int(ite[1]), int(ite[2]), int(ite[3]), sg.pg.image.load(script.guide.path + f"\\aset\\{ite[4]}").convert_alpha(), item_class_dictionary[0], item_class_dictionary[1], item_class_dictionary[2], item_class_dictionary[3], item_class_dictionary[4], item_class_dictionary[5], accuracy=item_class_dictionary[6], critic=item_class_dictionary[7], dodg=item_class_dictionary[8], mag_dodge=item_class_dictionary[9], counte_str=item_class_dictionary[10], counte_str_mag=item_class_dictionary[11], cru=item_class_dictionary[12], cu=item_class_dictionary[13], pie=item_class_dictionary[14], sh_l=item_class_dictionary[15], sh_h=item_class_dictionary[16], ea=item_class_dictionary[17], wa=item_class_dictionary[18], fi=item_class_dictionary[19], ai=item_class_dictionary[20], lig=item_class_dictionary[21], da=item_class_dictionary[22]) 
    for i in list_skill:
        if isinstance(skill.skill_dictionary[i], class_magic):
            enemy_class.list_of_enemy[ite[0]].magic.append(skill.skill_dictionary[i])
        else:
            enemy_class.list_of_enemy[ite[0]].ability.append(skill.skill_dictionary[i])
with open('script/enemy.txt', 'r', encoding='utf-8') as file:
    for line in file:
        converting_text_to_enemy_class(line.strip().split('_'))
def life_check(ene):
    pass
#copy.deepcopy()
enemy_class.list_of_enemy['Злодей'].magic.append(class_magic.magic_dictionary['Земляной разлом v2'])
enemy_combat_zone = [combat_zone((0,0,20,20), [copy.deepcopy(enemy_class.list_of_enemy['Злодей']),copy.deepcopy(enemy_class.list_of_enemy['Злодей']),copy.deepcopy(enemy_class.list_of_enemy['Злодей']), ], sg.pg.image.load(script.guide.path + "\\aset\\sac_b_les.png").convert_alpha()), ]