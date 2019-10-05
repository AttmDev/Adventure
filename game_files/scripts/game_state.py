from game_files.scripts import control_center

class state_run():
    def __init__(self):
        self.ctrl = control_center.Control(self)
        self.__STATE = 0

    def run(self):
        while True:
            self.ctrl.draw_state(self.__STATE)


    def set_state(self, state):
        self.__STATE = state

    def get_state(self):
        return self.__STATE
