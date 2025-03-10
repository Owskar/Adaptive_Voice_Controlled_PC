# services/weather.py
import requests
import streamlit as st


class WeatherService:
    def __init__(self):
        # Using a free API key - you should replace this with your own from OpenWeatherMap
        self.api_key = "bd5e378503939ddaee76f12ad7a97608"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        try:
            complete_url = f"{self.base_url}?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(complete_url)
            if response.status_code == 200:
                data = response.json()
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                weather_info = f"The weather in {city} is {desc} with a temperature of {temp}°C and humidity of {humidity}%"
                st.write(
                    f"<div class='command-result'>{weather_info}</div>",
                    unsafe_allow_html=True,
                )
                return weather_info
            else:
                error_msg = "Sorry, I couldn't fetch the weather information. Please check the city name."
                st.error(error_msg)
                return error_msg
        except Exception as e:
            error_msg = f"Error getting weather: {str(e)}"
            st.error(error_msg)
            return error_msg
