import requests, json

def kelvin_farenheit(x):
	return round((x*(9/5)) - 459.67, 2)

api_key = "ed8a507e2be80d33b06e629f3e66b6eb"
city = "Escondido"
base_link = "http://api.openweathermap.org/data/2.5/weather?"
full_link = base_link + "q=" + city + "&appid=" + api_key
response = requests.get(full_link)

#Turns JSON format into Python format
x = response.json()

y = x["main"]
current_temp = y["temp"]
print(kelvin_farenheit(current_temp))