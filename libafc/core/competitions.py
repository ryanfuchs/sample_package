class Competition:
    _registry = []
    def __init__(self, name: str):
        self.name = name
        Competition._registry.append(self)

    @classmethod
    def list_names(cls):
        return [c.name for c in cls._registry]

    def __str__(self):
        return f"Competition({self.name})"
