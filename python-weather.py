#!/usr/bin/python

#Name : Harriet Kerubo

#Date : 08 / 06 / 2022

#Finding the weather of different cities

#import requests and json
import requests, json
#base URL
BASE_URL = "https://openweathermap.org/"
#City Name
City = input("Enter your city Name")
CITY = "Nairobi"
#API_KEY = "Your API key"
API_KEY = "baab46c0cc3e0d2c177b6f2c892cf93d"
#updating the URL
URL = BASE_URL + "q=" + CITY +"&appid=" + API_KEY
#HTP request
response = requests.get(URL)
#checking the status code of the request
if response.status_code == 200:
    #getting data in the json format
    data = response.json()
    #getting the main dict block
    main = data['main']
    #getting temperature
    temperature = main['temp']
    #getting humidity
    humidity = main['humidity']
    #getting the pressure
    pressure = main['pressure']
    #weather report
    report = data['weather']
    print(f"{CITY:-^30}")
    print(f"Temperature:{temperature}")
    print(f"Humidity:{humidity}")
    print(f"Pressure:{pressure}")
    print(f"Weather Report:{report[0]['description']}")
else:

    #showing the error message
    print("Error in the HTTP request")    
