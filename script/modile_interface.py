from script.start_game import win, pg
import script.guide
f1 = pg.font.Font(script.guide.path + "\\Fonts\\Gabriola One.ttf", 26)
men_sn_ok = [pg.image.load(script.guide.path + "\\aset\\men\\oc_okn.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\dop_okn.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\dop_okn_n.png").convert_alpha(), pg.image.load(script.guide.path + "\\aset\\men\\dop_okn_v.png").convert_alpha()]
#
class interface:
    # Данный класс нужен для отображение 
    def __init__(self, spra, kor, son, sme, *spi_ind, s=True):
        # Необезательный аргумент отключающий показ спрайта
        self.show_sprait = s
        # Сам спрайт
        self.sprait = spra
        # Кординаты спрайта
        self.coordinates = kor
        # Начало и конец зоны отображение текста (начало(x, y): конец(x, y)) прим.(0, 0, 10, 200)
        self.dimensions = son
        # Смещение по x,y ячеек
        self.bias = sme
        # Список индексов и их расположения (или просто текста) в одном кортеже в ячейке по типу ((index, x, y), (index, x, y)))
        self.ind = spi_ind
    def rendering_interface(self, spi):
        if self.show_sprait == True:
            win.blit(self.sprait, self.coordinates)
        x = self.dimensions[0]
        y = self.dimensions[1]
        for i in spi:
            for d in self.ind:
                d(i, x, y)
            x += self.bias[0]
            if x == self.dimensions[2]:
                if y == self.dimensions[3]:
                    return
                x = self.dimensions[0]
                y += self.bias[1]
    def rendering_frame(self, ramka, kn):
        
        win.blit(ramka, ((self.dimensions[0] + kn * self.bias[0]) % self.dimensions[2], (self.dimensions[1] + kn * self.bias[1]) % self.dimensions[3]))
        pass
obw_od = interface(men_sn_ok[0], (0, 0), (50, 80, 50, 480), (0, 50), (0, 2, 2), lambda i, x, y: win.blit(f1.render(str(i[0].title), True, (180, 100, 0)), (x + 2, y + 2)))
dressed_item_specifications = interface(men_sn_ok[2],    (0, 0), (465, 130, 765, 280), (150, 25), lambda i, x, y: win.blit(f1.render(str(i[0]), True, (180, 100, 0)), (x + 2, y + 2)), lambda i, x, y: win.blit(f1.render(str(i[1]), True, (180, 100, 0)), (x + 130, y + 2)))
dressed_item_chances = interface('',                     (0, 0), (765, 130, 765, 280), (150, 25), lambda i, x, y: win.blit(f1.render(str(i[0]), True, (180, 100, 0)), (x + 2, y + 2)), lambda i, x, y: win.blit(f1.render(str(i[1]), True, (180, 100, 0)), (x + 130, y + 2)), s=False)
dressed_item_resistance = interface('',                  (0, 0), (1065, 130, 765, 280), (150, 25), lambda i, x, y: win.blit(f1.render(str(i[0]), True, (180, 100, 0)), (x + 2, y + 2)), lambda i, x, y: win.blit(f1.render(str(i[1]), True, (180, 100, 0)), (x + 130, y + 2)), s=False)
dressed_item_specifications_v2 = interface(men_sn_ok[3], (0, 0), (465, 330, 765, 280), (150, 25), lambda i, x, y: win.blit(f1.render(str(i[0]), True, (180, 100, 0)), (x + 2, y + 2)), lambda i, x, y: win.blit(f1.render(str(i[1]), True, (180, 100, 0)), (x + 130, y + 2)))
dressed_item_chances_v2 = interface('',                  (0, 0), (765, 330, 765, 280), (150, 25), lambda i, x, y: win.blit(f1.render(str(i[0]), True, (180, 100, 0)), (x + 2, y + 2)), lambda i, x, y: win.blit(f1.render(str(i[1]), True, (180, 100, 0)), (x + 130, y + 2)), s=False)
dressed_item_resistance_v2 = interface('',               (0, 0), (1065, 330, 765, 280), (150, 25), lambda i, x, y: win.blit(f1.render(str(i[0]), True, (180, 100, 0)), (x + 2, y + 2)), lambda i, x, y: win.blit(f1.render(str(i[1]), True, (180, 100, 0)), (x + 130, y + 2)), s=False)
gr = interface(men_sn_ok[1],(0, 0), (0, 484, 1360, 764), (136, 28), lambda i, x, y: win.blit(f1.render(str(i[0].title), True, (180, 100, 0)), (x + 2, y + 2)), lambda i, x, y: win.blit(f1.render(str(i[1]), True, (180, 100, 0)), (x + 126, y + 2)))
def showing_properties(pak):
    carrier, eq = pak # Для удобства создания меню в pak запакованно carrierr/носитель eq где он надет (голова, туловище и т.д)
    if isinstance(eq, str):
        if carrier.equipment[eq] != '':
            subject = carrier.equipment[eq] # Надетый предмет
            # В списки переберается (метод, словарь характеристик) после они преобразуются с помощью map в (название характиристики, её значение) и вызывается метод показа с этим списком
            [show.rendering_interface(list(map(lambda x: (x, characteristics[x]), characteristics.keys()))) for show, characteristics in ((dressed_item_specifications, subject.specifications), (dressed_item_chances, subject.chances), (dressed_item_resistance, subject.resistance))]
            #print(subject.specifications.values())
            #dressed_item_specifications.rendering_interface(subject.specifications.values)
            #dressed_item_chances.rendering_interface(subject.chances.values)
            #dressed_item_resistance.rendering_interface(subject.resistance.values)
        nam = tuple(carrier.equipment.keys())
        for i in range(len(nam)):
            v = f"{nam[i][:nam[i].rfind('_')]} / {carrier.equipment[nam[i]].title if carrier.equipment[nam[i]] != '' else ''}"
            win.blit(f1.render(str(v), True, (0, 255, 127)), (50, 80 + 50 * i))
    else:
        if len(carrier) < eq:
            try:
                subject = carrier[eq][0] # Предмет выбранный в таблице
            except:
                print(carrier, eq)
            # В списки переберается (метод, словарь характеристик) после они преобразуются с помощью map в (название характиристики, её значение) и вызывается метод показа с этим списком
            [show.rendering_interface(list(map(lambda x: (x, characteristics[x]), characteristics.keys()))) for show, characteristics in ((dressed_item_specifications_v2, subject.specifications), (dressed_item_chances_v2, subject.chances), (dressed_item_resistance_v2, subject.resistance))]
                    
        


