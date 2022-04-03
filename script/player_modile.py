#from script.inven import iventar, f1
class Pleeer:
    def __init__(self, name, maxhp, maxmp, msp,
        ataka, pro, mag, wil, agil, dext,
        accuracy = 80, critic = 5, dodg = 5, mag_dodge = 0, counte_str = 0, counte_str_mag = 0,
        cru = 100, cu = 100, pie = 100, sh_l = 100, sh_h = 100, ea = 100, wa = 100, fi = 100,
        ai = 100, lig = 100, da = 100): 
        self.condition = [] # Сдесь будут эфекты от зелья во время боя
        self.name = name                     #0 Имя игрока незнаю зачем нужно, ведь в сюжете оно не будет использоватся, но если что вырежу
        self.HP = maxhp                      #1 Хп что на данный момент имеется у игрока      
        self.MP = maxmp                      #2 Мана что на данный момент имеется у игрока     
        self.SP = 0                          #3 Очки способностей что на данный момент имеются у игрока   
        self.MaxHP = maxhp                   #4 Максимальное возможное количество хп у игрока       
        self.MaxMP = maxmp                   #5 Максимальное возможное количество маны у игрока
        self.MaxSP = msp                     #6 Максимальное возможное количество очков способностей у игрока
        #=-\
            # Характиристики        
        self.ataka = ataka                   #7 Урон что будет сумироватся с оружием
        self.pro = pro                       #8 Защита, будет сумироватся с бронёй
        self.mag = mag                       #9 Магический урон, будет сумироватся с эфектом заклинания: Защитой, Уроном и т.д
        self.wil = wil                       #10 Воля, наверное самая редко используемая характеристка, будет влиять на контроль и испуг
        self.agil = agil                     #11 Ловкость будет влиять на те или иные способности 
        self.dext = dext                     #12 Сноровка, будет влиять на шанс наподения противников опять таки возможно на те или иные способности
        #=-/
        self.specifications = {'Атака': ataka, 'Защита': pro, 'Магия': mag, 'Воля': wil, 'Ловкость': agil, 'Сноровка': dext}
        #=-\
            # Шансы       
        self.accuracy = accuracy             #13 Шанс попадание атакой, комисия по балансу игры ещё решает будет ли это влиять на заклинания
        self.critic = critic                 #14 Шанс критического попадания тут всё понятно, скорее всего будет в двое меньшем шансе работать на способности # Способности всё ещё в разработке
        self.dodg = dodg                     #15 Шанс уворота от атак/способностей
        self.mag_dodge = mag_dodge           #16 Шанс уворота от заклинаний
        self.counte_str = counte_str         #17 Шанс контр атаки/способности 
        self.counte_str_mag = counte_str_mag #18 Шанс контр заклинании
        #=-/
        self.chances = {"Попадание": accuracy, 'Критическое': critic, 'Уворот': dodg, 'Магический уворот': mag_dodge, 'Контр атака': counte_str, 'Контр заклинание': counte_str_mag}
        #=-\
            # Сопротивления        
        self.crushing = cru                       #19 Дробящее сопротивление
        self.cutting = cu                         #20 Режущее сопротивление
        self.piercing = pie                       #21 Пронзающее сопротивление
        self.weak_ranged = sh_l                     #22 Стрелковое лёгкое сопротивление
        self.strong_ranged = sh_h                     #23 Стрелковое тяжолое сопротивление
        self.earth = ea                         #24 Земляное сопротивление
        self.water = wa                         #25 Водное сопротивление
        self.fire = fi                         #26 Огненое сопротивление
        self.air = ai                         #27 Воздушное сопротивление
        self.holy = lig                       #28 Святое сопротивление
        self.dark = da                         #29 Тёмное сопротивление
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
        self.equipment = {'Голова': '',
                        'Туловище': '',
                        'Ноги': '',
                        'Оружие_0': '',
                        'Оружие_1': '',
                        'Кольцо_0': '',
                        'Кольцо_1': '', 
                        'Кольцо_2': ''}
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
    def state_step(self):
        for creature in self.condition:
            creature.duration -= 1
            if creature.duration == 0:
                creature.duration = creature.total_duration
                creature.using(reverse_application=True)
                del self.condition[self.condition.index[creature]]
pleeer = Pleeer('Pler', 20, 10, 3, 5, 3, 2, 3, 5, 2)
vrag = Pleeer('Vrag', 20, 10, 3, 5, 3, 2, 3, 5, 2, dodg=30)