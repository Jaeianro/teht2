from player_reader import PlayerReader

class StatisticsService:
    def __init__(self, player_reader: PlayerReader):
        self._player_reader = player_reader
        self._players = self._player_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player
        return None

    def team(self, team_name):
        players_of_team = filter(lambda player: player.team == team_name, self._players)
        return list(players_of_team)

    def top(self, how_many):
        def sort_by_points(player):
            return player.points

        sorted_players = sorted(self._players, reverse=True, key=sort_by_points)
        return sorted_players[:how_many]