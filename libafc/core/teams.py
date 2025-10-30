class Team:
    def __init__(self, name: str, players: list):
        self.name = name
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def get_roster(self):
        return [str(p) for p in self.players]

    def __repr__(self):
        return f"Team({self.name}, {len(self.players)} players)"
