import unittest
from unittest.mock import patch
from util.fileaction import FileAction
from util.weatherdata import Weatherdata
from datetime import datetime


class TestFog(unittest.TestCase):
    def setUp(self):
        self.weather = Weatherdata("new+york.json")

    def test_weatherdata_finds_correct_file(self):
        self.assertEqual(self.weather.data["id"], 5128581)

    def test_get_time_date(self):
        self.assertEqual(self.weather.get_time("date"), datetime(2023, 3, 31, 23, 47, 15))

    def test_get_temperature(self):
        self.assertEqual(self.weather.get_temperature("temperature_cels"), 10.8)
        self.assertEqual(self.weather.get_temperature("temperature_fahr"), 80.5)

    def test_get_feels_like(self):
        self.assertEqual(self.weather.get_temperature("feels_like_cels"), 9.5)
        self.assertEqual(self.weather.get_temperature("feels_like_fahr"), 74.8)

    def test_get_temperature_badinput(self):
        self.assertIsNone(self.weather.get_temperature("bad input"))

    def test_get_weather_badinput(self):
        self.assertIsNone(self.weather.get_weather("bad input"))

    def test_get_wind_badinput(self):
        self.assertIsNone(self.weather.get_wind("bad input"))


    city = 'helsinki'

    @patch('builtins.input', return_value=city)
    def test_user_input_returns_filename(self, mock_input):
        fog = FileAction()
        result = fog.user_input_fromfile()
        self.assertEqual(result, 'helsinki.json')

    empty = None
    @patch('builtins.input', return_value=empty)
    def test_user_input_is_empty(self, mock_input):
        fog = FileAction()
        result = fog.user_input_fromfile()
        self.assertEqual(result, "empty.json")
