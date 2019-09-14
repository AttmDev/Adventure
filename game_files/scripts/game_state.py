from game_files.scripts import control

class state_run():
    def __init__(self):
        self.ctrl = control.Control()

    def run(self):
        while True:
            STATE = self.ctrl.get_state()
            if STATE == 0:
                self.ctrl.menuLoop()
            elif STATE == 1:
                self.ctrl.gameLoop()
            self.ctrl.draw()
