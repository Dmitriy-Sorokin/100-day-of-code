import requests

url_female = "https://api.genderize.io?name=dima"
url_years = "https://api.agify.io?name=dima"

fm = requests.get(url_female).json()
ye = requests.get(url_years).json()


url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url)
all_posts = response.json()

print(all_posts[0]["title"])