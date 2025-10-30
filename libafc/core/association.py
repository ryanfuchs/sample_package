class Association:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Association):
            return self.name == other.name
        return False

    def __str__(self):
        return f"Association({self.name})"
