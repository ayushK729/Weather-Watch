# this is the first and most basic iteration of my weather application that outputs result in terminal


import time as tm
import requests as rq

with open("api_key.txt", "r") as f:
    api_key = f.read().strip()

url=api_key.replace("City_Name","Delhi")
# calling api to get data
try:
    json_data=rq.get(url).json()
except:
    print("Error Fetching Data")

# getting all data in variables
currTemp=json_data['list'][0]['main']['temp']
minTemp=json_data['list'][0]['main']['temp_min']
maxTemp=json_data['list'][0]['main']['temp_max']
humidity=json_data['list'][0]['main']['humidity']
desc=(json_data['list'][0]['weather'][0]['description']).title()
wind_speed=json_data['list'][0]['wind']['speed']
visibility=json_data['list'][0]['visibility']
pressure=json_data['list'][0]['main']['pressure']
print(currTemp,minTemp,maxTemp,humidity,desc,wind_speed,visibility,pressure)