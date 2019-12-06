from game_files.scripts import enemy, life_manager
from game_files.scripts.events.event_user_calls import User_event_manager
from threading import Timer

class enemy_zombie(enemy.Enemy_object):

    def __init__(self, sprite, dificuldade):
        super().__init__(sprite, 8)
        self.set_total_duration(100)
        self.set_loop(True)
        self.podevirar = True

        self.user = User_event_manager
        self.hit_points = 3+dificuldade
        self.speed = 60+10*dificuldade
        self.hp = life_manager.Health(self, [self.x, self.y])

    def movement(self, target, delta):

        if abs(self.x-target.x) > abs(self.y-target.y):
            if self.x > target.x:
                if self.podevirar:
                    self.podevirar = False
                    t = Timer(.3, self.end_timer)
                    t.start()
                    self.set_sequence(4, 5, True)
                self.x-=self.speed *delta

            elif self.x < target.x:
                if self.podevirar:
                    self.podevirar = False
                    t = Timer(.3, self.end_timer)
                    t.start()
                    self.set_sequence(2, 3, True)
                self.x+=self.speed*delta
            if self.y > target.y:
                self.y -= self.speed/4 * delta
            else:
                if self.y != target.y:
                    self.y += self.speed/4 * delta
        else:
            if self.y > target.y:
                if self.podevirar:
                    self.podevirar = False
                    t = Timer(.3, self.end_timer)
                    t.start()
                    self.set_sequence(0, 1, True)
                self.y-=self.speed*delta
            elif self.y < target.y:
                if self.podevirar:
                    self.podevirar = False
                    t = Timer(.3, self.end_timer)
                    t.start()
                    self.set_sequence(6, 7, True)
                self.y +=self.speed*delta
            ###
            if self.x > target.x:
                self.x -= self.speed/4 * delta
            else:
                if self.x != target.x:
                    self.x += self.speed/4 * delta

    def end_timer(self):
        self.podevirar = True