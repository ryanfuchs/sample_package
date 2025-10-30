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

    def update_description(self, new_description: str):
        self.description = new_description

    def __str__(self):
        return f"Event at {self.timestamp}: {self.description}"
