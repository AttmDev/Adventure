from game_files.scripts import enemies_manager, player_manager, hotbar
from game_files.scripts.events import event_name
from math import sqrt


class World_objects():
    def __init__(self, user_event_manager, screen):
        self.screen = screen
        self.user_event = user_event_manager
        self.enemies_list = enemies_manager.Enemies(user_event_manager=self.user_event)
        self.player = player_manager.Player(self.user_event)
        self.inventory = hotbar.Inventory()
        self.enemy_colliding = None

    def test_for_battle(self):
        for enemy in self.enemies_list.get_enemy_list():
            #print(self.distance_between_objects(self.player, enemy))
            if self.distance_between_objects(self.player, enemy) < 300:
                self.move_to_obj(enemy, self.player)

            if self.player.collided_perfect(enemy):
                # print(f"player colidindo com objeto em x:{enemy.x} y:{enemy.y}")
                self.enemy_colliding = enemy
                self.user_event.post_user_event(event_name.START_BATTLE)

    def get_player(self):
        return self.player

    def get_enemy_list(self):
        return self.enemies_list.get_enemy_list()

    def draw_and_update(self):
        self.inventory.draw()
        self.enemies_list.draw_and_update()
        self.player.draw_and_update()

    def distance_between_objects(self, obj1, obj2):
        return sqrt((obj2.x-obj1.x) ** 2 + (obj2.y-obj1.y) ** 2)

    def move_to_obj(self, obj1, obj2):
        pos_to_move = obj2.x - obj1.x, obj2.y - obj1.y
        if pos_to_move[0]>0:
            obj1.move_x(obj1.speed * self.screen.delta_time())
        else:
            obj1.move_x(-obj1.speed * self.screen.delta_time())
        if pos_to_move[1]>0:
            obj1.move_y(obj1.speed * self.screen.delta_time())
        else:
            obj1.move_y(-obj1.speed * self.screen.delta_time())
