from selenium.webdriver.common.by import By
import pytest

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

url = "https://www.amazon.com/HP-27h-Full-Monitor-Built/dp/B0B6CYVXF7/ref=sr_1_2?keywords=" \
      "monitor&qid=1678545096&refinements=p_n_feature_fifteen_browse-bin%3A17751807011%2Cp" \
      "_n_feature_twenty_browse-bin%3A72511692011&rnid=72511690011&s=pc&sprefix=mon%2Caps%2C329&sr=1-2"

url_p = "https://www.python.org/"

driver.get(url_p)

# price = driver.find_element(By.CSS_SELECTOR, "#model_name_0_price > p").text
# print(f"{price} asfasfasfsaf")

search = driver.find_element(By.NAME, "q")
print(search.get_attribute("placeholder"))

# driver.close()  # Закрывает вкладку

# driver.quit()  # Закрывает браузер
