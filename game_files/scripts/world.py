from math import sqrt

from game_files.PPlay import collision
from game_files.scripts import constants, enemies_manager, bullet, bullet_manager, player_manager, hotbar, sfx_manager
from game_files.scripts.events import event_name


class World_objects():
    def __init__(self, user_event_manager, screen):
        self.screen = screen
        self.user_event = user_event_manager
        self.enemies_list = enemies_manager.Enemies(self.user_event, )
        self.player = player_manager.Player(self.user_event)
        self.inventory = hotbar.Inventory()
        self.enemy_colliding = None
        self.sfx = sfx_manager.sfx()
        self.bullets = bullet_manager.Bullets(self.user_event, self.sfx)

    def test_damage_on_player(self):
        for enemy in self.enemies_list.get_enemy_list():
            if collision.Collision.collided(self.player, enemy):
                # print(f"player colidindo com objeto em x:{enemy.x} y:{enemy.y}")
                self.enemy_colliding = enemy #eu fiz duas vezes só pra garantir HSEIUAHEIUA
                self.enemy_colliding = enemy #eu fiz duas vezes só pra garantir HSEIUAHEIUA
                self.user_event.post_user_event(event_name.DAMAGE_RECEIVED)

    def test_bullet_enemy(self):
        for b in self.bullets.get_bullets_list():
            for e in self.enemies_list.get_enemy_list():
                if collision.Collision.collided(b, e):
                    self.enemy_colliding = e
                    e.knocked_back(b.direction_player)
                    b.is_colliding()
                    self.user_event.post_user_event(event_name.DAMAGE_DEALT)
                    break

    def get_player(self):
        return self.player

    def get_enemy_list(self):
        return self.enemies_list.get_enemy_list()

    def draw_and_update(self):
        self.inventory.draw()
        self.enemies_list.draw_and_update(self.player, self.screen.delta_time())
        self.sfx.draw_and_update()
        self.bullets.draw_and_update(self.screen.delta_time())
        self.player.draw_and_update()

    def distance_between_objects(self, obj1, obj2):
        return sqrt((obj2.x-obj1.x) ** 2 + (obj2.y-obj1.y) ** 2)

    def move_to_obj(self, obj1, obj2):
        pos_to_move = obj2.x - obj1.x, obj2.y - obj1.y
        if pos_to_move[0] > 0:
            obj1.move_x(obj1.speed * self.screen.delta_time())
        else:
            obj1.move_x(-obj1.speed * self.screen.delta_time())
        if pos_to_move[1] > 0:
            obj1.move_y(obj1.speed * self.screen.delta_time())
        else:
            obj1.move_y(-obj1.speed * self.screen.delta_time())

    def get_vector_between_obj(self, obj1, obj2):
        pass