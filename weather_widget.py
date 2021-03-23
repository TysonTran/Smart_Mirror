from tkinter import *
import datetime
import requests
import json

api_key = "ed8a507e2be80d33b06e629f3e66b6eb"
city = "Escondido"
base_link = "http://api.openweathermap.org/data/2.5/weather?"
full_link = base_link + "q=" + city + "&appid=" + api_key
response = requests.get(full_link)

#Turns JSON format into Python format
x = response.json()

temps = x["main"]
current_temp = temps["temp"] #tells weather in Farenheit

weather = x["weather"][0]
forecast = weather["main"] #tells weather rain, cloud, or weather
forecast_desc = weather["description"]

lookup_weather = { #Link to image file
"Thunderstrom" : "Some link",
"Drizzle" : "Some link",
"Rain" : "Some link",
"Snow" : "Some link",
"Mist" : "Some link",
"Smoke" : "Some link",
"Haze" : "Some link",
"Dust:" : "Some link",
"Fog" : "Some link",
"Sand" : "Some link",
"Ash" : "Some link",
"Squall" : "Some link",
"Tornado" : "Some link",
"Clear" : "Some link",
"Clouds" : "Some link"
}