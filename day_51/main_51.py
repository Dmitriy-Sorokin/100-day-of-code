from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


promised_up = 20
promised_down = 5
LOGIN = "sorokin.dm@nakukop.com"
PASS = "Dimon21234qwer"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/ru")
        button_start = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        button_start.click()
        time.sleep(60)
        down_elem = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        up_elem = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
        self.up = up_elem
        self.down = down_elem
        print(f"down: {down_elem}")
        print(f"up: {up_elem}")
        print(self.up, "dpeeed")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/?lang=ru")
        frames = self.driver.find_elements(By.CSS_SELECTOR, "iframe")
        self.driver.switch_to.frame(frames[0])
        button_login = self.driver.find_element(By.CSS_SELECTOR, "#container > div > div.nsm7Bb-HzV7m-LgbsSe-bN97Pc-sM5MNb.oXtfBe-l4eHX")
        time.sleep(2)
        button_login.click()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        time.sleep(3)
        input_email = self.driver.find_element(By.CSS_SELECTOR, "#identifierId")
        input_email.send_keys(LOGIN)
        btn_next = self.driver.find_element(By.CSS_SELECTOR, "#identifierNext > div > button")
        btn_next.click()
        time.sleep(1)
        input_pass = self.driver.find_element(By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
        input_pass.send_keys(PASS)
        button_next = self.driver.find_element(By.CSS_SELECTOR, "#passwordNext > div > button")
        button_next.click()
        time.sleep(10)
        self.driver.switch_to.window(handles[0])
        input_text = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div")
        input_text.send_keys(f"Speed my internet: speed down = {self.down}, speed up = {self.up}")
        btn_tweet = self.driver.find_element(By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-184en5c > div > div.css-1dbjc4n.r-kemksi.r-oyd9sg > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(3) > div > div > div:nth-child(2) > div")
        btn_tweet.click()
        time.sleep(5)




tw = InternetSpeedTwitterBot()
tw.get_internet_speed()
tw.tweet_at_provider()
