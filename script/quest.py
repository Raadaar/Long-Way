from script.inven import iventar
from script.start_game import f0, win
# 1) Сделать до конца квесты
# 2) Проверить их работоспособность
# 3) Сделать барьеры
# Завтра
# 1) Сделать локу
# 2) Проверить на ней работоспособность квестов
# 3) Настроить баланс и закомпелировать пролог
class Turn:
    def __init__(self) -> None:
        self.round = []
    def check(self, text, coordinates):
        if len(self.round) > 0:
            if self.round[0][0] == 'текст':
                text[0].aktv = True
                text[1].text_update(self.round[0][1])
            elif self.round[0][0] == 'действие с квестом':
                for quest in Quest.quests:
                    if quest.name == 'Доп квест':
                        quest.activation(True)
            elif self.round[0][0] == 'телепортация':
                coordinates[1].rect[0], coordinates[1].rect[1] = self.round[0][1][0], self.round[0][1][1]
                coordinates[0].rect[0], coordinates[0].rect[1] = self.round[0][1][0], self.round[0][1][1]
                
                
            del self.round[0]
turn = Turn()
interaction_zones = []
activation_zones = []
class Promotion:
    def __init__(self, text, promotion, warp, priority, addiction) -> None:
        self.text = text # Описание задания
        self.promotion = promotion # Данные для задания
        self.warp = warp # Ссылка на основной квест
        self.priority = priority # Очерёдность
        self.addiction = addiction # Действия после выполнения
        self.condition = True
#    def check(self, data):        
class Kill(Promotion):
    def __init__(self, text, promotion, warp, priority, addiction=False) -> None:
        super().__init__(text, promotion, warp, priority, addiction)
    def check(self, data):
        if data[0] == 'уб' and self.condition == True:
            for name in data[1:]:
                if name == self.promotion[0]:
                    self.promotion[1] -= 1
            if self.promotion[1] <= 0:
                self.warp.addiction.append(self.priority)
                self.condition = False
                if self.addiction[0] == False:
                    self.warp.activation(False)
                if len(self.addiction) > 1:
                    for i in self.addiction[1]:
                        turn.round.append(i)
                return True
        return False
class Interaction_NPS(Promotion):
    def __init__(self, text, promotion, warp, priority, addiction) -> None:
        super().__init__(text, promotion, warp, priority, addiction)
    def check(self, data):
        if data[0] == 'НПС': 
            if data[1] == self.promotion[0] and self.condition == True:
                if len(self.promotion) == 3:
                    for i in iventar.inventory:
                        if i[0].title == self.promotion[1] and i[1] >= self.promotion[2]:
                            self.warp.addiction.append(self.priority)
                            self.condition = False
                            if self.addiction[0] == False:
                                self.warp.activation(False)
                            if len(self.addiction) > 1:
                                for i in self.addiction[1]:
                                    turn.round.append(i)
                else:                            
                    self.warp.addiction.append(self.priority)
                    self.condition = False
                    if self.addiction[0] == False:
                        self.warp.activation(False)
                    if len(self.addiction) > 1:
                        for i in self.addiction[1]:
                            turn.round.append(i)
            return True
        return False
class Interaction(Promotion):
    def __init__(self, text, promotion, warp, priority, addiction) -> None:
        super().__init__(text, promotion, warp, priority, addiction)
        self.rect = self.promotion
        interaction_zones.append(self.rect)
    def check(self, data):
        if data[0] == 'взаимодействие': 
            if data[1] == self.rect and self.condition == True:
                self.warp.addiction.append(self.priority)
                self.condition = False
                if self.addiction[0] == False:
                    self.warp.activation(False)
                if len(self.addiction) > 1:
                    for i in self.addiction[1]:
                        turn.round.append(i)   
                return True            
        return False
class Region(Promotion):
    def __init__(self, text, promotion, warp, priority, addiction) -> None:
        super().__init__(text, promotion, warp, priority, addiction)
        self.rect = self.promotion
        activation_zones.append(self.rect)
    def check(self, data):
        if data[0] == 'область': 
            if data[1] == self.rect and self.condition == True:
                self.warp.addiction.append(self.priority)
                self.condition = False
                if self.addiction[0] == False:
                    self.warp.activation(False)
                if len(self.addiction) > 1:
                    for i in self.addiction[1]:
                        turn.round.append(i)   
                return True   
        return False 
