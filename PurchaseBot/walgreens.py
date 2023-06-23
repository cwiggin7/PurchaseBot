from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from browser import Browser
import random
import time

class Walgreens:
    def __init__(self, browser: Browser):
        self.browser = browser

    def login(self, username: str, password: str):
        is_logged_in = self.is_user_logged_in()

        if not is_logged_in:
            self.browser.navigate_to_page("https://www.walgreens.com/login.jsp")
            self.browser.add_input(By.ID, "user_name", username)
            self.browser.add_input(By.ID, "user_password", password)
            self.browser.click_button(By.ID, "submit_btn")

            verification_url = "https://www.walgreens.com/profile/verify_identity"
            wait = WebDriverWait(self.browser.driver, 10)
            wait.until(EC.url_changes(verification_url))

            if not self.browser.driver.current_url.startswith(verification_url):
                print("User is logged in.")
            else:
                print("Please complete the verification manually.")
        else:
            print("User is already logged in.")

    def is_user_logged_in(self):
        self.browser.navigate_to_page("https://www.walgreens.com/youraccount/default.jsp")
        return not self.browser.driver.current_url.startswith("https://www.walgreens.com/login")

    def check_product_stock_status(self):
        try:
            status_element = WebDriverWait(self.browser.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ".//span/p[text()='Out of stock']"))
            )
            return False  # Product is out of stock
        except TimeoutException:
            return True  # Product is in stock

    def is_product_in_stock(self, product_page):
        self.browser.navigate_to_page(product_page)

        target_item_xpath = "//ul[@class='fulfillment__container']//li[contains(@class, 'drawer')][3]"
        self.browser.locate_and_click_target_item(By.XPATH, target_item_xpath)

        return self.check_product_stock_status()

    def clip_coupons(self):
        coupon_divs = self.browser.driver.find_elements(By.XPATH, "//div[starts-with(@class, 'couponListCount-')]")
        for div in coupon_divs:
            div.click()

    def add_product_to_cart(self, quantity=12):
        target_item_xpath = "//ul[@class='fulfillment__container']//li[contains(@class, 'drawer')][3]"
        self.browser.locate_and_click_target_item(By.XPATH, target_item_xpath)

        # Wait for the select_element to be present
        try:
            select_element = WebDriverWait(self.browser.driver, 10).until(
                EC.presence_of_element_located((By.ID, "select-dropdown"))
            )
        except NoSuchElementException:
            print("Select element not found.")
            return

        select = Select(select_element)
        select.select_by_value(str(quantity))

        # Click the "Add for shipping" button
        add_to_cart_button = self.browser.driver.find_element(By.ID, "receiveing-addToCartbtn")
        add_to_cart_button.click()
        