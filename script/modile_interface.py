from script.start_game import win, pg, sys

f1 = pg.font.Font(sys.path[0] + "\\Fonts\\Gabriola One.ttf", 26)
men_sn_ok = [pg.image.load(sys.path[0] + "\\aset\\men\\oc_okn.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\dop_okn.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\dop_okn_n.png").convert_alpha(), pg.image.load(sys.path[0] + "\\aset\\men\\dop_okn_v.png").convert_alpha()]
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
                win.blit(f1.render(str(i[d[0]]), True, (180, 100, 0)), (x + d[1], y + d[2]))
            x += self.bias[0]
            if x == self.dimensions[2]:
                if y == self.dimensions[3]:
                    return
                x = self.dimensions[0]
                y += self.bias[1]
    def rendering_frame(self, ramka, kn):
        
        win.blit(ramka, ((self.dimensions[0] + kn * self.bias[0]) % self.dimensions[2], (self.dimensions[1] + kn * self.bias[1]) % self.dimensions[3]))
        pass
obw_od = interface(men_sn_ok[0], (0, 0), (50, 80, 50, 480), (0, 50), (0, 2, 2))
dressed_item_specifications = interface(men_sn_ok[2], (0, 0), (465, 130, 765, 280), (150, 25), (0, 2, 2), (1, 130, 2))
dressed_item_chances = interface(men_sn_ok[2], (0, 0), (765, 130, 765, 280), (150, 25), (0, 2, 2), (1, 130, 2), s=False)
dressed_item_resistance = interface(men_sn_ok[2], (0, 0), (1065, 130, 765, 280), (150, 25), (0, 2, 2), (1, 130, 2), s=False)
gr = interface(men_sn_ok[1], (0, 0), (0, 484, 1360, 764), (136, 28), (0, 2, 2), (1, 126, 2))