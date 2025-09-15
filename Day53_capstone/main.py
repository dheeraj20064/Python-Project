import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup

# EMAIL="dheerajkrishna29@gmail.com"

User_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
language="en-US,en;q=0.9"

header={"User-Agent":User_agent,"Accept-Language":language}
response = requests.get("https://appbrewery.github.io/Zillow-Clone/",headers=header)
soup = BeautifulSoup(response.content,"html.parser")
houses=soup.select(".PropertyCardWrapper__StyledPriceLine")
# house_list=[house.get_text().replace("/","").replace("+","").replace("mo","").replace("1 bd","").replace("1bd","").strip() for house in houses]
# print(house_list)

house_rate=[]
for house in houses:
    rate=house.get_text().strip()
    rated=rate.replace("/"," ").replace("+", " ")
    price=rated.split(" ")[0]
    house_rate.append(price)
print(house_rate)

links_id=soup.select(".StyledPropertyCardPhotoBody")

# Extract all <a> tags inside
houser_link=[]
for link in links_id:
    a_tag=link.find("a")
    if a_tag and "href" in a_tag.attrs:
        houser_link.append(a_tag.attrs["href"])
print(houser_link)

address = [addr.get_text(strip=True).replace("|","") for addr in soup.find_all("address", attrs={"data-test": "property-card-addr"})]
print(address)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdV8kwycZuCdWu9tieb62dU6ZaguAnsjqEinou10WLRmzy7YA/viewform")
wait = WebDriverWait(driver, 10)



for i in range(0,2):


    address_fill=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    address_fill.send_keys(address[i])

    price_fill=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_fill.send_keys(house_rate[i])

    link_fill=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_fill.send_keys(houser_link[i])

    button=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    button.click()

    time.sleep(2)
    another=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    another.click()

    wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))

# driver.get("https://docs.google.com/forms/")
# email=driver.find_element(By.NAME,"identifier")
# email.send_keys("EMAIL")

# spreadsheet=driver.find_element(By.XPATH,'//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div')
# spreadsheet.click()