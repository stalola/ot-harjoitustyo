import unittest
from weatherdata import Weatherdata
from weather import Weather
from unittest.mock import patch


class TestFog(unittest.TestCase):
    def setUp(self):
        self.weather = Weatherdata("new+york.json")

    def test_weatherdata_finds_correct_file(self):
        self.assertEqual(self.weather.data["id"], 5128581)
    

    city = 'helsinki'
    @patch('builtins.input', return_value=city)
    def test_user_input_returns_filename(self, mock_input):
        result = Weather.user_input()
        self.assertEqual(result, 'helsinki.json')
