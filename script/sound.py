from script.start_game import pg
import script.guide
pg.mixer.init()
mus = pg.mixer.Sound(script.guide.path + '\\sounds\\morning.ogg')
world = pg.mixer.Sound(script.guide.path + '\\sounds\\world.ogg')
leaves = pg.mixer.Sound(script.guide.path + '\\sounds\\leaves.ogg')
class Sound():
    def __init__(self) -> None:
        self.main_composition = pg.mixer.Channel(1) 
        self.footsteps = pg.mixer.Channel(2) 
        self.effects = [pg.mixer.Channel(i) for i in range(3, 5)]  
        self.slow = {
            'инвентарь':mus,
            'мир':world
        }
    def change_main_composition(self, bak):
        if bak in self.slow:
            self.main_composition.play(self.slow[bak])
            self.main_composition.set_volume(0.5)
            #self.main_composition.set_volume(1, 0.1)
sound = Sound()
