from browser import Browser
from walgreens import Walgreens
from amazon import Amazon
import time
from twilio.rest import Client
import keys

client = Client(keys.account_sid, keys.auth_token)

browser = Browser()
walgreens = Walgreens(browser)

while(1):
  if(walgreens.is_product_in_stock('https://www.walgreens.com/store/c/black-girl-sunscreen-spf-30/ID=300425138-product')):
    for number in keys.target_numbers:
      message = client.messages.create(
        body="Black Girl Sunscreen INSTOCK !",
        from_=keys.twilio_number,
        to=number
      )
      print(message.body)

    break
  else:
    print("Product out of stock")
    time.sleep(60)


input("")
