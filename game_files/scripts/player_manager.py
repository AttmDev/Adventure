from game_files.PPlay import sprite as sp
from game_files.scripts import constants as c
from game_files.scripts.events import event_name
from game_files.scripts.life_manager import Health


class Player(sp.Sprite):
    def __init__(self, user_event_manager):
        super().__init__(c.PLAYER_SPRITE)
        self.hit_points = 20
        self.hp = Health(self)
        self.speed = 250
        self.x = c.width/2
        self.y = c.height/2
        self.cd = .95  #tempo de cooldown usado em seg para invulnerabilidade quando recebe dano
        self.is_invulnerable = False
        self.user_events = user_event_manager
        self.invul_start()
        self.damage = 1
        self.is_atacking = False #caso seja espada, se for tiro tem que fazer a classe bullet
        self.facing = True #TRUE PARA DIREITA, FALSE PARA ESQUERDA

    def is_alive(self):
        return self.hp.healthPoints > 0

    def draw_and_update(self):
        self.draw()
        self.hp.draw_and_update()
        try:
            self.update()
        except:
            pass

    def loseHp(self, damage: int = 1):
        self.hp.lose_hp(damage, self.is_invulnerable)
        self.user_events.post_user_event(event_name.START_PLAYER_INVUL)

    def invul_start(self):
        #TODO mudar o sprite para um de invulnerabilidade
        if not self.is_invulnerable:
            self.is_invulnerable = True
            self.user_events.start_user_event_timer(self.cd, event_name.END_PLAYER_INVUL)

    def invul_end(self):
        #TODO mudar o sprite de volta
        self.is_invulnerable = False



