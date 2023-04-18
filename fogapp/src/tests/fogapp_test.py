import unittest
from unittest.mock import patch
from util.fileaction import FileAction
from util.weatherdata import Weatherdata


class TestFog(unittest.TestCase):
    def setUp(self):
        self.weather = Weatherdata("new+york.json")

    def test_weatherdata_finds_correct_file(self):
        self.assertEqual(self.weather.data["id"], 5128581)

    city = 'helsinki'

    @patch('builtins.input', return_value=city)
    def test_user_input_returns_filename(self, mock_input):
        fog = FileAction()
        result = fog.user_input()
        self.assertEqual(result, 'helsinki.json')

    empty = None
    @patch('builtins.input', return_value=empty)
    def test_user_input_is_empty(self, mock_input):
        fog = FileAction()
        result = fog.user_input()
        self.assertEqual(result, "empty.json")
