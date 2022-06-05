import script.guide
from script.start_game import pg, win, f0
import sys

clock = pg.time.Clock()
pla = pg.image.load(script.guide.path + "\\aset\\men\\nanel_textv1.png").convert_alpha()
#f1 = pg.freetype.Font(script.guide.path + "\\Fonts\\Gabriola One.ttf", 28)
got_t = []
class Text:
    def __init__(self) -> None:
        self.ob_text = []
        self.stroka = 0
        self.blok = 0
        self.per = 0
        self.xod = False
        self.kadr_texta = 0
    def otobra(self):
        try:
            len(self.ob_text[self.blok][self.stroka])
        except IndexError:
            raise IndexError(self.stroka, self.blok, len(self.ob_text), len(self.ob_text[0]))
        if self.ob_text[self.blok] == self.ob_text[-1] and self.stroka + 1 == len(self.ob_text[self.blok]) and self.per == len(self.ob_text[self.blok][self.stroka]):#self.ob_text[self.blok][self.stroka][self.per] == self.ob_text[-1][-1][-1]:
            # self.ob_text[self.blok] and self.ob_text[-1] and self.stroka == len(self.blok) and self.per == len(self.ob_text[self.blok][self.stroka])
            v = 1
            for d in range(self.stroka + 1):
                win.blit(f0.render(self.ob_text[self.blok][d], True, (255, 171, 24)), (5, 524 + 30 * v))
                v += 1
            self.xod = False#, self.per
            return            
        if self.per == len(self.ob_text[self.blok][self.stroka]):
            if self.stroka < len(self.ob_text[self.blok]) - 1:
                self.stroka += 1
            self.per = 0
            #return
        else:
            win.blit(f0.render(self.ob_text[self.blok][self.stroka][:self.per + 1], True, (255, 171, 24)), (5, 524 + 30 * (self.stroka + 1)))
        v = 1
        for d in range(self.stroka):
            win.blit(f0.render(self.ob_text[self.blok][d], True, (255, 171, 24)), (5, 524 + 30 * v))
            v += 1
        if self.xod == False:
            self.xod = False#, self.per
            return 
        if len(self.ob_text[self.blok]) <= self.stroka:
            self.blok += 1
            if self.blok >= len(self.ob_text):
                print('Конец текста')
                self.blok -= 1
            else:
                self.stroka = 0
            self.xod = False#, self.per
            return
        else:
            self.xod = True#, self.per
            return
    def otr(self, bak, fps):
        self.kadr_texta  += 1
        text.otobra()
        if self.kadr_texta % 5 == 0 and self.xod == True:
            self.per += 1
            self.kadr_texta  = 0 
    def text_update(self, text):
        self.ob_text = []
        x = []
        pere = []
        for i in text.split():
            pere.append(i)
            if len((' ').join(pere)) > 135:       
                x.append((' ').join(pere[:-1]))
                if '/' in x[-1]:
                    cl = x.pop()
                    x.append(cl[:cl.find('/')])
                    pere = [*[n for n in (cl[cl.find('/') + 1:]).split()]]
                elif len(x) == 7 or '№' in (' ').join(x[-1]):
                    self.ob_text.append(x)
                    x = []
                    pere = [i, ]
                else:
                    pere = [i, ]
        x.append((' ').join(pere))
        self.ob_text.append(x)
        self.stroka = 0
        self.blok = 0
        self.per = 0
        self.xod = True
        self.kadr_texta = 0       
text = Text()
if __name__ == '__main__':
    text = Text()
    kadr_texta = 0
    print(text.ob_text)
    per = 0
    kadr = 0
    vivod = False
    stop_text = False
    xod = True
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type==pg.KEYDOWN:
                if event.key == 13:
                    if vivod == True:
                        if xod == False:
                            text.blok += 1
                            if text.blok >= len(text.ob_text):
                                pass
                            text.stroka = 0
                            xod = True
                        elif xod == True:
                            text.stroka = len(text.ob_text[text.blok]) -1 
                            xod == False
                    else:
                        vivod = True
                if event.key == pg.K_z:
                    print(xod)      
        win.fill((255, 255, 255)) 
        if vivod == True:
            win.blit(pla, (0, 0))
            kadr_texta += 1
            xod, per = text.otobra(per, xod)
            if kadr_texta % 5 == 0  and xod == True:
                per += 1
                kadr_texta = 0 
        kadr += 1
        if kadr == 1000:
            kadr = 0
        pg.display.flip() ##    = pg.display.update()
        clock.tick(1000)
        pg.time.wait(1)
