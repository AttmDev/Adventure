from game_files.scripts import constants, Enemy


class Enemies():
    def __init__(self, user_event_manager, lista_de_inimigos = None):
        self.enemies_list = list()
        if lista_de_inimigos is not None:
            self.enemies_list = lista_de_inimigos

        self.enemies_list.append(Enemy.Enemy_object(constants.ENEMY_SPIKE_SPRITE))

    def get_enemy_list(self):
        return self.enemies_list

    def draw_and_update(self):
        for enemy in self.enemies_list:
            if not enemy.is_alive():
                self.enemies_list.remove(enemy)
                continue
            enemy.hp.draw_and_update()
            enemy.draw_and_update()


