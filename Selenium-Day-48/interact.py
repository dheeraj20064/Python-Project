from selenium  import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article=driver.find_element(By.LINK_TEXT,'Content portals')
#article.click()
Q=article.find_element(By.XPATH,'//*[@id="p-search"]/a/span[1]')
Q.click()
search=driver.find_element(By.NAME,'search')
search.send_keys("Python", Keys.ENTER)
