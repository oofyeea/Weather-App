import requests
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
import time
from PIL import Image, ImageTk

def get_time(): # logic for converting from GMT to EST
    hour = time.gmtime().tm_hour - 4
    min = time.gmtime().tm_min
    min_str = ''
    if min < 10:
        min_str = f'0{min}'
    else: 
        min_str = f'{min}'
    current_time = ''
    if hour == 0:
        current_time = f'12:{min_str} AM'
    elif hour < 0:
        hour = 12 + hour # since hour is negative when converted to est, it is just before midnight so this converts it to a positive value
        current_time = f'{hour}:{min_str} PM'
    elif hour == 12:
        current_time = f'12:{min_str} PM'
    elif hour > 12: 
        hour -= 12
        current_time = f'{hour}:{min_str} PM'
    else:
        current_time = f'{hour}:{min_str} AM'
    return current_time

def set_weather_icon(id):
    img = Image.open(requests.get(f'https://openweathermap.org/img/wn/{id}@2x.png', stream=True).raw)
    icon = ImageTk.PhotoImage(img)
    icon_label.configure(image=icon)
    icon_label.image = icon

def set_weather_data():
    location = city_entry.get()
    request = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={api_key}')
    if request.status_code != 200:
        messagebox.showerror('Error', 'Please enter a real city!')
        return
        
    data = {
        'temp' : request.json()['main']['temp'],
        'feels_like' : request.json()['main']['feels_like'],
        'wind' : request.json()['wind']['speed'],
        'description' : request.json()['weather'][0]['description'],
        'country' : request.json()['sys']['country'],
        'city' : request.json()['name'],
        'icon' : request.json()['weather'][0]['icon']
    }

    set_weather_icon(data["icon"])
    time_label.configure(text=f'Time: {get_time()} EST')
    location_label.configure(text=f'{data["city"]}, {data["country"]}')
    temp.configure(text=f'Temperature: {round(float(data["temp"]))}° F')
    feels_like.configure(text=f'Feels like: {round(float(data["feels_like"]))}° F')
    desc.configure(text=f'Description: {data["description"]}')
    wind.configure(text=f'Wind speed: {round(float(data["wind"]))} MPH')
    
    # move the search info to the top of the screen to display the data about weather
    search_instruction.pack(pady=(30,5))
    city_entry.pack(pady=5)
    get_weather.pack(pady=5)
    
def show_weather():
    set_weather_data()
    
api_key = open('api_key.txt',mode='r').readline()
        
root = ttk.Window(themename='morph')
root.title('Weather App')
root.geometry('500x650+700+200')

# Search Instruction Label
search_instruction = ttk.Label(root, text="Enter city name:", font=("Helvetica", 20))
search_instruction.pack(pady=(225,5))

# Search entry box
city_entry = ttk.Entry(root, style='morph')
city_entry.pack(pady=10)

# Get weather (search button basically)
get_weather = ttk.Button(root,text='Get Weather', command=show_weather, style='warning')
get_weather.pack(pady=10)

# Location + Country (title)
location_label = tk.Label(root, font='Helvetica, 25')
location_label.pack(pady=(25,10))

# Icon of weather
icon_label = tk.Label(root)
icon_label.pack(pady=(5,10))

# Time (EST)
time_label = tk.Label(root, font='Helvetica, 20')
time_label.pack(pady=(5))

# Temperature
temp = tk.Label(root, font='Helvetica, 20')
temp.pack(pady=(5))

# Feels like temperature
feels_like = tk.Label(root, font='Helvetica, 20')
feels_like.pack(pady=(5))

# Weather Description 
desc = tk.Label(root, font='Helvetica, 20')
desc.pack(pady=(5))

# Wind speed
wind = tk.Label(root, font='Helvetica, 20')
wind.pack(pady=(5))

# RUN PROGRAM
root.mainloop()
