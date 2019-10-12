from game_files.PPlay import sprite
from game_files.scripts import constants


class smoke(sprite.Sprite):

    def __init__(self, player):
        super().__init__(constants.SMOKE_IMAGE, 7)
        self.set_total_duration(360)
        self.player = player
        self.direction = player.get_curr_frame()
        self.set_initial_position()
        self.to_destroy = False

    def draw_and_update(self):
        self.draw()
        self.update()
        if self.get_curr_frame() == self.get_final_frame()-1:
            self.to_destroy = True


    def set_initial_position(self):
        if self.direction == 0:
            self.x = self.player.x-4
            self.y = self.player.y-2
        elif self.direction == 2:
            self.x = self.player.x+self.player.width-self.width +2
            self.y = self.player.y + self.player.height - self.height+4
        elif self.direction == 1:
            self.x = self.player.x+self.player.width - self.width - 6
            self.y = self.player.y - (self.height/2)-1
        elif self.direction == 3:
            self.x = self.player.x+5
            self.y = self.player.y + self.player.height-7
