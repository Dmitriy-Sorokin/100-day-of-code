from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

title_f = soup.find_all(name="h3", class_="title")
title_text = [text.getText() for text in title_f]
revers_list_title = list(reversed(title_text)) # try reverse [::-1]

with open("movies.txt", "w", encoding='utf-8') as file:
    for item in revers_list_title:
        file.write(f"{item}\n")