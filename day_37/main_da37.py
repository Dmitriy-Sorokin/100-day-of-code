import requests
from datetime import datetime as dt

USERNAME = "bashkavit"
TOKEN = "1aasdf3rfsfs3sdg4424"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_param = {
    "id": "graph2",
    "name": "100 Day of code",
    "unit": "time",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# resp_graph = requests.post(url=graph_endpoint, json=graph_param, headers=headers)
# print(resp_graph.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2"

today = dt(year=2023, month=2, day=20)

px_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7"
}

# resp_px = requests.post(url=pixel_endpoint, json=px_params, headers=headers)
# print(resp_px.text)

put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2/20230220"

params_update = {
    "quantity": "90"
}

# response_update = requests.put(url=put_endpoint, json=params_update, headers=headers)
# print(response_update.text)

del_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2/20230202"

resp_del = requests.delete(url=del_endpoint, headers=headers)
print(resp_del.text)
