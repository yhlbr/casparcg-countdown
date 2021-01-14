import time
from datetime import datetime


class ShowTimeService:
    def __init__(self, sharedData):
        self.sharedData = sharedData

    def start(self):
        while True:
            time.sleep(0.1)
            if ("showRunning" not in self.sharedData) or (self.sharedData['showRunning'] != True):
                continue

            if ("showStartTime" in self.sharedData) and (isinstance(self.sharedData['showStartTime'], datetime)):
                now = datetime.now()
                diff = now - self.sharedData['showStartTime']
                hours, remainder = divmod(diff.total_seconds(), 3600)
                minutes, seconds = divmod(remainder, 60)
                current_time = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
                self.sharedData['showTimeString'] = current_time
            else:
                self.sharedData['showTimeString'] = '00:00:00'
