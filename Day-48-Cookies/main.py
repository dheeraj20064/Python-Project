from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)

try:
    driver.find_element(By.ID, "langSelect-EN").click()
except:
    pass

time.sleep(5)
cookie = driver.find_elements(By.ID,"bigCookie")

store_items=driver.find_elements(By.CSS_SELECTOR,"#store div")
items_id=[item.get_attribute("id") for item in store_items if item.get_attribute("id")
          and item.get_attribute("id").startswith("product")]

timeout=time.time()+5
five_min=time.time()+5*60

while True:
    cookie.click()
    if time.time()>timeout:
        money_element=driver.find_elements(By.ID,"cookies")
        money=money_element.text.split(" ")[0]

        try:
            price=int(money.replace(",",""))
        except ValueError:
            price=0

        all_prices=driver.find_elements(By.CSS_SELECTOR,"#store b")
        prices=[]
        for item in all_prices:
            text=item.text
            if '-' in text:
                cost=int(text.split("-")[1].strip().replace(",",""))
                prices.append(cost)
        upgrades={}
        for i in range(min(len(prices),len(items_id))):
            upgrades[prices[i]]=items_id[i]

        affordable_upgrade={
            cost:id_ for cost, id_ in upgrades.items() if money>=cost
        }

        if affordable_upgrade:
            best_upgrade_id=affordable_upgrade[max(affordable_upgrade)]
            driver.find_element(By.ID, best_upgrade_id).click()
            print(f"Purchased: {best_upgrade_id} for {max(affordable_upgrade)} cookies")

    if time.time()>five_min:
        cps=driver.find_elements(By.ID,"cookiesPerSecond")
        print(f"{cps}")
        break
