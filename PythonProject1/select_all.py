from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Your LinkedIn credentials
USERNAME = "lothobrockragnar@gmail.com"
PASSWORD="Ragnarlothobrock@2025"

# Job search query
JOB_QUERY = 'Python Developer'
LOCATION = 'India'

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

try:
    # Step 1: Login
    driver.get("https://www.linkedin.com/login")
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Step 2: Search for Jobs
    driver.get(f"https://www.linkedin.com/jobs/search/?keywords={JOB_QUERY}&location={LOCATION}")
    time.sleep(5)

    # Step 3: Get all job listings
    job_list_xpath = "//ul[@class='jobs-search__results-list']/li"
    job_cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, job_list_xpath)))
    print(f"🟢 Found {len(job_cards)} job listings.")

    # Step 4: Loop through job listings
    for i in range(len(job_cards)):
        try:
            job_cards = driver.find_elements(By.XPATH, job_list_xpath)
            job = job_cards[i]
            driver.execute_script("arguments[0].scrollIntoView();", job)
            job.click()
            time.sleep(2)

            try:
                # Step 5: Look for Easy Apply
                easy_apply_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Easy Apply')]")))
                easy_apply_button.click()
                time.sleep(2)

                # Close the popup form (you can automate further)
                print("✅ Easy Apply clicked. Closing popup for now.")
                driver.find_element(By.XPATH, "//button[@aria-label='Dismiss']").click()
            except:
                print("⚠️ No Easy Apply button.")

        except Exception as e:
            print(f"❌ Error at job {i}: {e}")

    print("🎉 Done processing all jobs.")

except Exception as e:
    print(f"🚨 Script failed: {e}")

finally:
    driver.quit()
