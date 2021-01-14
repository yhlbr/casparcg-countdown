import time
from datetime import datetime


class ShowTimeService:
    def __init__(self, sharedData):
        self.sharedData = sharedData

    def start(self):
        while True:
            time.sleep(0.1)
            if "showStartTime" in self.sharedData and isinstance(self.sharedData['showStartTime'], datetime.datetime):
                now = datetime.now()
                diff = now - self.sharedData['showStartTime']
                current_time = diff.strftime("%H:%M:%S")
                self.sharedData['showTimeString'] = current_time
            else:
                self.sharedData['showTimeString'] = '00:00:00'