# Placeholder for analytics logic related to space-time analysis.

class SpaceTimeCoordinate:
    def __init__(self, x: float, y: float, t: float):
        self.x = x
        self.y = y
        self.t = t

    def scale_time(self, factor: float):
        self.t *= factor
