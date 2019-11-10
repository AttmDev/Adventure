from game_files.PPlay.sprite import Sprite
from game_files.PPlay.gameimage import GameImage
from game_files.scripts import constants as c
from game_files.scripts.events import event_name


class Item_manager():
    def __init__(self, user_event_manager):
        self.itens = []
        self.inventory_itens = []
        self.inventory_place = GameImage(c.INV_BAR_HUD_IMAGE)
        self.inventory_place.x = c.HUD_SPACER
        self.inventory_place.y = c.HUD_SPACER
        self.events = user_event_manager
        self.using_item = False
        self.cooldown = 0.2

    def get_item_list(self):
        return self.itens

    def add_item_ground(self, position):
        self.itens.append(Potion(position))

    def use_item(self, player, bullets):
        if not self.using_item and len(self.inventory_itens) > 0:
            self.events.post_user_event(event_name.START_ITEM_USED)
            self.inventory_itens[0].use_item(player, bullets)
            self.inventory_itens.remove(self.inventory_itens[0])

    def tick_start(self):
        self.using_item = True
        self.events.start_user_event_timer(self.cooldown, event_name.END_ITEM_USED)

    def tick_end(self):
        self.using_item = False

    def loot_item(self, item):
        if len(self.inventory_itens) < 2:
            item.x = self.inventory_place.x + (self.inventory_place.width - item.width)/2
            item.y = self.inventory_place.y + (self.inventory_place.height - item.height) / 2
            self.inventory_itens.append(item)

    def draw_up_invent(self):
        self.inventory_place.draw()
        if len(self.inventory_itens)>0:
            self.inventory_itens[0].draw_and_update()


    def draw_up_ground(self):
        for i in self.itens:
            if i.gotten():
                self.loot_item(i)
                self.itens.remove(i)
                continue
            i.draw_and_update()

    def draw_and_update(self):
        self.draw_up_ground()
        self.draw_up_invent()




class Item(Sprite):
    def __init__(self, sprite, position):
        super().__init__(sprite)
        self.x = position[0]
        self.y = position[1]
        self.collided = False
        self.used = False
        self.set_total_duration(1)

    def gotten(self):
        if self.collided:
            return True
        return False

    def is_colliding(self):
        self.collided = True

    def draw_and_update(self):
        self.draw()
        self.update()

class Potion(Item):
    def __init__(self, position):
        super().__init__(c.POTION_SPRITE, position)

    def use_item(self, player, bullets):
        player.hp.get_hp(2)
        self.used = True

class Shotgun(Item):
    def __init__(self, position):
        super().__init__(c.SHOTGUN_SPRITE, position)
