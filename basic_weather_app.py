# -*- coding: utf-8 -*-
"""Basic Weather App.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mx5RAnmY40HICfIgVTNukXuF_ONJ6rBs
"""

pip install requests

!pip install pyttsx3

import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        return None

def display_weather(weather_data):
    if weather_data:
        main_data = weather_data['main']
        weather = weather_data['weather'][0]

        print(f"Location: {weather_data['name']}, {weather_data['sys']['country']}")
        print(f"Weather: {weather['description']}")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Humidity: {main_data['humidity']}%")
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    api_key = "20265ac45cf305682089c7c2785d22d1"
    city = input("Enter the city name: ")
    weather_data = get_weather(api_key, city)

    display_weather(weather_data)