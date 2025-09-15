from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

EMAIL="lothobrockragnar@gmail.com"
PASSWORD="Ragnarlothobrock@2025"
SIMILAR_ACCOUNT="chefsteps"

class Instafollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        name=self.driver.find_element(By.NAME,"username")
        name.send_keys(EMAIL)
        password=self.driver.find_element(By.NAME,"password")
        password.send_keys(PASSWORD)
        login=self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button')
        login.click()
        time.sleep(15)
        not_now=self.driver.find_element(By.XPATH, "//div[@role='button' and text()='Not now']")
        not_now.click()

    def find_followers(self):
        time.sleep(10)
        search=self.driver.find_element(By.XPATH, "//input[@aria-label='Search input']")
        search.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)
        search.send_keys(Keys.ARROW_DOWN)
        search.send_keys(Keys.ENTER)

    def folow(self):
        pass

Instagram=Instafollower()
Instagram.login()
Instagram.find_followers()
Instagram.folow()
