from game_files.PPlay import gameimage as gi
from game_files.PPlay import sprite as sp
from game_files.scripts import constants as c


class Health:
    def __init__(self, player_hp):
        self.healthPoints = player_hp
        self.lifeBar = gi.GameImage(c.LIFE_BAR_HUD_IMAGE)

        self.lifeUnits = list()

        self.lifeBar.x = (c.width - self.lifeBar.width) / 2
        self.lifeBar.y = c.height - self.lifeBar.height - c.height / 72

        for i in range(0, player_hp):
            new_node = sp.Sprite(c.LIFE_UNIT_IMAGE, 1)
            new_node.width = ((self.lifeBar.width + self.spacing())/player_hp) - self.spacing()
            new_node.x = self.lifeBar.x + (new_node.width + self.spacing())* i
            new_node.y = self.lifeBar.y

            self.lifeUnits.append(new_node)

    def drawHealth(self):
        self.lifeBar.draw()
        for hp in range(self.healthPoints):
            self.lifeUnits[hp].draw()

    def spacing(self):
        """
        Calculo do tamanho do espaço que separa os quadrados de vida
        :return: int
        """
        return 5