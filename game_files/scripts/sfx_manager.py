
class sfx():
    def __init__(self):
        self.sfx_list = []

    def draw_and_update(self):
        for sfx_item in self.sfx_list:
            if sfx_item.to_destroy == True:
                self.sfx_list.remove(sfx_item)
                continue
            frame = sfx_item.draw_and_update()

    def add_to_list(self, sfx):
        self.sfx_list.append(sfx)
