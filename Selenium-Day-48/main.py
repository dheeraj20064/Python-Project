from selenium  import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/doc/")

# price_dollar=driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_cent=driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cent.text}.")

# search_bar=driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
# documentation_link=driver.find_element(By.CSS_SELECTOR, ".documentation-banner a")
# print(documentation_link.text)
element = driver.find_element(By.XPATH, '//*[@id="touchnav-wrapper"]/header/div/div[2]/div/p[2]')
print(element.text)




# driver.close()
#driver.quit()