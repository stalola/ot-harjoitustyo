import unittest
from unittest.mock import patch
from util.apimanipulation import APIManipulation
from util.weatherdata import Weatherdata


class TestFog(unittest.TestCase):
    def setUp(self):
        self.weather = Weatherdata("New York")

    def test_weatherdata_finds_correct_data(self):
        self.assertEqual(self.weather.data["id"], 5128581)

    def test_get_temperature(self):
        self.assertIsNotNone(self.weather.get_temperature("temperature_cels"))
        self.assertIsNotNone(self.weather.get_temperature("temperature_fahr"))

    def test_get_feels_like(self):
        self.assertIsNotNone(self.weather.get_temperature("feels_like_cels"))
        self.assertIsNotNone(self.weather.get_temperature("feels_like_fahr"))

    def test_get_temperature_badinput(self):
        self.assertIsNone(self.weather.get_temperature("bad input"))

    def test_get_weather_badinput(self):
        self.assertIsNone(self.weather.get_weather("bad input"))

    def test_get_wind_badinput(self):
        self.assertIsNone(self.weather.get_wind("bad input"))


    city = 'HeLsInki'

    @patch('builtins.input', return_value=city)
    def test_user_input_returns_filename(self, mock_input):
        fog = APIManipulation()
        result = fog.user_input_city()
        self.assertEqual(result, 'helsinki')

    def test_wind_direction(self):
        self.assertEqual(self.weather.wind_degrees_to_cardinal(360), "north")

    def test_wind_direction_bad_input(self):
        self.assertEqual(self.weather.wind_degrees_to_cardinal(361), "unknown")
