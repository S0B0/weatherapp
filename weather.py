import requests

API_KEY = " "
BASE_URL = " "

city = input("Please input a city name: \n>:")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print(" Today's weather: ", weather,"\n  Average Temperature: ",temperature," celsius")
else:
    print("Error occured please try again later!")