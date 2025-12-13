from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import smtplib
load_dotenv()

GMAIL_USERNAME = os.environ.get("GMAIL_USERNAME")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")
SMTP_ADDRESS = "smtp.gmail.com"
from_address = os.environ.get("FROM_ADDRESS")
to_address = os.environ.get("TO_ADDRESS")

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}

#url = "https://appbrewery.github.io/instant_pot/"

url="https://www.amazon.de/-/en/Containers-Programmes-Smoothie-Milkshakes-NC300EUCP/dp/B0CXXX6Z2H?pd_rd_w=6etPq&content-id=amzn1.sym.1f4ab70d-e4c2-4163-adb8-f439441a894e&pf_rd_p=1f4ab70d-e4c2-4163-adb8-f439441a894e&pf_rd_r=GR5PH87110TKR9S1EAYN&pd_rd_wg=hkqoa&pd_rd_r=f42d1149-4b95-4b24-9cf6-296780e090b9&pd_rd_i=B0CXXX6Z2H&ref_=oct_dx_dotd_B0CXXX6Z2H"
data = requests.get(headers=headers, url=url).text
soup = BeautifulSoup(data, "html.parser")

# price = soup.find(name="div", class_="a-section a-spacing-none aok-align-center aok-relative").getText().strip().split(" ")[0]
price = soup.find(name="span", class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay").getText().strip().split(" ")[0]

sanitize_price = float(price.replace('CZK', '').replace(",", ''))
target_price = 4000


message = f"The item you're tracking hit your target price {target_price}! It's {sanitize_price} now! Go get it!"

if sanitize_price <= target_price:
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=GMAIL_USERNAME, password=GMAIL_APP_PASSWORD)
        connection.sendmail(from_addr=from_address, to_addrs=to_address, msg=message)





