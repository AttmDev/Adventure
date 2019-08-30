from PPlay import sprite as sp
from PPlay import gameimage as gi
import constants as c

class Player(sp.Sprite):
    def __init__(self):
        sp.Sprite.__init__(self, c.soldierImage)
        self.x = c.width/2
        self.y = c.height/2
        self.hp = Health()

    def drawPlayerStuff(self):
        self.draw()
        self.hp.drawHealth()

    def loseHp(self):
        self.hp.healthPoints -= 1


class Health():
    def __init__(self):
        self.healthPoints = 11
        self.lifeBar = gi.GameImage(c.lifeBarImage)
        self.lifeBar.x = (c.width - self.lifeBar.width) / 2
        self.lifeBar.y = c.height - self.lifeBar.height - c.height / 72
        self.lifeUnits = [gi.GameImage(c.lifeUnitImage) for i in range(11)]
        self.lifeUnits[0].x = self.lifeBar.x
        self.lifeUnits[0].y = self.lifeBar.y
        for i in range(1, 11):
            self.lifeUnits[i].y = self.lifeBar.y
            self.lifeUnits[i].x = self.lifeUnits[i - 1].x + self.lifeUnits[i].width
    def drawHealth(self):
        self.lifeBar.draw()
        for i in range(self.healthPoints):
            self.lifeUnits[i].draw()
