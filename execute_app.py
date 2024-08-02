import tkinter as tk
from tkinter import messagebox
import requests

# Constants
API_KEY = '219bf061e78ee2f47aa7aad37dff542c'  # Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Function to fetch weather data
def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# Function to display weather data
def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    weather_data = get_weather(city)
    if weather_data.get('cod') != 200:
        messagebox.showerror("Error", weather_data.get('message', 'Error fetching data'))
        return

    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    result_label.config(text=f"City: {city}\nTemperature: {temp}°C\nDescription: {description}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s")

# Set up the Tkinter window
root = tk.Tk()
root.title("Weather App")

# Create and place widgets
tk.Label(root, text="Enter city name:").pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=show_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()