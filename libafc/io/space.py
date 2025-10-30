# Placeholder for IO logic related to space dimensions.

class Space:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def contains(self, x: float, y: float) -> bool:
        return 0 <= x <= self.width and 0 <= y <= self.height
