from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())

all_ancor_tags = soup.find_all(name="a")
print(all_ancor_tags)
for tag in all_ancor_tags:
    # print(tag.getText())
    print(tag.get("href"))


heading = soup.find(name="h1", id="name")
print(heading)

section_head = soup.find(name="h3", class_="heading")
print(section_head)

company_url = soup.select_one(selector="p a")
print(company_url)

search_id = soup.select_one(selector="#name")
print(search_id)

serach_class = soup.select_one(selector=".heading")
print(serach_class)