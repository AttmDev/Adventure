from game_files.scripts import constants, zombie
from random import randint
from game_files.scripts.events import event_user_calls, event_name

class Enemies():
    def __init__(self, user_event_manager, lista_de_inimigos = None):
        self.enemies_list = list()
        self.dropped_item = True
        if lista_de_inimigos is not None:
            self.enemies_list = lista_de_inimigos
        self.i = 1 #apenas para teste
        # self.user_event = event_user_calls.User_event_manager()
        self.round = 0


    def get_enemy_list(self):
        if not self.enemies_list:
            self.round+=1

            # self.user_event.post_user_event(event_name.ROUND_INCREMENT)
            spawn_raro = 20
            for x in range(self.i):

                rand = randint(0, spawn_raro)
                self.add_enemy(zombie.enemy_zombie(constants.ENEMY_ZOMBIE_SPRITE[:-4]+
                                                   str(0 if rand>4 else rand)+
                                                   constants.ENEMY_ZOMBIE_SPRITE[-4:],
                                                   0 if rand>4 else rand))
            self.i+=1#apenas para teste
        return self.enemies_list

    def draw_and_update(self, player, item_manager, delta):
        for enemy in self.enemies_list:
            if not enemy.is_alive():
                self.died(enemy, item_manager)
                continue
            enemy.movement(player,delta)
            enemy.hp.draw_and_update()
            enemy.draw_and_update(delta)

    def add_enemy(self, _enemy_obj):
        self.enemies_list.append(_enemy_obj)

    def will_drop(self, chance): #chance em porcentagem, ex: x.will_drop(70) p/ 70% de chance de ocorrer
        return randint(0, 200) <= chance

    def died(self, enemy, item_manager):
        if self.will_drop(70):
            item_manager.add_item_ground((enemy.x, enemy.y))
        self.enemies_list.remove(enemy)





