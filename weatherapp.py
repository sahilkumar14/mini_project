import tkinter as tk
import requests
from tkinter import font

HEIGHT = 500
WIDTH = 600


def city_name(entry):
    print("entry is :", entry)
def format(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        feels_like = weather['main']['feels_like']
        wind_speed = weather['wind']['speed']  
        final =  'city: %s \ncondition: %s \ntemperature(°C): %s \nfeels_like: %s \nwind_speed: %s' %(name,desc,temp,feels_like,wind_speed)
    except:
        final = 'city entered is not present.'
    return final

def get_weather(city):
    weather_key = 'c1137eceb90543f503993200ed124e90'
    url = 'HTTPS://api.openweathermap.org/data/2.5/weather'
    params = {'appid': weather_key, 'q': city, 'units':'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label_lower['text'] = format(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="landscapeimg.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#49d049", bd=4.5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=('courier',15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('courier',13),command = lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#49d049", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label_lower = tk.Label(lower_frame, font=('courier',15),anchor='nw',justify='left', bd = 4)
label_lower.place(relwidth=1, relheight=1)

root.mainloop()
