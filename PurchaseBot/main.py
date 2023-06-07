from browser import Browser
from walgreens import Walgreens

browser = Browser()
walgreens = Walgreens(browser)
browser.driver.get("https://www.walgreens.com/store/c/olay-total-effects-tone-correcting-cc-cream-with-spf-15,-light-to-medium/ID=prod6083321-product")
walgreens.add_product_to_cart()

input("")
