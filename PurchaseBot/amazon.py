from browser import Browser
from selenium.webdriver.common.by import By

class Amazon:
    def __init__(self, browser: Browser):
        self.browser = browser
        pass
    
    def add_product_to_cart(self):
      input_element = self.browser.driver.find_element(By.CSS_SELECTOR, 'input[aria-label^="Add to Cart from seller Amazon.com"]')
      