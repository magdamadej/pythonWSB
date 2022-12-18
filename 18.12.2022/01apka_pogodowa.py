#python -m pip install requests
import requests

api_link = 'https://api.openweathermap.org/data/2.5/weather?q='
api_key = '&appid=7dc1e3959907f252891451585f715299'
api_units = '&units=metric'
api_lang = '&lang=pl'
api_city = input("Podaj nazwę miasta: ").lower().strip()

URL = api_link + api_city + api_key + api_units + api_lang

respone_dict = requests.get(URL).json()
#print(respone_dict)

print(f"{respone_dict['name']}, {respone_dict['sys']['country']}")
print(f"Temperatura: {round(respone_dict['main']['temp'])} °C")
print(f"Temperatura odczuwalna: {round(respone_dict['main']['feels_like'])} °C")
print(f"Temperatura maksymalna: {round(respone_dict['main']['temp_max'])} °C")
print(f"Temperatura minimalna: {round(respone_dict['main']['temp_min'])} °C")
print(f"Opis pogody: {respone_dict['weather'][0]['description']}")
print(f"Wilgotność: {respone_dict['main']['humidity']} %")
print(f"Ciśnienie: {respone_dict['main']['pressure']} hPa")
print(f"Prędość wiatru: {(respone_dict['wind']['speed']) * 3.6} km/h")

