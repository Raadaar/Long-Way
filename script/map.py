from script.start_game import pg, win, path
from script.base_classes import player, object, camera
import script.guide
chest = pg.image.load(script.guide.path + "\\aset\\chest.png").convert_alpha()
nps = pg.image.load(script.guide.path + "\\aset\\nps.png").convert_alpha()
class object:
    ##  Это какой-нибудь объект, отличный игрока (к примеру враг или дерево)
    def __init__(self, x, y, width, height, RGP=(255, 0, 0), spr=[], py=[]):
        self.rect = pg.Rect(x, y, width, height)
        self.RGP = RGP
        self.sprait = spr
        self.py_sprai = py
        self.barrier = False
        self.chest = [[],]
        self.nps = []
    def draw(self):
        ##  Чтобы отрисовка соответствовала позиции объекта его нужно отрисовывать
        ##  на self.rect[0]-camera.rect[0], self.rect[1]-camera.rect[1]
        if self.sprait != "":
                card.layer_one.append([card.sprites[self.sprait], (self.rect[0], self.rect[1])]) 
    def interaction_check(self, map):
        if self.barrier != 'False':
            map.layer_barriers.extend(pg.Rect(self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1], 50, 50))
        if self.chest[0][0] != ['']:
            map.interaction_layer.append((pg.Rect(self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1], 50, 50), chest, self.chest, 'Сундук', self))
        if self.nps != '[]':
            map.interaction_layer.append((pg.Rect(self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1], 50, 50), nps, self.nps, 'NPS'))
    def dop(self, v):
        self.sprait = [*self.sprait, v[0]]
        self.py_sprai = [*self.py_sprai, v[1]]
puzzles = [[],[]]
class big_chunk:
    def __init__(self, r, ostl) -> None:
        self.rect = pg.Rect(r[0], r[1], r[2], r[3])
        self.adjusting_coordinates = [r[0], r[1]]
        m_c = []
        v = [0, 0]
        for i in ostl:
            if i[3] / 2500 == 1:
                v[0] = len(m_c)
                v[1] = 0
                m_c.append([i, []])
            elif i[3] / 1250 == 1:
                m_c[v[0]][1].append([i, []])
                v[1] += 1
            else:
                m_c[v[0]][1][v[1] - 1][1].append(i)
        self.compound = (middle_chunk(m_c[0][0], m_c[0][1], self.adjusting_coordinates, self), middle_chunk(m_c[1][0], m_c[1][1], self.adjusting_coordinates, self), middle_chunk(m_c[2][0], m_c[2][1], self.adjusting_coordinates, self), middle_chunk(m_c[3][0], m_c[3][1], self.adjusting_coordinates, self))
class middle_chunk:
    def __init__(self, r, ostl, adjusting_coordinates, warp) -> None:
        self.rect = pg.Rect(r[0] - adjusting_coordinates[0], r[1] - adjusting_coordinates[1], r[2], r[3])
        self.compound = (small_chunk(ostl[0][0], ostl[0][1], adjusting_coordinates, warp), small_chunk(ostl[1][0], ostl[1][1], adjusting_coordinates, warp), small_chunk(ostl[2][0], ostl[2][1], adjusting_coordinates, warp), small_chunk(ostl[3][0], ostl[3][1], adjusting_coordinates, warp))
class small_chunk:
    def __init__(self, r, ostl, adjusting_coordinates, warp) -> None:
        self.rect = pg.Rect(r[0] - adjusting_coordinates[0], r[1] - adjusting_coordinates[1], r[2], r[3])
        self.layer_one = [] # Первый слой пол
        self.layer_two = [] # Второй слой
        self.compound = [] # Третий слой
        x = []
        for i in ostl:
            pred = object(i[0], i[1], i[2], i[3])
            spr = i[4][0].split('!')
            for sp in range(len(spr)):
                pust = card.sprites_py.index(spr[sp])

                #warp._surface[sp].blit(card.sprites[pust], (i[0] - adjusting_coordinates[0], i[1] - adjusting_coordinates[1]))
                if sp > 0:
                    v = card.sprites[pust].get_size()
                    puzzles[sp].append([card.sprites[pust], pg.Rect(i[0], i[1], v[0], v[1])])
                else:
                    pred.sprait = pust
            pred.barrier = i[4][1]
            pred.chest[0] = [d.split('$') for d in i[4][2].split('!')]
            pred.chest.append(True)
            pred.nps = i[4][3]
            x.append(pred)
        self.compound = tuple(x)
