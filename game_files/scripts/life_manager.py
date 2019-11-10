from game_files.PPlay import sprite as sp
from game_files.scripts import constants as c


class Health:
    def __init__(self, object_with_health, pos = None):
        self.healthPoints = object_with_health.hit_points
        self.lifeBar = sp.Sprite(c.LIFE_BAR_HUD_IMAGE)
        self.actor = object_with_health
        self.lifeUnits = list()
        self.is_player = True

        if pos == None:
            self.lifeBar.x = c.HUD_SPACER * 6.2
            self.lifeBar.y = c.HUD_SPACER
            self.lifeBar.width *= 0.5
        else:
            self.is_player = False
            self.lifeBar.width = object_with_health.width * 0.5
            self.lifeBar.height = c.HUD_SPACER * 0.5
            self.re_position(pos)

        for i in range(0, self.healthPoints):
            new_node = sp.Sprite(c.LIFE_UNIT_IMAGE, 1)
            new_node.height = self.lifeBar.height - self.spacing() * 2
            new_node.width = ((self.lifeBar.width + self.spacing())/object_with_health.hit_points) - self.spacing()


            self.lifeUnits.append(new_node)

    def draw_and_update(self):
        if not self.is_player:
            self.re_position([self.actor.x, self.actor.y])
        self.lifeBar.draw()

        i = 0
        for hp in self.lifeUnits:
            hp.x = self.lifeBar.x + (hp.width + self.spacing()) * i
            hp.y = self.lifeBar.y + self.spacing()
            hp.draw()
            i+=1
            if i >= self.healthPoints:
                break

    def spacing(self):
        """
        Calculo do tamanho do espaço que separa os quadrados de vida
        :return: int
        """
        return 2

    def re_position(self, pos):
        self.lifeBar.x = pos[0] + self.actor.width * 0.25
        self.lifeBar.y = pos[1] - self.lifeBar.height * 1.5

    def get_hp(self, hp):
        self.healthPoints+=hp

    def lose_hp(self, damage, invul):
        if not invul:
            self.healthPoints-=damage