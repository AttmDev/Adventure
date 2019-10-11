from game_files.scripts import enemy, life_manager

class enemy_zombie(enemy.Enemy_object):

    def __init__(self, sprite):
        super().__init__(sprite, 8)
        self.set_total_duration(100)
        self.set_loop(True)

        self.hit_points = 3
        self.speed = 60
        self.hp = life_manager.Health(self, [self.x, self.y])

    def movement(self, target, delta):
        if abs(self.x-target.x) > abs(self.y-target.y):
            if self.x > target.x:
                self.set_sequence(4, 5, True)
                self.x-=self.speed *delta
            elif self.x < target.x:
                self.set_sequence(2, 3, True)
                self.x+=self.speed*delta
        else:
            if self.y > target.y:
                self.set_sequence(0, 1, True)
                self.y-=self.speed*delta
            elif self.y < target.y:
                self.set_sequence(6, 7, True)
                self.y +=self.speed*delta
