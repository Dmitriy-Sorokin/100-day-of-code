import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

url = "https://opentdb.com/api.php"

current_url = requests.get(url=url, params=parameters)
current_url.raise_for_status()
json_data = current_url.json()
question_data = json_data["results"]

