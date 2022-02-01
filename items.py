from script.player_modile import *
class thing: # Предмет
    list_of_items = {}
    '''
    Начальный класс
    '''
    def __init__(self, title='', ataka=0, pro=0, mag=0, wil=0, agil=0, dext=0,
        accuracy = 0, critic = 0, dodg = 0, mag_dodge = 0, counte_str = 0, counte_str_mag = 0,
        cru = 0, cu = 0, pie = 0, sh_l = 0, sh_h = 0, ea = 0, wa = 0, fi = 0,
        ai = 0, lig = 0, da = 0):
        self.title = title
        thing.list_of_items[title] = self
        self.specifications = {'Атака': ataka, 'Защита': pro, 'Магия': mag, 'Воля': wil, 'Ловкость': agil, 'Сноровка': dext}
        [self.specifications.pop(i, None) for i in list(filter(lambda x: self.specifications[x] == 0, self.specifications.keys()))]
        self.chances = {"Попадание": accuracy, 'Критическое': critic, 'Уворот': dodg, 'Магический уворот': mag_dodge, 'Контр атака': counte_str, 'Контр заклинание': counte_str_mag}
        [self.chances.pop(i, None) for i in list(filter(lambda x: self.chances[x] == 0, self.chances.keys()))]
        self.resistance = {'Дробящий': cru, 'Режущий': cu, 'Пронзающий': pie, 'Стрелковый лёгкий': sh_l, 'Стрелковый тяжолый': sh_h, 'Земленой': ea, 'Водный': wa, 'Огненый': fi, 'Воздушный': ai, 'Святой': lig, 'Тёмный': da} 
        [self.resistance.pop(i, None) for i in list(filter(lambda x: self.resistance[x] == 0, self.resistance.keys()))]
class food(thing): # Еда
    def __init__(self, title, mp=0, hp=0) -> None:
        thing.list_of_items[title] = self
        self.title = title
        self.HP = hp
        self.MP = mp
    def using(self, name_obj):
        name_obj.HP += self.HP
        if name_obj.HP > name_obj.MaxHP:
            name_obj.HP = name_obj.MaxHP
        name_obj.MP += self.MP
        if name_obj.MP > name_obj.MaxMP:
            name_obj.MP = name_obj.MaxMP           
class potion(thing): # Зелья
    def __init__(self, title='', mp=0, hp=0, ataka=0, pro=0, mag=0, wil=0, agil=0, dext=0, accuracy=0, critic=0, dodg=0, mag_dodge=0, counte_str=0, counte_str_mag=0, cru=0, cu=0, pie=0, sh_l=0, sh_h=0, ea=0, wa=0, fi=0, ai=0, lig=0, da=0, duration=0):
        super().__init__(title, ataka, pro, mag, wil, agil, dext, accuracy, critic, dodg, mag_dodge, counte_str, counte_str_mag, cru, cu, pie, sh_l, sh_h, ea, wa, fi, ai, lig, da)
        self.HP = hp
        self.MP = mp
        self.duration = duration # временное время действия 
        self.total_duration = duration # Постояниое время действия
    def using(self, name_obj, reverse_application=False):
        if reverse_application == False:
            name_obj.HP += self.HP
            if name_obj.HP > name_obj.MaxHP:
                name_obj.HP = name_obj.MaxHP
            name_obj.MP += self.MP
            if name_obj.MP > name_obj.MaxMP:
                name_obj.MP = name_obj.MaxMP   
            if self.duration > 0: # Если зелеe не временное и премененно не в бою оно не может давать такие навыки
                for key in self.specifications.keys():
                    name_obj.specifications[key] += self.specifications[key]
                for key in self.chances.keys():
                    name_obj.chances[key] += self.chances[key]
                for key in self.resistance.keys():
                    name_obj.resistance[key] += self.resistance[key]
                name_obj.condition.append(self)
        else:
            for key in self.specifications.keys():
                name_obj.specifications[key] -= self.specifications[key]
            for key in self.chances.keys():
                name_obj.chances[key] -= self.chances[key]
            for key in self.resistance.keys():
                name_obj.resistance[key] -= self.resistance[key]            
