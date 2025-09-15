from selenium  import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
timings=[]
time= driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
for element in time:
    timings.append(element.text)

events=[]
event=driver.find_elements(By.XPATH,'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
for element in event:
    events.append(element.text)

result = {
    i: {'time': t, 'event': e}
    for i, (t, e) in enumerate(zip(timings, events))
}

print(result)
