from game_files.scripts import world_objects

class state_run():
    def __init__(self):
        self.ctrl = world_objects.Control(self)
        self.__STATE = 0

    def run(self):
        while True:
            if self.__STATE == 0:
                self.ctrl.menuLoop()
            elif self.__STATE == 1:
                self.ctrl.gameLoop()

            self.ctrl.draw(self.__STATE)

    def set_state(self, state):
        self.__STATE = state

    def get_state(self):
        return self.__STATE
