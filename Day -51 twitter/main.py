from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN=150
PROMISED_UP=10
TWITTER_PASSWORD="Ragnarlothobrock@2025"
TWITTER_EMAIL="lothobrockragnar@gmail.com"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.down=0
        self.up=0
        self.driver=webdriver.Chrome()


    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        continue_button=self.driver.find_element(By.ID,"onetrust-accept-btn-handler")
        continue_button.click()
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print("Download Speed:",self.down)
        print("Upload Speed:",self.up)
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/signup")
        time.sleep(15000)
        error_button=self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/button/div')
        error_button.click()
        time.sleep(5)


        message = f"Hey, Internet provider why is my internet speed {self.down} down / {self.up} up even though I paid for {PROMISED_DOWN} down and {PROMISED_UP} up"

        message_box=self.driver.find_element(By.CSS_SELECTOR,"DraftEditor-root")
        message_box.send_keys(message)


bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
