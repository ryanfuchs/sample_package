import json

class Event:
    def __init__(self, timestamp: float, description: str):
        self.timestamp = timestamp
        self.description = description
    def serialize(self):
        return json.dumps({
            "timestamp": self.timestamp,
            "description": self.description
        })
