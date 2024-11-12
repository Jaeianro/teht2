import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        # Kovakoodattu pelaajalista
        return [
            Player("Alice", "Team A", 25, 30),  # 55 pistettä
            Player("Bob", "Team A", 20, 10),    # 30 pistettä
            Player("Charlie", "Team B", 15, 25), # 40 pistettä
            Player("David", "Team B", 30, 40),  # 70 pistettä
            Player("Eve", "Team C", 35, 20)     # 55 pistettä
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # Testiluokan alustuksessa luodaan PlayerReaderStub ja StatisticsService
        self.reader = PlayerReaderStub()
        self.service = StatisticsService(self.reader)

    def test_search_existing_player(self):
        player = self.service.search("Alice")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Alice")
    
    def test_search_non_existing_player(self):
        player = self.service.search("Nonexistent Player")
        self.assertIsNone(player)

    def test_search_partial_name(self):
        player = self.service.search("Al")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Alice")


    def test_team(self):
        team_a_players = self.service.team("Team A")
        self.assertEqual(len(team_a_players), 2)
        self.assertEqual(team_a_players[0].name, "Alice")
        self.assertEqual(team_a_players[1].name, "Bob")

    
    def test_top_zero_players(self):
        top_players = self.service.top(0)
        self.assertEqual(top_players, [])  # Ei voida ottaa nollaa pelaajia  
    
    def test_top_more_than_available_players(self):
        top_players = self.service.top(10)  # Pyydetään enemmän pelaajia kuin on olemassa
        self.assertEqual(len(top_players), 5)  # Meillä on vain 5 pelaajaa      
    
      
