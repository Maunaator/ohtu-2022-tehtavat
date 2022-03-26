from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    nationality = "FIN"
    players = stats.top_scorers_by_nationality(nationality)

    print("Players from " + nationality + " on " + reader.date)
    print("")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()