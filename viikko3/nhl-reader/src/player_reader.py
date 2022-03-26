from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        self.players = []
        self.date = ""

        self.init(url)

    def init(self, url):
        self.date = requests.get(url).headers['Date']
        response = requests.get(url).json()

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['nationality'],
                player_dict['goals'],
                player_dict['assists']
            )
            self.players.append(player)


