# Placeholder for analytics logic related to shape graphs.

class ShapeGraph:
    def __init__(self, points: list):
        self.points = points

    def centroid(self):
        if not self.points:
            return None
        x = sum(pt[0] for pt in self.points) / len(self.points)
        y = sum(pt[1] for pt in self.points) / len(self.points)
        return (x, y)
