from game_files.PPlay.sprite import Sprite
from game_files.scripts import constants as c

class Item_manager():
    def __init__(self, user_event_manager):
        self.itens = []
        self.events = user_event_manager

    def add_item(self, position):
        self.itens.append(Item)

    def draw_and_update(self):
        for i in self.itens:
            if i.used():
                self.itens.remove(i)
                continue
            i.draw_and_update()




class Item(Sprite):
    def __init__(self, sprite, frames, position):
        super().__init__(sprite, frames)
        self.x = position[0]
        self.y = position[1]
        self.collided = False

    def used(self):
        if self.is_colliding():
            return True
        return False

    def is_colliding(self):
        self.collided = True

    def draw_and_update(self):
        self.draw()
        self.update()

class Potion(Item):
    def __init__(self, position):
        super().__init__(c.POTION_SPRITE, 1, position)


