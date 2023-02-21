import requests
import datetime
# url = "http://api.open-notify.org/iss-now.json"
#
# respons = requests.get(url=url)
#
# respons.raise_for_status()
#
# data = respons.json()
# print(data)
# latitude = respons.json()["iss_position"]["latitude"]
# longitude = respons.json()["iss_position"]["longitude"]
#
# print(longitude, latitude)
parametrs = {
    "lat": 53.5359,
    "long": 27.3400,
    "formatted": 0
}

respons = requests.get("https://api.sunrise-sunset.org/json", params=parametrs)
respons.raise_for_status()
data = respons.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)


time_now = datetime.datetime.now()



print(time_now.hour)