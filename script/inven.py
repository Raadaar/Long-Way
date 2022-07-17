from script.start_game import win, f1
from script.items import food, armor, arms, ring, thing, equipment
ibi = ['Голова', 'Туловище', 'Ноги', 'Оружие', 'Щит', 'Кольцо_0', 'Кольцо_1', 'Кольцо_2']
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
            sor = (food, )
        elif uslow == 1:
            sor = (arms, armor, ring)
        else:
            sor = (thing, )
        if isinstance(uslow, equipment):
            sort_spik = [d for d in [i for i in self.inventory if isinstance(i[0], equipment)] if d[0].kind == uslow.kind] # В первом кругу проверяется является ли предмет снарежением, во втором является ли вид снарежение одинаковым, если это не оружие
        elif uslow == '':
            return sort_spik
        else:
            for it in self.inventory:
                if isinstance(it[0], sor):
                    sort_spik.append(it)
        return sort_spik
    def equipment_sorti(self, pack):
        sample, subsample = pack
        if '_' in subsample:
            pass
        subsample = subsample[:subsample.find('_')] if '_' in subsample else subsample
        return [i for i in self.inventory if isinstance(i[0], sample) and i[0].kind == subsample]
    # Добовляет предмет в инвентарь, если такой уже есть, добовляет к количеству существующего
    def dopov(self, pr):
        prov = False
        for i in range(len(self.inventory)):
            if self.inventory[i][0] == pr[0]:
                prov = True       
                self.inventory[i][1] += pr[1]
                break
        if prov == False:
            self.inventory.append(pr)
    # Отрисовывает название вещей в инвенторе
    def otrisovka(self, spis, osnova):
        visata = 75
        dlina = 275
        perexod = 0
        for i in spis:
            perexod += 1
            dlina += 285
            win.blit(f1.render(str(i[0].title), True, (180, 0, 0)), (dlina, visata))             
            win.blit(f1.render(str(i[1]), True, (180, 0, 0)), (dlina + 220, visata))            
            if perexod == 3:
                perexod = 0
                visata += 25
                dlina = 275
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