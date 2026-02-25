import requests
from pprint import pprint
from datetime import datetime
from typing import Dict, Union
import requests


def current_weather(lat: float, lon: float) -> Dict[str, Union[str, float]]:

    api_key = "0a7c7f6e0c0a426b977182128262502"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"

    response = requests.get(url)
    data = response.json()

    result = {
        "city": data['location']['name'],
        "time": data['current']['last_updated'].split()[1],
        "temp": data['current']['temp_c'],
        "feels_like_temp": data['current']['feelslike_c'],
        "pressure": round(data['current']['pressure_mb'] * 0.75, 1),
        "humidity": data['current']['humidity'],
        "wind_speed": round(data['current']['wind_kph'] / 3.6, 1),
        "wind_gust": round(data['current']['gust_kph'] / 3.6, 1),
        "wind_dir": data['current']['wind_dir']
    }

    return result
if __name__ == "__main__":
    weather_data = current_weather(59.93, 30.31)
    print("Текущая погода:")
    for key, value in weather_data.items():
        print(f"{key}: {value}")