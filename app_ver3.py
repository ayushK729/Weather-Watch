# this version of weather application builds on the UI design , giving users a proper view of weather report

import tkinter as tk
import customtkinter as ctk
from PIL import Image,ImageTk
import requests as rq

WEATHER_ICONS={
    "Clear": "sun.png",
    "Clouds": "cloud.png",
    "Rain": "rain.png",
    "Drizzle": "rain.png",
    "Thunderstorm": "storm.png",
    "Snow": "snow.png",
    "Mist": "fog.png",
    "Haze": "fog.png",
    "Fog": "fog.png"
}

# function for ctk image handling
def load_icon(path,size=(24,24)):
    return ctk.CTkImage(
        light_image=Image.open(path),
        dark_image=Image.open(path),
        size=size
    )

def getWeather(event=None):
    city=city_entry.get()
    with open("api_key.txt", "r") as f:
        api_key = f.read().strip()

    url=api_key.replace("City_Name",city)
    try:
        json_data=rq.get(url).json()
    except:
        print("Error fetching data")
        return
    
    currentTemp=json_data['list'][0]['main']['temp']
    minTemp=json_data['list'][0]['main']['temp_min']
    maxTemp=json_data['list'][0]['main']['temp_max']
    humidity_d=json_data['list'][0]['main']['humidity']
    desc=(json_data['list'][0]['weather'][0]['description']).title()
    windSpeed=json_data['list'][0]['wind']['speed']
    visibility_d=json_data['list'][0]['visibility']
    pressure_d=json_data['list'][0]['main']['pressure']
    city_label.configure(text=city.title())
    weather_main=json_data['list'][0]['weather'][0]['main']
    currTemp.configure(text=f"{round(currentTemp,1)}\u00B0C")
    max_temp.configure(text=f"{round(maxTemp,1)}\u00B0C")
    min_temp.configure(text=f"{round(minTemp,1)}\u00B0C")
    humidity.configure(text=f"{humidity_d}%")
    visibility.configure(text=f"{visibility_d/1000} km")
    wind_speed.configure(text=f"{windSpeed} m/s")
    pressure.configure(text=f"{pressure_d} hPa")
    description.configure(text=f"{desc.title()}")


    # dynamic icons
    icon_file=WEATHER_ICONS.get(weather_main,"storm.png")
    icon_path=f"res/icons/{icon_file}"

    currW_img.configure(
        light_image=Image.open(icon_path),
        dark_image=Image.open(icon_path)
    )



# defining the application canvas
app=ctk.CTk()
app.geometry("430x832")
app.resizable(False,False)
app.title("Weather Watch")
app.iconbitmap("res/app_icon.ico")
ctk.set_appearance_mode("light")

white_code="#F2F2F7"

# setting background to white
app.config(background=white_code)

# defining the fonts
f=("Segoe UI", 24, "bold")
t=("Segoe UI", 13,)

# building first container and respective elements
container1=ctk.CTkFrame(app,width=310,height=280,fg_color="#e1e1e3",bg_color=white_code,corner_radius=12)
container1.pack(pady=20,padx=10)
container1.pack_propagate(False)

# city label
city_label=ctk.CTkLabel(container1,text="City Name",font=f)
city_label.pack(pady=20)

# creating Ctk image for weather icons
currW_img=ctk.CTkImage(
        light_image=Image.open("res/icons/storm.png"),
        dark_image=Image.open("res/icons/storm.png"),
        size=(90,90)
    )
currWeather=ctk.CTkLabel(container1,text="",image=currW_img)
currWeather.pack(pady=5)

# current temp
currTemp=ctk.CTkLabel(container1,text="Current Weather",font=f)
currTemp.pack(pady=5)

# current weather description
description=ctk.CTkLabel(container1,text="Description",font=f)
description.pack(pady=5)


