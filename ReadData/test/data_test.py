import unittest

from weather_data import WeatherData
from football_data import FootballData

class WeatherTests(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.weather_data = WeatherData()

    def test_it_works(self):
        self.assertEqual(14, self.weather_data.minimum_spread())

class FootballTests(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.football_data = FootballData()

    def test_it_works(self):
        self.assertEqual("Derby", self.football_data.minimum_difference())