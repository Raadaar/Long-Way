from script.player_modile import *
class thing: # Предмет
    list_of_items = {}
    '''
    Начальный класс
    '''
    def __init__(self, title='', ataka=0, pro=0, mag=0, wil=0, agil=0, dext=0,
        accuracy=0, critic=0, dodg=0, mag_dodge=0, counte_str=0, counte_str_mag=0,
        cru=0, cu=0, pie=0, sh_l=0, sh_h=0, ea=0, wa=0, fi=0,
        ai=0, lig=0, da=0):
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
class ring(equipment):
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
def converting_things_from_text_format_to_game_class(ite):
    index_dictionary = ['Атака', 'Защита', 'Магия', 'Воля', 'Ловкость', 'Сноровка',
                        "Попадание", 'Критическое', 'Уворот', 'Магический уворот', 'Контр атака', 'Контр заклинание',
                        'Дробящий', 'Режущий', 'Пронзающий', 'Стрелковый лёгкий', 'Стрелковый тяжолый', 'Земленой', 'Водный', 'Огненый', 'Воздушный', 'Святой', 'Тёмный']
    item_class_dictionary = [0 for _ in range(27)]
    if ite[1] == 'Зелье':
        li = ['Maна', 'Здоровье', 'Длительность']
        index_dictionary.extend(li)
        item_class_dictionary.extend([0 for _ in range(len(li))])
        for i in range(2, len(ite)):
            sel = ite[i].split('=')  
            if sel[0] in index_dictionary:
                item_class_dictionary[index_dictionary.index(sel[0])] = int(sel[1])
            else:
                print(f'Ошибка №f4Ht неизвестный параметр _:{i}:_ в предмете {ite[0]}')
        potion(title=ite[0], ataka=item_class_dictionary[0], pro=item_class_dictionary[1], mag=item_class_dictionary[2], wil=item_class_dictionary[3], agil=item_class_dictionary[4], dext=item_class_dictionary[5], accuracy=item_class_dictionary[6], critic=item_class_dictionary[7], dodg=item_class_dictionary[8], mag_dodge=item_class_dictionary[9], counte_str=item_class_dictionary[10], counte_str_mag=item_class_dictionary[11], cru=item_class_dictionary[12], cu=item_class_dictionary[13], pie=item_class_dictionary[14], sh_l=item_class_dictionary[15], sh_h=item_class_dictionary[16], ea=item_class_dictionary[17], wa=item_class_dictionary[18], fi=item_class_dictionary[19], ai=item_class_dictionary[20], lig=item_class_dictionary[21], da=item_class_dictionary[22], mp=item_class_dictionary[23], hp=item_class_dictionary[24], duration=item_class_dictionary[25])
    elif 'Оружие' in ite[1]:
        for i in range(2, len(ite)):
            sel = ite[i].split('=')  
            if sel[0] in index_dictionary:
                item_class_dictionary[index_dictionary.index(sel[0])] = int(sel[1])
            else:
                print(f'Ошибка №f4Ht неизвестный параметр _:{i}:_ в предмете {ite[0]}')
        arms(kind=ite[1].split('/')[1],title=ite[0], ataka=item_class_dictionary[0], pro=item_class_dictionary[1], mag=item_class_dictionary[2], wil=item_class_dictionary[3], agil=item_class_dictionary[4], dext=item_class_dictionary[5], accuracy=item_class_dictionary[6], critic=item_class_dictionary[7], dodg=item_class_dictionary[8], mag_dodge=item_class_dictionary[9], counte_str=item_class_dictionary[10], counte_str_mag=item_class_dictionary[11], cru=item_class_dictionary[12], cu=item_class_dictionary[13], pie=item_class_dictionary[14], sh_l=item_class_dictionary[15], sh_h=item_class_dictionary[16], ea=item_class_dictionary[17], wa=item_class_dictionary[18], fi=item_class_dictionary[19], ai=item_class_dictionary[20], lig=item_class_dictionary[21], da=item_class_dictionary[22])
    elif 'Броня' in ite[1]:
        li = ['Максимальное количество здоровья', 'Максимальное количество магии']
        index_dictionary.extend(li)
        item_class_dictionary.extend([0 for _ in range(len(li))])
        for i in range(2, len(ite)):
            sel = ite[i].split('=')  
            if sel[0] in index_dictionary:
                item_class_dictionary[index_dictionary.index(sel[0])] = int(sel[1])
            else:
                print(f'Ошибка №f4Ht неизвестный параметр _:{i}:_ в предмете {ite[0]}')
        armor(kind=ite[1].split('/')[1],title=ite[0], ataka=item_class_dictionary[0], pro=item_class_dictionary[1], mag=item_class_dictionary[2], wil=item_class_dictionary[3], agil=item_class_dictionary[4], dext=item_class_dictionary[5], accuracy=item_class_dictionary[6], critic=item_class_dictionary[7], dodg=item_class_dictionary[8], mag_dodge=item_class_dictionary[9], counte_str=item_class_dictionary[10], counte_str_mag=item_class_dictionary[11], cru=item_class_dictionary[12], cu=item_class_dictionary[13], pie=item_class_dictionary[14], sh_l=item_class_dictionary[15], sh_h=item_class_dictionary[16], ea=item_class_dictionary[17], wa=item_class_dictionary[18], fi=item_class_dictionary[19], ai=item_class_dictionary[20], lig=item_class_dictionary[21], da=item_class_dictionary[22], maxmp=item_class_dictionary[23], maxhp=item_class_dictionary[24]) 
    elif ite[1] == 'Еда':  
        li = ['Maна', 'Здоровье']
        index_dictionary = li
        item_class_dictionary = [0 for _ in range(len(li))]
        for i in range(2, len(ite)):
            sel = ite[i].split('=')  
            if sel[0] in index_dictionary:
                item_class_dictionary[index_dictionary.index(sel[0])] = int(sel[1])
            else:
                print(f'Ошибка №f4Ht неизвестный параметр _:{i}:_ в предмете {ite[0]}')
        food(title=ite[0], mp=item_class_dictionary[0], hp=item_class_dictionary[1])
    elif ite[1] == 'Кольцо':  
        li = ['Максимальное количество здоровья', 'Максимальное количество магии']
        index_dictionary.extend(li)
        item_class_dictionary.extend([0 for _ in range(len(li))])
        for i in range(2, len(ite)):
            sel = ite[i].split('=')  
            if sel[0] in index_dictionary:
                item_class_dictionary[index_dictionary.index(sel[0])] = int(sel[1])
            else:
                print(f'Ошибка №f4Ht неизвестный параметр _:{i}:_ в предмете {ite[0]}')
        ring(kind=ite[1], title=ite[0], ataka=item_class_dictionary[0], pro=item_class_dictionary[1], mag=item_class_dictionary[2], wil=item_class_dictionary[3], agil=item_class_dictionary[4], dext=item_class_dictionary[5], accuracy=item_class_dictionary[6], critic=item_class_dictionary[7], dodg=item_class_dictionary[8], mag_dodge=item_class_dictionary[9], counte_str=item_class_dictionary[10], counte_str_mag=item_class_dictionary[11], cru=item_class_dictionary[12], cu=item_class_dictionary[13], pie=item_class_dictionary[14], sh_l=item_class_dictionary[15], sh_h=item_class_dictionary[16], ea=item_class_dictionary[17], wa=item_class_dictionary[18], fi=item_class_dictionary[19], ai=item_class_dictionary[20], lig=item_class_dictionary[21], da=item_class_dictionary[22], maxmp=item_class_dictionary[23], maxhp=item_class_dictionary[24]) 
with open('items.txt', 'r', encoding='utf-8') as file:
    for line in file:
        converting_things_from_text_format_to_game_class(line.strip().split('_'))
#pleeer