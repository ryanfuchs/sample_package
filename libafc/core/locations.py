class Location:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, other):
        # Simplified Euclidean distance (not accurate for global scale)
        return ((self.latitude - other.latitude)**2 + (self.longitude - other.longitude)**2 ) ** 0.5

    def __repr__(self):
        return f"Location(lat={self.latitude}, lon={self.longitude})"
