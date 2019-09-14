from game_files.PPlay import gameimage as gi
from game_files.scripts import constants as c

class Inventory():
    def __init__(self):
        self.spaces = [gi.GameImage(c.INV_BAR_HUD_IMAGE) for i in range(5)]
        self.spaces[0].x = c.width/15
        self.spaces[0].y = c.height/40
    def draw(self):
        self.spaces[0].draw()

class Item(gi.GameImage):
    def __init__(self, image_file, tipo = None):
        gi.GameImage.__init__(self, image_file)
        self.tipo = tipo