from player import Player

class PlayerStats:

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player in self.reader.players:
            if player.nationality == nationality:
                players.append(player)

        players.sort(key=lambda x: (x.goals + x.assists), reverse=True)

        return players