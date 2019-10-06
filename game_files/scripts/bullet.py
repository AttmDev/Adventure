from game_files.PPlay.sprite import Sprite
from game_files.scripts import constants

class Bullet(Sprite):
    def __init__(self, sprite, frames, player):
        super().__init__(sprite, frames)
        self.set_total_duration(500)
        self.player = player
        self.direction = player.get_curr_frame()
        self.set_initial_position()
        self.speed = 200
        self.collided = False

    def set_initial_position(self):
        if self.direction == 0:
            self.x = self.player.x+2
            self.y = self.player.y+2
        elif self.direction == 2:
            self.x = self.player.x+self.player.width-self.width
            self.y = self.player.y + self.player.height - self.width
        elif self.direction == 1:
            self.x = self.player.x+self.player.width - self.width - 10
            self.y = self.player.y
        elif self.direction == 3:
            self.x = self.player.x+self.width
            self.y = self.player.y + self.player.height - self.width


    def draw_and_update(self, delta_time):
        self.draw()
        self.move(delta_time)
        self.update()

    def is_colliding(self):
        self.collided = True

    def is_dead(self):
        if self.collided:
            return True
        elif self.x > constants.width:
            return True
        elif self.x < 0:
            return True
        elif self.y > constants.height:
            return True
        elif self.y < 0:
            return True
        else:
            return False

    def move(self, delta_time):
        if self.direction == 0:
            self.x -= self.speed * delta_time
        elif self.direction == 2:
            self.x += self.speed * delta_time
        elif self.direction == 1:
            self.y -= self.speed * delta_time
        elif self.direction == 3:
            self.y += self.speed * delta_time
