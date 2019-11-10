from game_files.PPlay import window as win
from game_files.PPlay.gameimage import GameImage
from game_files.scripts import constants as c, world
from game_files.scripts.events import event_handler, event_user_calls


class Control():
    def __init__(self, state):
        self.screen = win.Window(c.width, c.height)
        self.screen.set_title(c.TITTLE)
        self.mouse = self.screen.get_mouse()
        self.state_manager = state
        self.user_events = event_user_calls.User_event_manager()


        self.background = GameImage(c.BACKGROUND_IMAGE)

        self.titleImage = GameImage(c.MENU_TITTLE_IMAGE)
        self.titleImage.x = (c.width - self.titleImage.width) / 2
        self.titleImage.y = c.height / 12

        self.playButton = GameImage(c.MENU_PLAY_IMAGE[0]), GameImage(c.MENU_PLAY_IMAGE[1])
        for item in self.playButton:
            item.x = (c.width - item.width) / 2
            item.y = (c.height / 2)


        self.game_world = world.World_objects(self.user_events, self.screen)
        self.events = event_handler.Game_event_handler(self.user_events)



    def draw_state(self, STATE):
        if STATE == 0:
            self.menu_loop()
            self.background.draw()
            self.titleImage.draw()

        elif STATE == 1:
            self.background.draw()
            self.game_world.draw_and_update()
            self.game_world.test_bullet_enemy()
            self.game_world.test_damage_on_player()
            self.game_world.test_item_player()
            self.events.run(self.screen.delta_time(), self.game_world)
            self.screen.update()

    def menu_loop(self):
        if self.mouse.is_over_object(self.playButton[0]):
            self.playButton[1].draw()
            if self.mouse.is_button_pressed(1):
                self.screen.clear()
                self.state_manager.set_state(1)
        else:
            self.playButton[0].draw()
        self.screen.update()




