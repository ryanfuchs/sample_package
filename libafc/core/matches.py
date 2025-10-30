class Match:
    def __init__(self, id: int, teams: list):
        self.id = id
        self.teams = teams

    def summary(self):
        return f"Match {self.id} between {' vs '.join(self.teams)}"

    def __repr__(self):
        return f"<Match id={self.id} teams={self.teams}>"
