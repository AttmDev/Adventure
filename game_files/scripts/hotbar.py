from game_files.PPlay import gameimage as gi
from game_files.scripts import constants as c

class Inventory():
    def __init__(self):
        self.inventory_area = gi.GameImage(c.INV_BAR_HUD_IMAGE)
        self.inventory_area.x = c.HUD_SPACER #self.inventory_area.width * 0.2
        self.inventory_area.y = self.inventory_area.x

    def draw(self):
        self.inventory_area.draw()

class Item(gi.GameImage):
    def __init__(self, image_file, tipo = None):
        gi.GameImage.__init__(self, image_file)
        self.tipo = tipo