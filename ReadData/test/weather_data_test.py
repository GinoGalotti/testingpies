import unittest

from weather_data import WeatherData

class WeatherTests(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.weather_data = WeatherData()

    def test_it_works(self):
        self.assertEqual(14, self.weather_data.minimum_spread())