prop_objects = []
faj = []
class Map_class:
    def __init__(self) -> None:
        self.__map = []
        self.prop_objects = []
        self.layer_one = [] # Первый слой пол
        self.interaction_layer = [] # Слой взаимодействия
        self.layer_two = [] # Второй слой
        self.layer_three = [] # Третий слой
        self.layer_barriers = []
        self.sprites = []
        self.sprites_py = []
    def converting_txt_v_map(self):
        with open("proverka.txt", 'r', encoding='utf-8') as file:
            bag = (file.readline()).strip().split(', ')
            self.sprites = [pg.image.load(script.guide.path + i).convert_alpha() for i in bag[:-1]]
            self.sprites_py = bag[:-1]
            amount = int(bag[-1])
            for _ in range(amount):
                x = (file.readline()).strip().split('~')
                vrem_bak = []
                for i in x:
                    #print(i.split(', '))
                    prob = i.split(', ')
                    if len(prob) > 4:
                        prob = [int(prob[0]), int(prob[1]), int(prob[2]), int(prob[3]), prob[4:]]
                    else:
                        prob = [int(d) for d in prob]
                    vrem_bak.append(prob)
                prop_objects.append(big_chunk(vrem_bak[0], vrem_bak[1:]))
        for i in sorted(puzzles[1], key=lambda x: [x[1][0], x[1][1]]):
            for big in prop_objects:
                if i[1].colliderect(big.rect):
                    for middle in big.compound:
                        if i[1].colliderect(middle.rect):
                            for small in middle.compound:
                                if i[1].colliderect(small.rect):
                                    small.layer_two.append([i[0], (i[1][0], i[1][1])])
    def drawing_layers(self):
        #for layers in [self.layer_one, self.layer_two]:
        #    win.blits([[i[0], (i[1][0] - camera.rect[0], i[1][1] - camera.rect[1])] for i in layers])
        #    #for i in layers:
        #    #    win.blit(i[0], (i[1][0] - camera.rect[0], i[1][1] - camera.rect[1]))
        win.blits([[i[0], (i[1][0] - camera.rect[0], i[1][1] - camera.rect[1])] for i in self.layer_one])
        [win.blit(i[1], i[0]) for i in self.interaction_layer]
        player.draw()
        win.blits([[i[0], (i[1][0] - camera.rect[0], i[1][1] - camera.rect[1])] for i in self.layer_two])
        self.layer_one = [] # Первый слой пол
        self.interaction_layer = [] # Слой взаимодействия
        self.layer_two = [] # Второй слой
        self.layer_three = [] # Третий слой
        self.layer_barriers = []
            #win.blits([[i[0] (i[1][0] - camera.rect[0], i[1][1] - camera.rect[1])] for i in layers])
        #[i for i in prop_objects if i.rect.colliderect(camera.rect)]
        
#def recursion_otr(spis, ind):
#    #if len(spis) < 1:
#    #    return
#    if isinstance(spis[ind], small_chunk):
#        #pg.draw.rect(win, (0, 100, 0), ((spis[ind].rect[0] - camera.rect[0], spis[ind].rect[1] - camera.rect[1], spis[ind].rect[2], spis[ind].rect[3]))) # spis[ind].rect
#        [[obj.draw(), obj.interaction_check(card)] for obj in [obj for obj in spis[ind].compound if obj.rect.colliderect(camera.rect)]]
#        #    obj.draw()
#        #    obj.interaction_check(card)
#        [card.layer_two.append(obj) for obj in [obj for obj in spis[ind].layer_two if pg.Rect(obj[1][0], obj[1][1], obj[0].get_width(), obj[0].get_height()).colliderect(camera.rect)] if obj not in card.layer_two]
#        #    if obj not in card.layer_two:
#        #        card.layer_two.append(obj)
#        #return
#    elif spis[ind].rect.colliderect(camera.rect):
#        recursion_otr(spis[ind].compound, 0)
#    ind += 1
#    if ind > 3:
#        return
#    return recursion_otr(spis, ind)
def recursion_otr():#spis, ind):
#    [d for d in [i for i in prop_objects if i.rect.colliderect(camera.rect)] if d.rect.colliderect(camera.rect)]
    for i in prop_objects:
        if i.rect.colliderect(camera.rect):
            for d in i.compound:
                if d.rect.colliderect(camera.rect):
                    for v in d.compound:
                        if v.rect.colliderect(camera.rect):
                            [[obj.draw(), obj.interaction_check(card)] for obj in v.compound if obj.rect.colliderect(camera.rect)]
                            [card.layer_two.append(obj) for obj in v.layer_two if pg.Rect(obj[1][0], obj[1][1], obj[0].get_width(), obj[0].get_height()).colliderect(camera.rect)]# and obj not in card.layer_two]
                            #for obj in v.layer_two:
                            #    if pg.Rect(obj[1][0], obj[1][1], obj[0].get_width(), obj[0].get_height()).colliderect(camera.rect):
                            #        card.layer_two.append(obj)

card = Map_class()
card.converting_txt_v_map()