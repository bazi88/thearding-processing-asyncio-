from threading import Thread, Event
from time import sleep, perf_counter

class Child(Thread):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event

    def run(self):
        for i in range(10):
            print(f"Running child {i}")
            if self.event.is_set():
                print(f"Child {i} exiting")
                break
            else: