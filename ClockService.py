import time
from datetime import datetime


class ClockService:
    def __init__(self, sharedData):
        self.sharedData = sharedData

    def start(self):
        while True:
            time.sleep(0.1)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.sharedData['curTimeString'] = current_time