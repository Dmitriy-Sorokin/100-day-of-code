import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "test.100.day@gmail.com"
app_password = "wukp pqxy imsi knzs"


url = "https://www.amazon.com/HP-27h-Full-Monitor-Built/dp/B0B6CYVXF7/ref=sr_1_2?keywords=" \
      "monitor&qid=1678545096&refinements=p_n_feature_fifteen_browse-bin%3A17751807011%2Cp" \
      "_n_feature_twenty_browse-bin%3A72511692011&rnid=72511690011&s=pc&sprefix=mon%2Caps%2C329&sr=1-2"

param = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url=url, headers=param)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
price = soup.find(name="span", class_="a-offscreen")
num = price.getText()
final_price = num.replace("$", "")
int_price =  float(final_price)


if int_price <= 220:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="onehandriddayofcode@yahoo.com",
                            msg=f"Subject:Hello!!!! "
                                f"this is project 100 day of code\n\n "
                                f"Discounts on monitors today!!! Your monitor costs {final_price}.")