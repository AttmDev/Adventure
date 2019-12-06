from threading import Timer

from game_files.PPlay import sprite
from game_files.scripts import constants


class Begin(sprite.Sprite):

    def __init__(self):

        super().__init__(constants.START_SCREEN, 4)
        self.cmd = sprite.Sprite(constants.CONTROLS_SPRITE, 1)
        self.cmd.set_position(constants.width-constants.width/4, constants.height-constants.height/5)
        self.set_total_duration(1500)
        self.loop = False
        self.to_destroy = False
        t = Timer(5, self.set_dead)
        t.start()

    def draw_and_update(self):
        self.draw()
        self.cmd.draw()
        self.update()
        if self.get_curr_frame() == self.get_final_frame()-1:
            self.hide()

    def set_dead(self):
        self.to_destroy = True