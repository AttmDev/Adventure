from game_files.PPlay.sprite import Sprite
from game_files.scripts import constants, smoke
from math import cos, sin, radians

class Bullet(Sprite):
    def __init__(self, sprite, frames, player, sfx, speed, angulo = 0):
        super().__init__(sprite, frames)
        self.set_total_duration(500)
        self.sfx_manager = sfx
        self.player = player
        self.direction_player = player.get_curr_frame()
        self.calc_direction(angulo)
        self.set_initial_position()
        self.speed = speed
        self.collided = False

    def calc_direction(self, angle):
        if self.direction_player == 0:
            self.vec_dir = [-1, 0]
        elif self.direction_player == 2:
            self.vec_dir = [1, 0]
        elif self.direction_player == 1:
            self.vec_dir = [0, -1]
        elif self.direction_player == 3:
            self.vec_dir = [0, 1]
        vec_dir0 = self.vec_dir[0] * cos(angle) - self.vec_dir[1] * sin(angle)
        self.vec_dir[1] = self.vec_dir[0] * sin(angle) + self.vec_dir[1] * cos(angle)
        self.vec_dir[0] = vec_dir0


    def set_initial_position(self):
        if self.direction_player == 0:
            self.x = self.player.x+2
            self.y = self.player.y+2
        elif self.direction_player == 2:
            self.x = self.player.x+self.player.width-self.width
            self.y = self.player.y + self.player.height - self.width
        elif self.direction_player == 1:
            self.x = self.player.x+self.player.width - self.width - 10
            self.y = self.player.y
        elif self.direction_player == 3:
            self.x = self.player.x+self.width
            self.y = self.player.y + self.player.height - self.width
        self.sfx_manager.add_to_list(smoke.smoke(player=self.player))


    def draw_and_update(self, delta_time):
        self.draw()
        self.move(delta_time)
        self.update()

    def is_colliding(self):
        self.collided = True

    def is_dead(self):
        if self.collided or self.x > constants.width or self.x < 0 or self.y > constants.height or self.y < 0:
            return True
        return False

    def move(self, delta_time):
        self.x += self.vec_dir[0]* delta_time*self.speed
        self.y+= self.vec_dir[1]*delta_time*self.speed