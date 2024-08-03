import requests
import tkinter as tk
from tkinter import messagebox
import get_data
from PIL import Image, ImageTk
import imageio

img = Image.open(requests.get('https://openweathermap.org/img/wn/10d@2x.png', stream=True).raw)

