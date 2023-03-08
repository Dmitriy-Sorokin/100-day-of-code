from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"

response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

article_tag = soup.find(name="td span a")
print(article_tag)
point = soup.select_one(selector="#score_35053402")
# print(point)

p = soup.find_all(name="span", class_="score")
print(p)

score = [int(number.getText().split()[0]) for number in p]
print(max(score))
# text_h = article_tag[8].getText()
# print(text_h)
# article_link =

# a = soup.find_all(name="a")
# print(a)