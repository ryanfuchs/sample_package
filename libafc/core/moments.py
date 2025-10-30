class Moment:
    def __init__(self, timestamp: float):
        self.timestamp = timestamp

    @classmethod
    def from_event(cls, event):
        return cls(timestamp=event.timestamp)

    def __repr__(self):
        return f"Moment({self.timestamp})"
