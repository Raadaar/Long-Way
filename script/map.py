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
        self.barrier = False
        self.chest = []
        self.nps = []
        # Очень страннный баг, если _surface давать gg, то при обращение к _surface оно меняет _surface всех классов object
        self._surface = ['', '', '']
        self._surface_py = ['', '', '']
        self.execution = 0
        self.dop_sprait = []
    def draw(self):
        ##  Чтобы отрисовка соответствовала позиции объекта его нужно отрисовывать
        ##  на self.rect[0]-camera.rect[0], self.rect[1]-camera.rect[1]
        if str(set(self._surface)) != "{''}":
            if isinstance(self._surface[0], int):
                win.blit(card.sprites[self._surface[0]], (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1])) 
            if isinstance(self._surface[1], int):
                win.blit(card.sprites[self._surface[1]], (self.rect[0] - camera.rect[0], self.rect[1] - camera.rect[1]))
    def dop(self, v):
        self.sprait = [*self.sprait, v[0]]
        self.py_sprai = [*self.py_sprai, v[1]]
puzzles = [[],[]]
class big_chunk:
    def __init__(self, r, ostl) -> None:
        self.rect = pg.Rect(r[0], r[1], r[2], r[3])
        self._surface = [pg.Surface((r[2], r[3]), flags=pg.SRCALPHA), pg.Surface((r[2], r[3]), flags=pg.SRCALPHA), pg.Surface((r[2], r[3]), flags=pg.SRCALPHA)]
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
        x = []
        for i in ostl:
            pred = object(i[0] - adjusting_coordinates[0], i[1] - adjusting_coordinates[1], i[2], i[3])
            spr = i[4][0].split('!')
            for sp in range(len(spr)):
                pust = card.sprites_py.index(spr[sp])
                pred._surface[sp] = pust
                #warp._surface[sp].blit(card.sprites[pust], (i[0] - adjusting_coordinates[0], i[1] - adjusting_coordinates[1]))
                puzzles[sp].append([pg.Rect(i[0], i[1], i[2], i[3]), pust])
            pred.barrier = i[4][1]
            pred.chest = i[4][2]
            pred.nps = i[4][3]
            x.append(pred)
        self.compound = tuple(x)
prop_objects = []
faj = []
class Map_class:
    def __init__(self) -> None:
        self.__map = []
        self.prop_objects = []
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
        for xislo in range(2):
            for i in sorted(puzzles[xislo], key=lambda x: [x[0][0], x[0][1]]):
                for d in prop_objects:
                    if i[0].colliderect(d.rect):
                        d._surface[xislo].blit(card.sprites[i[1]], (i[0][0] - d.adjusting_coordinates[0], i[0][1] - d.adjusting_coordinates[1]))
        #[i for i in prop_objects if i.rect.colliderect(camera.rect)]
        
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
card = Map_class()
card.converting_txt_v_map()