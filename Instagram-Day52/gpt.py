from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

EMAIL = "lothobrockragnar@gmail.com"
PASSWORD = "Ragnarlothobrock@2025"
SIMILAR_ACCOUNT = "chefsteps"


class Instafollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        self.driver.find_element(By.NAME, "username").send_keys(EMAIL)
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button').click()

        # Wait for 'Not Now' after login
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Not now']"))
        ).click()

        # Handle notification popup
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']"))
            ).click()
        except:
            pass

    def find_followers(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
        ).send_keys(SIMILAR_ACCOUNT)

        # Click first profile
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '/{SIMILAR_ACCOUNT}/')]"))
        ).click()

        # Click followers link
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "followers"))
        ).click()

    def follow(self):
        scroll_popup = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[contains(@style,'overflow: auto')]"))
        )

        print("Scroll popup found.")

        last_height = self.driver.execute_script("return arguments[0].scrollHeight", scroll_popup)

        for i in range(10):  # Try scrolling 10 times
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_popup)
            time.sleep(2)

            new_height = self.driver.execute_script("return arguments[0].scrollHeight", scroll_popup)
            if new_height == last_height:
                break
            last_height = new_height

        print("Done scrolling.")

        # Click follow buttons
        follow_buttons = scroll_popup.find_elements(By.XPATH, ".//button[normalize-space()='Follow']")

        print(f"Found {len(follow_buttons)} follow buttons.")

        for btn in follow_buttons:
            try:
                self.driver.execute_script("arguments[0].click();", btn)
                time.sleep(1.5)
            except Exception as e:
                print(f"Error clicking follow: {e}")


Instagram = Instafollower()
Instagram.login()
Instagram.find_followers()
Instagram.follow()


