from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_MAIL="lothobrockragnar@gmail.com"
PASSWORD="Ragnarlothobrock@2025"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4258138447&distance=25&geoId=102257491&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")

time.sleep(5)

try:
    sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
    driver.execute_script("arguments[0].click();", sign_in_button)
    print("Clicked 'Sign in' button successfully.")
except Exception as e:
    print("Failed to click 'Sign in':", e)
email=driver.find_element(By.ID,'username')
email.send_keys(ACCOUNT_MAIL, Keys.ENTER)
passwword=driver.find_element(By.ID,'password')
passwword.send_keys(PASSWORD, Keys.ENTER)
try:
    sign_button = driver.find_element(By.LINK_TEXT, "Sign in")
    driver.execute_script("arguments[0].click();", sign_button)
    print("Clicked 'Sign in' button successfully.")
except Exception as e:
    print("Failed to click 'Sign in':", e)
driver.find_element(By.XPATH,'//*[@id="jobs-apply-button-id"]/span').click()
number=driver.find_element(By.ID,"single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4258138447-14190701169-phoneNumber-nationalNumber")
number.send_keys("8921089288", Keys.ENTER)
driver.find_element(By.XPATH, "//button//span[text()='Next']").click()

RESUME_PATH = "C:\\Users\\HP\\Downloads\\simple_resume.pdf"
# change to your actual file path

file_input = driver.find_element(
    By.ID,
    "jobs-document-upload-file-input-upload-resume-urn:li:fsu_jobApplicationFileUploadFormElement:urn:li:jobs_applyformcommon_easyApplyFormElement:(4258138447,14190701161,document)"
)
time.sleep(3)
file_input.send_keys(RESUME_PATH)
driver.find_element(By.XPATH, "//button//span[text()='Review']").click()
wait = WebDriverWait(driver, 10)

submit_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button//span[text()='Submit application']"))
)
submit_btn.click()



