import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    
    
    def get_players(self):
        return [
            Player("Huuko", "A", 6, 55),
            Player("Hiiko", "CD", 15, 50),
            Player("Hii", "B", 26, 40),
            Player("Huu", "A", 25, 45),
            Player("Haa", "A", 10, 37),
            Player("Hoo", "B", 22, 41)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())
    
    def test_search_palauttaa_none_jos__ei_loydy(self):
        self.assertEqual(self.statistics.search("Muuga"), None)

    def test_search_loytaa_pelaajan(self):
        # str vertailu ei varmaan järkevin tapa
        self.assertEqual(str(self.statistics.search("Huuko")), str(Player("Huuko", "A", 6, 55)))
    
    def test_team_palauttaa_tyhjan_listan_jos_ei_joukuetta(self):
        self.assertEqual(self.statistics.team("X"), [])
    
    def test_team_palauttaa_oikeat_pelaajat(self):
        pelaajat = self.statistics.team("B")
        pelaajatStr = str(pelaajat[0]) + str(pelaajat[1])
        self.assertEqual(pelaajatStr, str(Player("Hii", "B", 26, 40)) + str(Player("Hoo", "B", 22, 41)))

    def test_top_scorers_jarjestaa_oikein(self):
        # annettu top_scorers metodi palauttaa yhden enemmän kuin pyydetty (how_many)
        pelaajat = self.statistics.top_scorers(2)
        pelaajatStr = str(pelaajat[0]) + str(pelaajat[1]) + str(pelaajat[2])
        testiStr = str(Player("Huu", "A", 25, 45)) + str(Player("Hii", "B", 26, 40)) + str(Player("Hiiko", "CD", 15, 50))
        self.assertEqual(pelaajatStr,testiStr)
