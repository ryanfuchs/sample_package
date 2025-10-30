class Player:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number

    def to_dict(self):
        return {"name": self.name, "number": self.number}

    def __str__(self):
        return f"{self.name} (#{self.number})"
