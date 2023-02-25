import requests

first_name = input("Write first name: ")
last_name = input("Write last name: ")
email = input("Write email: ")
email1 = input("Write email again: ")

url = "https://api.sheety.co/18ae19b46e0eb8883332528cd03f2bf1/flightDeals/newUser"

body = {
    "newUser": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}

put_resp = requests.put(url=f"{url}/2", json=body)

response = requests.get(url)
print(response.text)
