#!/usr/bin/env python3
# Student ID: fouwhumiakpo

class Time:
    """Simple object type for time of the day.
       data attributes: hour, minute, second
       function attributes: __init__, __str__, __repr__,
                            time_to_sec, format_time,
                            change_time, sum_times
    """

    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        '''return a string representation for the object self'''
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        '''return a string representation for the object self'''
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'


    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __add__(self, t2):
        return self.sum_times(t2)

    def sum_times(self, t2):
        self_sec = self.time_to_sec()
        t2_sec = t2.time_to_sec()
        total_sec = self_sec + t2_sec
        return sec_to_time(total_sec)

    def change_time(self, seconds):
        total_sec = self.time_to_sec() + seconds
        new_time = sec_to_time(total_sec)
        self.hour = new_time.hour
        self.minute = new_time.minute
        self.second = new_time.second
        return None

    def time_to_sec(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True

def sec_to_time(seconds):
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t
