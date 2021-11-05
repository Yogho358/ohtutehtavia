import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.stats = Statistics(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name,"Semenko")
    
    def test_wrong_search_returns_none(self):
        player = self.stats.search("Zemenko")
        self.assertEqual(player,None)

    def test_team_finds_players(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players),3)

    def test_top_scorers(self):
        players = self.stats.top_scorers(3)
        third = players[2]
        self.assertEqual(third.name,"Yzerman")