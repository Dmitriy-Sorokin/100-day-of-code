from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

url_p = "https://www.python.org/"
driver.get(url_p)

event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_text = [ev.text for ev in event_time]
print(event_text)

text = driver.find_elements(By.XPATH, "//*[@id='content']/div/section/div[2]/div[2]/div/ul/li/a")

get_text = [text1.text for text1 in text]

dict_word = dict(zip(event_text, get_text))
print(dict_word)

events = {}

for n in range(len(event_time)):
    events[n] = {
        "time": event_time[n].text,
        "name": text[n].text,
    }
print(events)
