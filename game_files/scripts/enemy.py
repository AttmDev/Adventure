from game_files.PPlay.sprite import Sprite
from game_files.scripts import life_manager, constants
from threading import Timer
import random

class Enemy_object(Sprite):

    def __init__(self, sprite, n=1):
        super().__init__(sprite, n)
        self.x = random.randint(0, int(constants.width - self.width))
        self.y = random.randint(0, int(constants.height - self.height))
        self.speed = 50
        self.hit_points = 5
        self.hp = life_manager.Health(self, [self.x, self.y])
        self.damage = 2
        self.is_invulnerable = False
        self.cd = .25
        self.knockback_status = False
        self.knockback_time = .24
        self.knockback_force = 300
        self.knockback_direction = 0


    def draw_and_update(self, delta):
        if self.is_alive():
            self.hp.re_position([self.x, self.y])
            if self.knockback_status:
                self.__do_knock_mov(delta)
            self.draw()
            try:
                self.play()
                self.update()
            except:
                print(f"unable to update {self} at x:{self.x} y:{self.y}")


    def wiggle(self):
        normal_height = self.height
        normal_width = self.width

        self.height *= .9
        t = Timer(self.knockback_time, self.set_height, args=[normal_height])
        t.start()
        self.width *= .9
        t = Timer(self.knockback_time, self.set_width, args=[normal_width])
        t.start()


    def is_alive(self):
        return self.hp.healthPoints > 0

    def lose_hp(self, damage):
        self.hp.lose_hp(damage, self.is_invulnerable)
        if not self.is_invulnerable:
            # self.wiggle() #TODO FAZER ISSO FUNFAR
            self.set_invul_state(True)
            t = Timer(self.cd, self.set_invul_state, args=[False])
            t.start()

    def set_invul_state(self, bool):
        self.is_invulnerable = bool

    def set_height(self, x):
        self.height = x

    def set_width(self, x):
        self.width = x

    def set_knockback_status(self, boolX):
        self.knockback_status = boolX

    def knocked_back(self, bullet): #TODO ESSE MOV PODE FICAR MAIS NATURAL SE FOR DE PIXEL EM PIXEL
        self.knockback_status = True
        self.knockback_direction = bullet
        t = Timer(self.knockback_time, self.set_knockback_status, args=[False])
        t.start()

    def __do_knock_mov(self, x):
        if self.knockback_direction == 0:
            self.x -= self.knockback_force *x
        elif self.knockback_direction == 1:
            self.y -= self.knockback_force *x
        elif self.knockback_direction == 2:
            self.x += self.knockback_force *x
        elif self.knockback_direction == 3:
            self.y += self.knockback_force *x
