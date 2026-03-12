import tkinter as tk
import customtkinter as ctk
from PIL import Image,ImageTk

# defining the application canvas
app=ctk.CTk()
app.geometry("360x640")
app.resizable(False,False)
app.title("Weather Watch")
app.iconbitmap("res/app_icon.ico")
ctk.set_appearance_mode("light")

# setting background to white
app.config(background="#F5F5F5")

#defining the fonts
f=("poppins",25,"bold")
t=("poppins",12,"bold")

# building first container and respective elements
container1=ctk.CTkFrame(app,fg_color="gray",bg_color="transparent")
container1.pack(pady=20,padx=10)

# city label
city_label=ctk.CTkLabel(container1,text="City Name",font=f)
city_label.pack(pady=10)

# current weather icon
currW=Image.open("res/storm.png")
currW_img=ImageTk.PhotoImage(currW)
currWeather=ctk.CTkLabel(container1,text="",image=currW_img)
currWeather.pack(pady=10)

# current temp
currTemp=ctk.CTkLabel(container1,text="Current Weather",font=f)
currTemp.pack(pady=10)

# current weather description
description=ctk.CTkLabel(container1,text="Description",font=f)
description.pack(pady=10)


# building second container for holding data
gridContainer=ctk.CTkFrame(app,fg_color="gray")
gridContainer.pack(pady=10)
gpy=10  #grid padding x-axis
gpx=10  #grid padding y-axis

min_temp=ctk.CTkLabel(gridContainer,text="Min Temp",font=t)
min_temp.grid(row=0,column=0,padx=40,pady=20)

max_temp=ctk.CTkLabel(gridContainer,text="Max Temp",font=t)
max_temp.grid(row=0,column=1,padx=40,pady=20)

humidity=ctk.CTkLabel(gridContainer,text="Humidity",font=t)
humidity.grid(row=1,column=0,padx=40,pady=20)

visibility=ctk.CTkLabel(gridContainer,text="Visibility",font=t)
visibility.grid(row=1,column=1,padx=40,pady=20)

wind_speed=ctk.CTkLabel(gridContainer,text="Wind Speed",font=t)
wind_speed.grid(row=2,column=0,padx=40,pady=20)

pressure=ctk.CTkLabel(gridContainer,text="Pressure",font=t)
pressure.grid(row=2,column=1,padx=40,pady=20)


# building a bottom bar
bottom_bar=ctk.CTkFrame(app,bg_color="transparent")
bottom_bar.pack(side="bottom",pady=20)

# placeholder
home=ctk.CTkLabel(bottom_bar,text="🏠",font=f,cursor="hand2")
home.pack(side="left",pady=10,padx=20)

search=ctk.CTkLabel(bottom_bar,text="🔍", font=f,cursor="hand2")
search.pack(side="left",pady=10,padx=20)


# building a hidden city input bar
city_entry=ctk.CTkEntry(app,placeholder_text="Input city name",width=220)
city_entry.place(x=70,y=40)
city_entry.place_forget()

# click handler
def open_search(Event=None):
    city_entry.place(x=70,y=40)
    city_entry.focus_set()

# weather refresh    
def refresh_weather(Event=None):
    print("Refreshing data")
    # call the weather function here

search.bind("<Button-1>",open_search)
home.bind("<Button-1>",refresh_weather)

app.mainloop()