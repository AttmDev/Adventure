from threading import Timer

class User_event_manager():
    def __init__(self):
        self.user_event_queue = list()

    def post_user_event(self, event):
        self.user_event_queue.append(event)

    def get_user_events(self):
        queue = self.user_event_queue.copy()
        self.user_event_queue.clear()
        return queue

    def __pop_event_from_queue(self):
        return self.user_event_queue.pop(0)

    def start_user_event_timer(self, time, event):
        t = Timer(time, self.post_user_event, [event])
        t.start()