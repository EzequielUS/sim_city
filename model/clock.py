from datetime import datetime as time

class Clock:
    def __init__(self):
        self.time = time.now()

    def get_time(self):
        return f"Time: {self.time}"

    def advance_time(self):
        self.time += 1