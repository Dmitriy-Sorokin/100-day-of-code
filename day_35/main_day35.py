import requests
import smtplib

my_email = "test.100.day@gmail.com"
app_password = "wukp pqxy imsi knzs"


api_key = "349a35d3f3c95904257d35da7e26381d"
latitude = 53.5359
longitude = 27.3400
url = "https://api.openweathermap.org/data/2.5/onecall"

parameter = {
    "lat": latitude,
    "lon": longitude,
    "exclude": "current,minutely,daily,alerts",
    "appid": api_key
}

respons = requests.get(url, parameter)
respons.raise_for_status()
weather_data = respons.json()

will_rain = False

hourly = [weather_data["hourly"][num]["weather"][0]["id"] for num in range(0, 12)]
for id_w in hourly:
    if int(id_w) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="onehandriddayofcode@yahoo.com",
                            msg=f"Subject:Hello\n\n.Umbrella.")
