from game_files.PPlay.sprite import Sprite
from game_files.scripts import constants

class Bullet(Sprite):
    def __init__(self, sprite, frames):
        super().__init__(sprite, frames)
        self.set_total_duration(500)
        self.x = 300
        self.y = 400

    def draw_and_update(self):
        self.draw()
        self.update()
