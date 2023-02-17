import requests
from datetime import datetime
import smtplib

my_email = "test.100.day@gmail.com"
app_password = "wukp pqxy imsi knzs"

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude
print(round(MY_LONG, 4))

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# print(iss_longitude)
# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunset)

time_now = datetime.now()
time_our = time_now.hour
print(time_our)
if iss_longitude == iss_longitude and time_our > sunset:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="onehandriddayofcode@yahoo.com",
                            msg=f"Subject:Hello\n\n.To look up.")

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
