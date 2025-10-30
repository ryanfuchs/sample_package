# Placeholder for IO logic related to time dimensions.

class TimeWindow:
    def __init__(self, start: float, end: float):
        self.start = start
        self.end = end

    def contains(self, t: float) -> bool:
        return self.start <= t <= self.end
