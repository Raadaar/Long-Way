from math import ceil
import random
class skill:
    skill_dictionary = {}
    def __init__(self, title, application, action, dam, time=0, view='') -> None:
        skill.skill_dictionary[title] = self
        self.title = title # Название
        self.application = application # Будет примененно для одиночной цели, всем или случайно [один, мас, случайно]
        self.action = action # Баф, дебаф, наполнение, урон 
        self.time = time # Время действия
        self.dam = dam # {'' : 0}  Вид : значение
        self.view = view # Какой будет вид
    def positive_effect(self, user, choice):
        if choice == True:
            for d in [user.specifications, user.chances, user.resistance]:
                for i in self.dam.keys():
                    if i in d:
                        d[i] += self.dam[i]
        else:
            for d in [user.specifications, user.chances, user.resistance]:
                for i in self.dam.keys():
                    if i in d:
                        d[i] -= self.dam[i]
    def negative_effect(self, user, choice):
        if choice == True:
            for d in [user.specifications, user.chances, user.resistance]:
                for i in self.dam.keys():
                    if i in d:
                        d[i] -= self.dam[i]
        else:
            for d in [user.specifications, user.chances, user.resistance]:
                for i in self.dam.keys():
                    if i in d:
                        d[i] += self.dam[i]
    def replenishment(self, user):
        for i in self.dam.keys():
            if self.view == 'Магия':
                user.MP += ceil((user.resistance[i] / self.dam[i]) * 100)
                if user.MP > user.MaxMP:
                    user.MP = user.MaxMP
            elif self.view == 'Жизнь':
                user.HP += ceil((user.resistance[i] / self.dam[i]) * 100)
                if user.HP > user.MaxHP:
                    user.HP = user.MaxHP
    def skill_damage(self, user):
        for i in self.dam.keys():
            user.HP -= ceil((self.dam[i] / user.resistance[i]) * 100)
    def using(self, utilizing, command, host, choice): # Использующий, его пати и пати врагов и выбранный враг (необезательный, время действия)
        activity_dictionary = {'баф': self.positive_effect, 'дебаф': self.negative_effect, 'наполнение': self.replenishment, 'урон': self.skill_damage}
        condition = []
        if self.action == 'баф':
            if self.application == 'один':
                activity_dictionary['баф'](command[choice], True)
                command[choice].condition.append([self.action, activity_dictionary['баф'], self.time])
            elif self.application == 'мас':
                for i in range(len(command)):
                    activity_dictionary['баф'](command[i], True)
                    command[i].condition.append([self.action, activity_dictionary['баф'], self.time])
            else:
                ch = random.randint(0, len(command) - 1)
                activity_dictionary['баф'](command[ch], True)
                command[ch].condition.append([self.action, activity_dictionary['баф'], self.time])
        elif self.action == 'дебаф':
            if self.application == 'один':
                activity_dictionary['дебаф'](host[choice], True)
                host[choice].condition.append([self.action, activity_dictionary['дебаф'], self.time])
            elif self.application == 'мас':
                for i in range(len(host)):
                    activity_dictionary['дебаф'](host[i], True)
                    host[i].condition.append([self.action, activity_dictionary['дебаф'], self.time])
            else:
                ch = random.randint(0, len(host) - 1)
                activity_dictionary['дебаф'](host[ch], True)
                host[ch].condition.append([self.action, activity_dictionary['дебаф'], self.time])            
        elif self.action == 'наполнение':
            if self.application == 'один':
                command[choice].condition.append([self.action, activity_dictionary['наполнение'], self.time])
            elif self.application == 'мас':
                for i in range(len(command)):
                    command[i].condition.append([self.action, activity_dictionary['наполнение'], self.time])
            else:
                ch = random.randint(0, len(command) - 1)
                command[ch].condition.append([self.action, activity_dictionary['наполнение'], self.time])
        elif self.action == 'урон':
            if self.application == 'урон':
                host[choice].condition.append([self.action, activity_dictionary['урон'], self.time])
            elif self.application == 'мас':
                for i in range(len(host)):
                    host[i].condition.append([self.action, activity_dictionary['урон'], self.time])
            else:
                ch = random.randint(0, len(host) - 1)
                host[ch].condition.append([self.action, activity_dictionary['урон'], self.time])
class class_ability(skill):
    ability_dictionary = {}
    def __init__(self, title, application, action, dam, consumption, time=0, view='') -> None:
        super().__init__(title, application, action, dam, time, view)
        class_ability.ability_dictionary[self.title] = self
        self.consumption = consumption # Потребление очков способности
    def using(self, utilizing, command, host, choice):
        utilizing.SP = utilizing.SP - self.consumption if utilizing.SP - self.consumption >= 0 else 0
        return super().using(utilizing, command, host, choice)
class class_magic(skill):
    magic_dictionary = {}
    def __init__(self, title, application, action, dam, consumption, time=0, view='') -> None:
        super().__init__(title, application, action, dam, time, view)
        class_magic.magic_dictionary[self.title] = self
        self.consumption = consumption # Потребление магии
    def using(self, utilizing, command, host, choice):
        utilizing.MP = utilizing.MP - self.consumption if utilizing.MP - self.consumption >= 0 else 0
        return super().using(utilizing, command, host, choice) 
def converting_text_to_skill(skil):
    e = ["Баф", "дебаф", "наполнение", "урон"]
    sl = {}
    tim = 0
    view = ''
    if 'Время' in skil[4]:
        tim = skil[4].split('/')[1]
        del skil[4]
    if skil[4] in ['Магия', 'Жизнь']:
        view = skil[4]
        del skil[4]
    for i in skil[4:]:
        s = i.split('/')
        sl[s[0]] = int(s[1])
    if skil[3][0] == 'м':
        class_magic(skil[0], skil[1], skil[2], sl, int(skil[3].split('/')[1]), time=tim, view=view)
    else:
        class_ability(skil[0], skil[1], skil[2], sl, int(skil[3].split('/')[1]), time=tim, view=view)
# script/
with open('script/skill.txt', 'r', encoding='utf-8') as file:
    for line in file:
        converting_text_to_skill(line.strip().split('_'))
