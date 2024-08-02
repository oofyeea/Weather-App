import requests
import tkinter as tk
from tkinter import messagebox

api_key = open('api_key.txt',mode='r').readline()
        
root = tk.Tk('hello')
root.title('Weather App')
root.geometry('500x650+700+200')
search_instruction = tk.Label(root, text="Enter city name:", font=("Helvetica", 20)).pack(pady=(200,20),side='top')
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

def show_weather():
    location = city_entry.get()
    request = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={api_key}')
    if request.status_code != 200:
        messagebox.showerror('Error', 'Please enter a real city!')
        return
        
    data = {
        'temp' : request.json()['main']['temp'],
        'feels_like' : request.json()['main']['feels_like'],
    }
    print(data['temp'])

    
get_weather = tk.Button(root,text='Get Weather', command=show_weather)
get_weather.pack(pady=10)
