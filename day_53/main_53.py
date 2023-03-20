from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


class Forms:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def forms_google(self):
        url = "https://docs.google.com/forms/d/e/1FAIpQLSdzuWkUyTZnazCeD0_mRJgFHOD52C0pC33HDpay0Up4DxSa3Q/viewform?usp=sf_link"
        pass

    def onliner(self):
        self.driver.get(
            "https://r.onliner.by/ak/?price%5Bmin%5D=50&price%5Bmax%5D=320&currency=usd&rent_type%5B%5D=2_rooms&only_owner=true#bounds%5Blb%5D%5Blat%5D=53.909495557432045&bounds%5Blb%5D%5Blong%5D=27.5562858581543&bounds%5Brt%5D%5Blat%5D=53.933176030067045&bounds%5Brt%5D%5Blong%5D=27.597141265869144")
        ads = self.driver.find_elements(By.CSS_SELECTOR,
                                        "#search-filter-results > div.classifieds > div > div.classifieds-list a")
        link = [item.get_attribute("href") for item in ads]
        print(link)

        apart = [kw.text.replace("\n", "").replace("2к", "").replace(" ", "").replace("$", " ").replace("р.", " ").split() for kw in ads]
        print(apart)



kw = Forms()
kw.onliner()
