from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

cooc = driver.find_element(By.CSS_SELECTOR, "#money").text
cost = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text
rep = cost.split()

print(cooc)

counter = 0
go_game = True
while go_game:
    counter += 1
    cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
    cookie.click()
    grandma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma")
    grandma.click()
    if counter > 10000:
        go_game = False