# building second container for holding data
gridContainer=ctk.CTkFrame(app,fg_color="#e1e1e3",bg_color=white_code,width=320,height=230,corner_radius=12)
gridContainer.pack(pady=5)
gridContainer.grid_propagate(False)
gridContainer.grid_rowconfigure((0,1,2),weight=1)
gridContainer.grid_columnconfigure((0,1),weight=1)

containerIconSize=(22,22)
minTempIcon=load_icon("res/icons/min_temp.png",size=containerIconSize)
min_temp=ctk.CTkLabel(gridContainer,text="Min Temp",image=minTempIcon,font=t,compound="bottom")
min_temp.grid(row=0,column=0,padx=40,pady=5,sticky="nsew")

maxTempIcon=load_icon("res/icons/max_temp.png",size=containerIconSize)
max_temp=ctk.CTkLabel(gridContainer,text="Max Temp",font=t,image=maxTempIcon,compound="bottom")
max_temp.grid(row=0,column=1,padx=40,pady=5,sticky="nsew")

humidityIcon=load_icon("res/icons/humidity.png",size=containerIconSize)
humidity=ctk.CTkLabel(gridContainer,text="Humidity",font=t,image=humidityIcon,compound="bottom")
humidity.grid(row=1,column=0,padx=40,pady=5,sticky="nsew")

visibilityIcon=load_icon("res/icons/visib.png",size=containerIconSize)
visibility=ctk.CTkLabel(gridContainer,text="Visibility",font=t,image=visibilityIcon,compound="bottom")
visibility.grid(row=1,column=1,padx=40,pady=5,sticky="nsew")

windSpeedIcon=load_icon("res/icons/wind.png",size=containerIconSize)
wind_speed=ctk.CTkLabel(gridContainer,text="Wind Speed",font=t,image=windSpeedIcon,compound="bottom")
wind_speed.grid(row=2,column=0,padx=40,pady=10,sticky="nsew")

pressureIcon=load_icon("res/icons/barometer.png",size=containerIconSize)
pressure=ctk.CTkLabel(gridContainer,text="Pressure",font=t,image=pressureIcon,compound="bottom")
pressure.grid(row=2,column=1,padx=40,pady=10,sticky="nsew")


# building a bottom bar
bottom_bar=ctk.CTkFrame(app,width=180,height=40,fg_color="#e1e1e3",bg_color=white_code,corner_radius=30)
# bottom_bar.pack(side="bottom",pady=20)
bottom_bar.place(relx=0.5, rely=0.96, anchor="s")
bottom_bar.pack_propagate(False)

# placeholder
home_icon=load_icon("res/icons/home.png",size=(28,28))
home=ctk.CTkLabel(bottom_bar,text="",image=home_icon,font=f,cursor="hand2")
home.pack(side="left",pady=10,padx=20,expand=True)

search_icon=load_icon("res/icons/search.png",size=(28,28))
search=ctk.CTkLabel(bottom_bar,text="",image=search_icon, font=f,cursor="hand2")
search.pack(side="left",pady=10,padx=20,expand=True)


# building a hidden city input bar
city_entry=ctk.CTkEntry(app,placeholder_text="Input city name",width=220,corner_radius=20,bg_color="#e1e1e3",justify="center")
city_entry.place(x=70,y=40)
city_entry.place_forget()


def submit_city(event=None):
    city=city_entry.get()
    city_entry.place_forget()
    getWeather()
    city_entry.place_forget()


# click handler
def open_search(Event=None):
    city_entry.place(x=70,y=40)
    city_entry.focus_set()
    # Clear any previous text
    city_entry.delete(0, "end")
    # Move the cursor to the entry and give it keyboard focus
    city_entry.focus_force()
    # Ensure the insertion cursor is at the beginning
    city_entry.icursor(0)

city_entry.bind("<Return>",submit_city)
# weather refresh    
def refresh_weather(Event=None):
    print("Refreshing data")
    # call the weather function here

search.bind("<Button-1>",open_search)
home.bind("<Button-1>",refresh_weather)

app.mainloop()