class equipment(thing): # Снарежение
    '''
    Промежуточный класс нужный для единых команд снаряжения, к примеру вывода характеристик в меню снарежения
    '''
    def __init__(self, kind, title='', ataka=0, pro=0, mag=0, wil=0, agil=0, dext=0, accuracy=0, critic=0, dodg=0, mag_dodge=0, counte_str=0, counte_str_mag=0, cru=0, cu=0, pie=0, sh_l=0, sh_h=0, ea=0, wa=0, fi=0, ai=0, lig=0, da=0):
        super().__init__(title, ataka, pro, mag, wil, agil, dext, accuracy, critic, dodg, mag_dodge, counte_str, counte_str_mag, cru, cu, pie, sh_l, sh_h, ea, wa, fi, ai, lig, da)
        self.kind = kind # Вид/класс 
    def derivation_of_characteristics(self): # Вывод характеристик на экран
        pass
class armor(equipment): # Броня/снарежение
    def __init__(self, kind, title='', maxmp=0, maxhp=0, ataka=0, pro=0, mag=0, wil=0, agil=0, dext=0, accuracy=0, critic=0, dodg=0, mag_dodge=0, counte_str=0, counte_str_mag=0, cru=0, cu=0, pie=0, sh_l=0, sh_h=0, ea=0, wa=0, fi=0, ai=0, lig=0, da=0):
        super().__init__(kind, title, ataka, pro, mag, wil, agil, dext, accuracy, critic, dodg, mag_dodge, counte_str, counte_str_mag, cru, cu, pie, sh_l, sh_h, ea, wa, fi, ai, lig, da)
        self.MaxMP = maxmp
        self.MaxHP = maxhp
    def using(self, name_obj, reverse_application=False):
        if reverse_application == False:
            name_obj.MaxMP += self.MaxMP
            name_obj.MaxMP += self.MaxMP
            for key in self.specifications.keys():
                name_obj.specifications[key] += self.specifications[key]
            for key in self.chances.keys():
                name_obj.chances[key] += self.chances[key]
            for key in self.resistance.keys():
                name_obj.resistance[key] += self.resistance[key]
        else:
            name_obj.MaxMP -= self.MaxMP
            name_obj.MaxMP -= self.MaxMP
            for key in self.specifications.keys():
                name_obj.specifications[key] -= self.specifications[key]
            for key in self.chances.keys():
                name_obj.chances[key] -= self.chances[key]
            for key in self.resistance.keys():
                name_obj.resistance[key] -= self.resistance[key]   
class arms(equipment): # Оружие/снарежение
    def __init__(self, kind, title='', ataka=0, pro=0, mag=0, wil=0, agil=0, dext=0, accuracy=0, critic=0, dodg=0, mag_dodge=0, counte_str=0, counte_str_mag=0, cru=0, cu=0, pie=0, sh_l=0, sh_h=0, ea=0, wa=0, fi=0, ai=0, lig=0, da=0):
        super().__init__(kind, title, ataka, pro, mag, wil, agil, dext, accuracy, critic, dodg, mag_dodge, counte_str, counte_str_mag, cru, cu, pie, sh_l, sh_h, ea, wa, fi, ai, lig, da)
    def using(self, name_obj, reverse_application=False):
        if reverse_application == False:
            for key in self.specifications.keys():
                name_obj.specifications[key] += self.specifications[key]
            for key in self.chances.keys():
                name_obj.chances[key] += self.chances[key]
            for key in self.resistance.keys():
                name_obj.resistance[key] += self.resistance[key]
        else:
            for key in self.specifications.keys():
                name_obj.specifications[key] -= self.specifications[key]
            for key in self.chances.keys():
                name_obj.chances[key] -= self.chances[key]
            for key in self.resistance.keys():
                name_obj.resistance[key] -= self.resistance[key] 
potion(title='F', pro='Bel')
potion(title='Fk', pro='Bel')
potion(title='j', pro='Bel')
potion(title='u', pro='Bel')
print(thing.list_of_items)
#pleeer