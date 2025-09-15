from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_DOWN = 150  # in Mbps
PROMISED_UP = 10     # in Mbps
TWITTER_EMAIL = "lothobrockragnar@gmail.com"
TWITTER_PASSWORD = "Ragnarlothobrock@2025"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        # Wait for test to complete (~45 sec)
        time.sleep(45)

        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)

        print(f"Download Speed: {self.down} Mbps")
        print(f"Upload Speed: {self.up} Mbps")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        wait = WebDriverWait(self.driver, 30)

        # Login Step 1: Enter email
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(3)

        # Optional: Twitter sometimes asks for username again
        try:
            username_input = self.driver.find_element(By.NAME, "text")
            username_input.send_keys(TWITTER_EMAIL)
            username_input.send_keys(Keys.ENTER)
            time.sleep(3)
        except:
            pass

        # Login Step 2: Enter password
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        # Tweet message
        tweet_message = f"Hey Internet provider, why is my speed {self.down} Mbps down / {self.up} Mbps up when I pay for {PROMISED_DOWN} down / {PROMISED_UP} up?"

        # Compose Tweet
        tweet_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="tweetTextarea_0"]')))
        tweet_box.send_keys(tweet_message)

        # Click tweet
        tweet_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButtonInline"]')))
        tweet_button.click()

        print("✅ Tweet sent successfully!")

        time.sleep(5)
        self.driver.quit()

# RUN
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
