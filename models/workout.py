from math import floor
from statistics import mean


class Workout:
    def __init__(self, activity, start, duration, bpm_values):
        self.activity = activity
        self.start = start
        self.duration = duration
        self.bpm_values = bpm_values

    def get_average_heartrate(self):
        return floor(mean(self.bpm_values))

    def get_max_heartrate(self):
        return max(self.bpm_values)