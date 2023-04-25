import datetime
from util.fileaction import FileAction


class WeatherdataFromApi:
    def __init__(self, url):
        self.data = FileAction.access_data_w_api(self, url)
        self.city = self.data["name"]
        self.timestamp = self.data["dt"]
        self.timezone = self.data["timezone"]

    def get_time(self, name):
        date = datetime.datetime.fromtimestamp(self.timestamp)
        sunrise_utc = self.data["sys"]["sunrise"]
        sunset_utc = self.data["sys"]["sunset"]
        if name == "date":
            return date
        if name == "sunrise_utc":
            return sunrise_utc
        if name == "sunset_utc":
            return sunset_utc
        return None

    def get_temperature(self, name):
        temperature_kelv = self.data["main"]["temp"]
        feels_like_kelv = self.data["main"]["feels_like"]
        temperature_cels = round(temperature_kelv-273.15, 1)
        feels_like_cels = round(feels_like_kelv-273.15, 1)
        temperature_fahr = round((temperature_kelv-273.15)*9/2+32, 1)
        feels_like_fahr = round((feels_like_kelv-273.15)*9/2+32, 1)
        if name == "temperature_cels":
            return temperature_cels
        if name == "temperature_fahr":
            return temperature_fahr
        if name == "feels_like_cels":
            return feels_like_cels
        if name == "feels_like_fahr":
            return feels_like_fahr
        return None

    def get_weather(self, name):
        humidity = self.data["main"]["humidity"]
        pressure = self.data["main"]["pressure"]
        clouds = self.data["clouds"]["all"]
        weather_group = self.data["weather"][0]["main"]
        weather_description = self.data["weather"][0]["description"]
        weather_icon = self.data["weather"][0]["icon"]
        if name == "humidity":
            return humidity
        if name == "pressure":
            return pressure
        if name == "clouds":
            return clouds
        if name == "weather_group":
            return weather_group
        if name == "weather_description":
            return weather_description
        if name == "weather_icon":
            return weather_icon
        return None

    def get_wind(self, name):
        wind_speed_met = self.data["wind"]["speed"]
        wind_speed_imp = round(wind_speed_met*2.236936, 2)
        wind_deg = self.data["wind"]["deg"]
        if name == "wind_speed_met":
            return wind_speed_met
        if name == "wind_speed_imp":
            return wind_speed_imp
        if name == "wind_deg":
            return wind_deg
        return None
