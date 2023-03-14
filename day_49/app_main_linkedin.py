from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

url = "https://www.linkedin.com/home"
driver.get(url)

input_login = driver.find_element(By.CSS_SELECTOR, ".text-input>.text-md")
input_password = driver.find_element(By.CSS_SELECTOR, "#session_password")
btn_login = driver.find_element(By.CSS_SELECTOR, ".cursor-pointer")
"Alexander Levkin"

input_login.send_keys("write email")
input_password.send_keys("write password")
time.sleep(1)
btn_login.click()
time.sleep(1)
btn_message = driver.find_element(By.CSS_SELECTOR, "#global-nav > div > nav > ul > li:nth-child(2) > a")
btn_message.click()
time.sleep(1)
contacts = driver.find_element(By.CSS_SELECTOR, ".mn-community-summary__entity-info")
contacts.click()
time.sleep(1)
search = driver.find_element(By.CSS_SELECTOR, "#mn-connections-search-input")
search.send_keys("Alexander Levkin")
time.sleep(1)
send_message = driver.find_element(By.CSS_SELECTOR, ".entry-point .artdeco-button")
time.sleep(2)
send_message.click()
time.sleep(1)
msg_countener = driver.find_element(By.CSS_SELECTOR, ".msg-form__contenteditable")
msg_countener.send_keys("Привет это я питон бот шлю тебе сообщенгие!!! Ха ХА ХА! И пошли уже жрать!)")
time.sleep(1)
send_m = driver.find_element(By.CSS_SELECTOR, ".msg-form__footer .msg-form__right-actions .msg-form__send-button")
send_m.click()
