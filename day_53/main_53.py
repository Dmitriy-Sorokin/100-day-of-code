from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


class Forms:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def onliner(self):
        self.driver.get(
            "https://r.onliner.by/ak/?price%5Bmin%5D=50&price%5Bmax%5D=320&currency=usd&rent_type%5B%5D=2_rooms&only_owner=true#bounds%5Blb%5D%5Blat%5D=53.909495557432045&bounds%5Blb%5D%5Blong%5D=27.5562858581543&bounds%5Brt%5D%5Blat%5D=53.933176030067045&bounds%5Brt%5D%5Blong%5D=27.597141265869144")
        time.sleep(2)
        ads = self.driver.find_elements(By.CSS_SELECTOR,
                                        "#search-filter-results > div.classifieds > div > div.classifieds-list a")
        link = [item.get_attribute("href") for item in ads]

        apart = [
            item.text.replace("\n", "").replace("2к", "").replace(" ", "").replace("$", " ").replace("р.", " ").split()
            for item in ads]

        return link, apart

    def forms_google(self):
        adr = Forms()
        links, adres = adr.onliner()
        leen_link = len(links)
        print(leen_link)
        self.driver.get(
            "https://docs.google.com/forms/d/e/1FAIpQLSdzuWkUyTZnazCeD0_mRJgFHOD52C0pC33HDpay0Up4DxSa3Q/viewform?usp=sf_link")

        for count in range(1):
            input_adres = self.driver.find_element(By.CSS_SELECTOR,
                                                   "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
            time.sleep(1)
            input_adres.clear()
            input_adres.send_keys(adres[count][2])
            inpit_cost = self.driver.find_element(By.CSS_SELECTOR,
                                                  "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
            inpit_cost.clear()
            inpit_cost.send_keys(f"Стоимость в доларах {adres[count][0]}$, в беларусских рублях {adres[count][1]} BYN")
            input_link = self.driver.find_element(By.CSS_SELECTOR,
                                                  "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.RpC4Ne.oJeWuf > div.Pc9Gce.Wic03c > textarea")
            input_link.clear()
            input_link.send_keys(links[count])
            btn_send = self.driver.find_element(By.CSS_SELECTOR,
                                                "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div > span > span")
            btn_send.click()
            time.sleep(1)
            click_again = self.driver.find_element(By.CSS_SELECTOR,
                                                   "body > div.Uc2NEf > div:nth-child(2) > div.RH5hzf.RLS9Fe > div > div.c2gzEf > a")
            click_again.click()


kw = Forms()
kw.forms_google()
