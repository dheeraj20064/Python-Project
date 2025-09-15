from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

fname=driver.find_element(By.NAME,'fName')
fname.send_keys("DKT", Keys.ENTER)
lname=driver.find_element(By.NAME,'lName')
lname.send_keys("Dheeru", Keys.ENTER)
email=driver.find_element(By.NAME,'email')
email.send_keys("guegfeuyfg@gmail.com", Keys.ENTER)
button=driver.find_element(By.XPATH,'/html/body/form/button')
button.click()

