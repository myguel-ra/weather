import unittest
from unittest.mock import patch, MagicMock
from api.provider.openweathermap.weather import service


class TestOpenweathermap(unittest.TestCase):
    @patch("api.provider.openweathermap.weather.requests.get")
    def test_get_temperature(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": "200",
            "list": [{"main": {"temp": 25}, "weather": [{"main": "Rain"}]}],
        }
        mock_get.return_value = mock_response

        temperature = service.get_temperature("MockCity", 0)

        self.assertEqual(temperature, 25.0)

    @patch("api.provider.openweathermap.weather.requests.get")
    def test_will_rain(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": "200",
            "list": [{"main": {"temp": 25}, "weather": [{"main": "Rain"}]}],
        }
        mock_get.return_value = mock_response

        is_rainy = service.will_rain("MockCity", 0)

        self.assertTrue(is_rainy)

    @patch("api.provider.openweathermap.weather.requests.get")
    def test_get_forecast_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"cod": "404"}
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError):
            service._get_forecast("City", 0)


if __name__ == "__main__":
    unittest.main()
