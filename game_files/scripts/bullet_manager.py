from game_files.scripts import bullet, constants
from game_files.scripts.events import event_name


class Bullets():
    def __init__(self, user_event_manager):
        self.bullets = []
        self.cooldown = .5
        self.is_shooting = False
        self.events = user_event_manager

    def add_bullets(self, player):
        if not self.is_shooting:
            self.events.post_user_event(event_name.START_BULLET_TICK)
            self.bullets.append(bullet.Bullet
                                (constants.BULLET_IMAGE, 5, player))

    def get_bullets_list(self):
        return self.bullets

    def draw_and_update(self, delta_time):
        for b in self.bullets:
            if b.is_dead():
                self.bullets.remove(b)
                continue
            b.draw_and_update(delta_time)

    def tick_start(self):
        self.is_shooting = True
        self.events.start_user_event_timer(self.cooldown,
                                           event_name.END_BULLET_TICK)

    def tick_end(self):
        self.is_shooting = False

    def check_hit(self, enemies):
        for b in self.bullets:
            for e in enemies:
                if b.collided_perfect(e):
                    self.events.post_user_event(
                        event_name.DAMAGE_DEALT)
                    break
