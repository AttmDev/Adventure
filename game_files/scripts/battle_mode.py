from game_files.scripts.events import event_name


class Battle():
    def __init__(self, event_calls):
        self.event_dispatcher = event_calls


    def run(self):
        self.event_dispatcher.post_user_event(event_name.DAMAGE_RECEIVED)
        self.event_dispatcher.post_user_event(event_name.DAMAGE_DEALT)

