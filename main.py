import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime
import csv
import os.path

def get_weather(event=None):
    city = text_field.get()
    api_key = "0ddde264bc800de785beef4cb507a5d5"
    api = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
    try:
        json_data = requests.get(api).json()
        

        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = json_data['sys']['sunrise']
        sunset = json_data['sys']['sunset']
        sunrise_time = datetime.fromtimestamp(sunrise).strftime("%H:%M:%S")
        sunset_time = datetime.fromtimestamp(sunset).strftime("%H:%M:%S")


         # write weather data to CSV file
        filename = 'weather_data.csv'
        fieldnames = ['City', 'Condition', 'Temperature', 'Minimum Temperature', 'Maximum Temperature',
                      'Pressure', 'Humidity', 'Wind Speed', 'Sunrise Time', 'Sunset Time']
        
        if not os.path.isfile(filename):
            with open(filename, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
        
        with open(filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([city, condition, min_temp, max_temp, pressure, humidity, wind, sunrise_time, sunset_time])

        with open(filename, 'r', newline='') as f:
             data = f.read().replace(',', ', ')

        with open(filename, 'w', newline='') as f:
            f.write(data)




        condition_label.config(text=condition)
        temp_label.config(text=str(temp) + "°C")
        min_temp_label.config(text="Minimum Temperature: " + str(min_temp) + "°C")
        max_temp_label.config(text="Maximum Temperature: " + str(max_temp) + "°C")
        pressure_label.config(text="Pressure: " + str(pressure) + " hPa")
        humidity_label.config(text="Humidity: " + str(humidity) + "%")
        wind_label.config(text="Wind Speed: " + str(wind) + " m/s")
        sunrise_label.config(text="Sunrise Time: " + str(sunrise_time))
        sunset_label.config(text="Sunset Time: " + str(sunset_time))
    except KeyError:
        messagebox.showerror("Error", "City not found. Please enter a valid city name.")
        text_field.delete(0, tk.END)
        text_field.focus()

app = tk.Tk()
app.geometry("680x770")
app.configure(bg='white')
app.title("Weather App")

#title function
title_label = tk.Label(app, text="Weather App", font=("Arial", 20, "bold"),bg='white',fg='black')
title_label.pack(pady=20)

#textfield search button function
frame = tk.Frame(app)
frame.pack()
text_field = tk.Entry(frame, font=("poppins", 20, 'bold'),fg='black',bg='white', justify='center')
text_field.grid(row=0, column=0, padx=50, pady=50, ipadx=50, ipady=10,sticky="nsew",)
text_field.focus()
text_field.bind("<Return>", get_weather)
search_button = tk.Button(frame, text="Search", font=("Arial", 15), command=get_weather,fg='black',bg='white')
search_button.grid(row=0,column=1,padx=20)

#condition & temperature label
condition_label = tk.Label(app, font=("poppins", 35, "bold"),bg='white',fg='black')
condition_label.pack()
temp_label = tk.Label(app, font=("poppins", 35, "bold"),bg='white',fg='black')
temp_label.pack()

#information labels
min_temp_label = tk.Label(app, font=("poppins", 16, 'bold'), bg='white',fg='black')
min_temp_label.pack()

max_temp_label = tk.Label(app, font=("poppins", 16, 'bold'), bg='white',fg='black')
max_temp_label.pack()

pressure_label = tk.Label(app, font=("poppins", 16, 'bold'), bg='white',fg='black')
pressure_label.pack()

humidity_label = tk.Label(app, font=("poppins", 16, 'bold'), bg='white',fg='black')
humidity_label.pack()

wind_label = tk.Label(app, font=("poppins", 16, 'bold'), bg='white',fg='black')
wind_label.pack()

sunrise_label = tk.Label(app, font=("poppins", 16, 'bold'), bg='white',fg='black')
sunrise_label.pack()

sunset_label = tk.Label(app, font=("poppins", 16, 'bold'), bg='white',fg='black')
sunset_label.pack()

app.mainloop()

