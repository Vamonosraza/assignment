import requests
import json

url = "http://api.weatherapi.com/v1/history.json?key=f2b3d8b7c90c47e086d193033251501&q=Fairbanks&dt=2024-12-12&end_dt=2025-01-15&hour=12"

url2 = "http://api.weatherapi.com/v1/history.json?key=f2b3d8b7c90c47e086d193033251501&q=Fairbanks&dt=2024-11-10&end_dt=2025-12-11&hour=12"

response = requests.get(url)
response2 = requests.get(url2)

if response.status_code == 200:
    print("Success!")
    data = response.json()
    data2 = response2.json()

    combined_data = {
        "location": data["location"],
        "forecast":{
           'forecast': data['forecast']['forecastday'] + data2['forecast']['forecastday']
        }
    }

    # Save the JSON data to a file
    with open("AlaskaWeather.json", "w") as json_file:
        json.dump(combined_data, json_file)
    print("Data saved to AlaskaWeather.json")
else:
    print(f"Failed to retrieve data: {response.status_code}")
    print(response.json())