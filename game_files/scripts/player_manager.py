import pygame

from game_files.PPlay import sprite as sp
from game_files.scripts import constants as c, game_events
from game_files.scripts.life_manager import Health


class Player(sp.Sprite):
    def __init__(self):
        sp.Sprite.__init__(self, c.PLAYER_SPRITE)
        self.player_hp = 20
        self.hp = Health(self.player_hp)
        self.speed = 250
        self.x = c.width/2
        self.y = c.height/2
        self.cd = 750  #tempo de cooldown usado para invulnerabilidade quando recebe dano
        self.is_invulnerable = False
        self.invul_start()

    def draw_and_update(self):
        self.draw()
        self.hp.drawHealth()

    def loseHp(self, damage: int = 1):
        if not self.is_invulnerable:
            self.hp.healthPoints -= damage
            pygame.event.post(pygame.event.Event(game_events.START_PLAYER_INVUL))

    def invul_start(self):
        #TODO mudar o sprite para um de invulnerabilidade
        vida_atual = self.hp.healthPoints
        self.is_invulnerable = True
        pygame.time.set_timer(game_events.END_PLAYER_INVUL, self.cd)

    def invul_end(self):
        #TODO mudar o sprite de volta
        self.is_invulnerable = False



