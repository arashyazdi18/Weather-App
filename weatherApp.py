# Arash Yazdidoost, 2020

# This program can be used to 
# lookup the weather in any
# city, leveraging the openWeatherMap API.
# Weather data is returned in JSON and printed to the user

# import necessary modules
import requests, json

#API details
api_key = "b788f6c4cdaf0dcf8d1343b0cafdc699"

base_url = "http://api.openweathermap.org/data/2.5/weather?q="

# Enter desired city name
city_name = input("Enter the city name: ")

# complete url based on user input
complete_url = base_url + city_name + "&appid=" + api_key 

# return the response
response = requests.get(complete_url)

# openWeatherMap returns JSON data
# We will convert the json format data into Python 
x = response.json()

# 404 means not found, otherwise found
if x["cod"] != "404":

    y = x["main"]

    #API returns in kelvin
    current_temp = int(round(y["temp"] - 273.15))

    current_pressure = y["pressure"]

    current_humidity = y["humidity"]

    z = x["weather"]

    weather_description = z[0]["description"]

    print(" Temperature = " + str(current_temp) + " Degrees Celsius")
    print(" Pressure: "+ str(current_pressure) + "hPa")
    print(" Humiditiy: " + str(current_humidity) + "%")
    print(" Conditions: " + str(weather_description))

else:
    print(" City Not Found ")