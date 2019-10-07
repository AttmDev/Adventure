from game_files.PPlay.sprite import Sprite
from game_files.scripts import life_manager, constants
from threading import Timer
import random

class Enemy_object(Sprite):

    def __init__(self, sprite):
        super().__init__(sprite)
        self.x = random.randint(0, constants.width - self.width)
        self.y = random.randint(0, constants.height - self.height)
        self.speed = 100
        self.hit_points = 3
        self.hp = life_manager.Health(self, [self.x, self.y])
        self.damage = 2
        self.is_invulnerable = False
        self.cd = .1


    def draw_and_update(self):
        if self.is_alive():
            self.hp.re_position([self.x, self.y])
            self.draw()
            try:
                self.update()
            except:
                #print(f"Erro ao update Enemy {self}")
                pass


    def is_alive(self):
        return self.hp.healthPoints > 0

    def lose_hp(self, damage):
        self.hp.lose_hp(damage, self.is_invulnerable)
        if not self.is_invulnerable:
            self.set_invul_state(True)
            t = Timer(self.cd, self.set_invul_state, args=[False])
            t.start()

    def set_invul_state(self, bool):
        self.is_invulnerable = bool