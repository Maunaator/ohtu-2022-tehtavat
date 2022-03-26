import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    date = requests.get(url).headers['Date']
    response = requests.get(url).json()
    

    #print("JSON-muotoinen vastaus:")
    #print(response)
    #print(date)

    nationality = 'FIN'
    players = []

    for player_dict in response:
        if player_dict['nationality'] == nationality:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists']
            )

            players.append(player)

    print("Players from " + nationality + " " + date)
    print("")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()