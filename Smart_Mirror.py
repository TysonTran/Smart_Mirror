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

y = x["main"]
current_temp = y["temp"]
print(kelvin_to_farenheit(current_temp))

class Weather(Frame):
	def __init__(self, parent): #Parent is where frame widget is created
		super().__init__(self, parent, bg = 'black') #Uses init from Frame
		self.temp = ''


	
	def kelvin_to_farenheit(k):
	return round((k*(9/5)) - 459.67, 2)