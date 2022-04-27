from statistics import Statistics
from query_builder import QueryBuilder
from player_reader import PlayerReader
from matchers import And, Not, HasAtLeast, HasFewerThan, PlaysIn, All, Or

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    matcher = (
        query
            .playsIn("NYR")  
            .hasAtLeast(5, "goals")  
            .hasFewerThan(10, "goals")  
            .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