class Quest:
    quests = []
    def __init__(self, quest) -> None:
        self.name = quest[0]
        Quest.quests.append(self)
        self.activity = False # None неактивен, False закончен, True активен
        self.description = [] # Описание 
        self.choise = [] # Задачи для продвежение по квесту 
        pr = quest
        sl = {'уб':Kill, 'НПС':Interaction_NPS, 'взаимодействие':Interaction, 'область':Region}
        while True:
            self.description.append(pr[1])
            pak = []
            for qvest in range(len(pr[2])):
                pak.append(sl[pr[2][qvest][1][0]](pr[2][qvest][0], pr[2][qvest][1][1], self, qvest, pr[2][qvest][2]))
            self.choise.append(pak)
            if pr[3] != []:
                pr = pr[3]
            else:
                break
        self.addiction = [] # зависемости создаются на основе описания, если будут развилки они будут отмечатся в зависемости
    def search(data):
        for mini_quest in [i.choise for i in Quest.quests if i.activity == True]:
            for i in mini_quest:
                for d in i:
                    if d.check(data):
                        pass
    def activation(self, meaning):
        self.activity = meaning
        for bak in self.choise:
            for quest in bak:
                quest.condition = meaning
    def sort(sna):
        if sna:
            return [i for i in Quest.quests if i.activity == True]
        return [i for i in Quest.quests if i.activity == False]
    def otr(spis, osnova):
        visata = 60
        dlina = 0
        for i in range(len(spis)):
            win.blit(f0.render(str(spis[i].name), True, (180, 0, 0)), (dlina, visata * (i + 1))) 
        if len(spis) > osnova.p:
            akt = spis[osnova.p]
            win.blit(f0.render(str(akt.description[0]), True, (180, 56, 89)), (360, 0))  # Добавить возоможность распределения текста по экрану
            for i in range(len(akt.choise[0])):
                if akt.choise[0][i].condition:
                    win.blit(f0.render(str(akt.choise[0][i].text), True, (255, 0, 0)), (360, 45 * (i + 1)))
                else:
                    win.blit(f0.render(str(akt.choise[0][i].text), True, (68, 148, 74)), (360, 45 * (i + 1)))
        #perexod = 0
        #for i in spis:
        #    perexod += 1
        #    dlina += 285
        #    win.blit(f0.render(str(i[0].title), True, (180, 0, 0)), (dlina, visata))             
        #    win.blit(f0.render(str(i[1]), True, (180, 0, 0)), (dlina + 220, visata))            
        #    if perexod == 3:
        #        perexod = 0
        #        visata += 25
        #        dlina = 275
replenishment_queue = []

lineika = ['Начало',
            'Начало квеста: Нужно освоится в этом лесу или попытатся выбратся',
            [
            ['Убить 10 врагов', ['уб', ['Злодей', 100]], [None, [['текст', 'Вроде стало чище'],]]], # [Описание, требование, результат False конец квеста, True продолжение, доп скрипт [текст/новый квест/телепортация]]
            ['Поговорить с торговцем', ['НПС', ['name', 'text']], [None, [['действие с квестом', 'Доп квест', True],]]],
            ['Собрать цветок', ['взаимодействие', (750, 750, 50, 50)], [None, [['телепортация', (150, 150)],]]],
            ['Найти выход', ['область', (4215, 4550, 50, 50)], [None, [['текст', 'ура!!!'], ['телепортация', (300, 399)], ['текст', 'Блин!']]]]
            ],
            []]
gv_nps = ['Доп квест',
            'Описание квеста',
            [
            ['Принести 10 духовной энергии', ['НПС', ['name', 'духовная энергия', 1]], [False, []]],    
            ],
            []]
Quest(lineika)
Quest.quests[0].activation(True)
Quest(gv_nps)
test_areas = []