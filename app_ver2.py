# this version of application builds on a basic ui to present weather information

# importing necesary packages
import tkinter as tk
import time as tm
import requests as re

# function to get weather data using API
def getWeather(event=None):
    city=tf.get()
    with open("api_key.txt", "r") as f:
        api_key = f.read().strip()

    url=api_key.replace("City_Name",city)
    # calling api to fetch weather data
    try:
        json_data=re.get(url).json()
    except:
        l1.config(text="Error fetching data",font=t)
        l2.config()
        return
    #storing weather data in variables
    if(json_data['cod']=="404"):
        l1.config(text="City not found")
        return
    api_call_time=json_data['list'][0]['dt']
    curr_time=int(tm.time())
    # print(api_call_time,curr_time,"diff->",abs(curr_time-api_call_time))
    c_temp=round(json_data['list'][0]['main']['temp']-273.15,1)
    condition=json_data['list'][0]['weather'][0]['description']
    max_temp=round(json_data['list'][0]['main']['temp_max']-273.15,1)
    min_temp=round(json_data['list'][0]['main']['temp_min']-273.15,1)
    pressure=json_data['list'][0]['main']['pressure']
    humidity=json_data['list'][0]['main']['humidity']
    wind_speed=json_data['list'][0]['wind']['speed']
    visibility=json_data['list'][0]['visibility']
    sunrise=json_data['city']['sunrise']+19800
    sunset=json_data['city']['sunset']+19800
    sunrise_format=tm.strftime("%I:%M",tm.gmtime(sunrise))
    sunset_format=tm.strftime("%I:%M",tm.gmtime(sunset))
    top=f"Current temperature : {c_temp} \nCondition : {condition} \nMax temperature : {max_temp} \t Min temperature : {min_temp}"
    bottom=f"Pressure : {pressure} hPa \nHumidity : {humidity} % \nWindspeed : {wind_speed} m/s \nVisibility : {round(visibility/1000,1)} km \n Sunrise : {sunrise_format} \t Sunset : {sunset_format}"
    l1.config(text=top)
    l2.config(text=bottom)


# defining the application canvas
canvas=tk.Tk()
canvas.geometry("600x500")  #setting dimensions of canvas
canvas.title("Weather Watch")   #setting title of canvas

# defining fonts for application
t=("poppins",25,"bold")
f=("poppins",15,"bold")


# defining a textfield to take name of city as input
tf=tk.Entry(font=t)
tf.pack(anchor="center",padx=10,pady=10)
tf.focus()

# defining labels for canvas
l1=tk.Label(font=t)
l2=tk.Label(font=f)
l1.pack()
l2.pack()

# binding return key with textfield
tf.bind('<Return>',getWeather)

#mainloop to keep the application active
canvas.mainloop()