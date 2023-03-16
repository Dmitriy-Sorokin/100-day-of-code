from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


promised_up = 20
promised_down = 5


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
#
# url = "https://www.linkedin.com/home"
# driver.get(url)


class InternetSpeedTwitterBot:
    def __init__(self, current_url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(current_url)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        button_start = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        button_start.click()
        time.sleep(60)
        down_elem = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        up_elem = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
        print(f"down: {down_elem}")
        print(f"up: {up_elem}")

    def tweet_at_provider(self):
        pass


get_int_speed = InternetSpeedTwitterBot("https://www.speedtest.net/ru")
get_int_speed.get_internet_speed()
