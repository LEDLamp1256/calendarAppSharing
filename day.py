from typing import List

from event import Event
class Day:
    def __init__(self, day: int, month: int, year: int, events=None):
        if events is None:
            events = []
        self.day = day
        self.month = month
        self.year  = year
        self.events: List[Event] = events

