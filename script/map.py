from script.start_game import pg, win, path
from script.base_classes import player, object, camera
import script.guide
class object:
    ##  Это какой-нибудь объект, отличный игрока (к примеру враг или дерево)
    def __init__(self, x, y, width, height, RGP=(255, 0, 0), spr=[], py=[]):
        self.rect = pg.Rect(x, y, width, height)
        self.RGP = RGP
        self.sprait = spr
        self.py_sprai = py
    def draw(self):
        ##  Чтобы отрисовка соответствовала позиции объекта его нужно отрисовывать
        ##  на self.rect[0]-camera.rect[0], self.rect[1]-camera.rect[1]
        if self.sprait == []:
            pg.draw.rect(win, self.RGP, (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1], self.rect[2], self.rect[3]), 2)
        else:
            for i in self.sprait:
                i = pg.image.load(script.guide.path + i).convert_alpha()
                win.blit(i, (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1]))
    def dop(self, v):
        self.sprait = [*self.sprait, v[0]]
        self.py_sprai = [*self.py_sprai, v[1]]
class big_chunk:
    def __init__(self, r, ostl) -> None:
        self.rect = pg.Rect(r[0], r[1], r[2], r[3])
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
        self.compound = (middle_chunk(m_c[0][0], m_c[0][1]), middle_chunk(m_c[1][0], m_c[1][1]), middle_chunk(m_c[2][0], m_c[2][1]), middle_chunk(m_c[3][0], m_c[3][1]))
class middle_chunk:
    def __init__(self, r, ostl) -> None:
        self.rect = pg.Rect(r[0], r[1], r[2], r[3])
        self.compound = (small_chunk(ostl[0][0], ostl[0][1]), small_chunk(ostl[1][0], ostl[1][1]), small_chunk(ostl[2][0], ostl[2][1]), small_chunk(ostl[3][0], ostl[3][1]))
class small_chunk:
    def __init__(self, r, ostl) -> None:
        self.rect = pg.Rect(r[0], r[1], r[2], r[3])
        self.compound = tuple([object(i[0], i[1], i[2], i[3], spr=i[4]) for i in ostl])
prop_objects = []
faj = []
class Map_class:
    def __init__(self) -> None:
        self.__map = []
        self.prop_objects = []
    def converting_txt_v_map():
        with open("proverka.txt", 'r', encoding='utf-8') as file:
            bag = (file.readline()).strip().split(' ')
            sprites = bag[0].split('_')
            amount = int(bag[1])
            for _ in range(amount):
                x = (file.readline()).strip().split('_')
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
def recursion_otr(spis, ind):
    if len(spis) < 1:
        return
    if isinstance(spis[0], object):
        [(obj.draw(), faj.append(obj)) for obj in spis if obj.rect.colliderect(camera.rect)]
        return
    elif spis[ind].rect.colliderect(camera.rect):
        recursion_otr(spis[ind].compound, 0)
    ind += 1
    if ind == len(spis):
        return
    return recursion_otr(spis, ind)
Map_class.converting_txt_v_map()