class Player:
    def __init__(self, name, team, points, games):
        self.name = name
        self.team = team
        self.points = points
        self.games = games

    def __repr__(self):
        return f"Player(name={self.name}, team={self.team}, points={self.points}, games={self.games})"