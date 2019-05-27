import unittest

import weather_data
import football_data

class WeatherTests(unittest.TestCase):

    def test_it_works(self):
        self.assertEqual("14", weather_data.minimum_difference())

class FootballTests(unittest.TestCase):

    def test_it_works(self):
        self.assertEqual("Derby", football_data.minimum_difference())