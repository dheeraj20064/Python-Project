import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/dp/B098F5PJRV"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

price_element=soup.find("span",class_="a-price-whole")

if price_element:
    price_text=price_element.get_text().replace(",","").strip()
    price=float(price_text)
    print("Price:",price)

    TARGET=4400

    if price<TARGET:
        my_email="dheerajkrishna29@gmail.com"
        password="esqoukbpoxvnzpht"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="angithchandran@gmail.com",  # Receiver's email
                msg=f"Subject:Amazon Price Drop!\n\nThe price is now RS{price}.\nCheck the product here:\n{URL}"
            )
            print("📧 Email sent! Price dropped.")
    else:
        print("ℹ️ Price is still higher than your target.")
else:
    print("❌ Price not found. Check the class name or HTML structure.")









