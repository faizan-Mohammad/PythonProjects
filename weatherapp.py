import requests
from tkinter import *

API_KEY = "[REPLACE WITH YOUR OWN API KEY(CREATE AN ACCOUNT FOR OPENWEATHERMAP)]"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


# GO Button definition, Process
def go():
    city_name = city_entry.get()
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }


    response = requests.get(BASE_URL, params=params)

    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    desctription = data["weather"][0]["description"]

    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {desctription}")

    stats_temp = Label(window, text=f"Temperature: {temperature} °C")
    stats_humid = Label(window, text=f"Humidity: {humidity}%")
    stats_desc = Label(window, text=f"Description: {desctription}")

    stats_temp.pack()
    stats_humid.pack()
    stats_desc.pack()

window = Tk()

# TK Widgets
entrcty_label = Label(window, text="Enter a City Name to Get Weather Stats:", font=(20))
entrcty_label.pack()

city_entry = Entry()
city_entry.config(font=(10))
city_entry.pack()

go_btn = Button(window, text="-->", command=go)
go_btn.pack()



window.mainloop()
