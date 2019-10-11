from game_files.scripts import constants, enemy, zombie


class Enemies():
    def __init__(self, user_event_manager, lista_de_inimigos = None):
        self.enemies_list = list()
        if lista_de_inimigos is not None:
            self.enemies_list = lista_de_inimigos
        self.i = 1 #apenas para teste



    def get_enemy_list(self):

        if not self.enemies_list:
            for x in range(self.i):
                self.add_enemy(zombie.enemy_zombie(constants.ENEMY_ZOMBIE_SPRITE))
            self.i+=1#apenas para teste
        return self.enemies_list

    def draw_and_update(self, player, delta):
        for enemy in self.enemies_list:
            if not enemy.is_alive():
                self.enemies_list.remove(enemy)
                continue
            enemy.movement(player,delta)
            enemy.hp.draw_and_update()
            enemy.draw_and_update(delta)

    def add_enemy(self, _enemy_obj):
        self.enemies_list.append(_enemy_obj)


