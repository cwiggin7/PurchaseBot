from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

class Browser:
    def __init__(self):
        self.driver = self._create_driver()

    def _create_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--incognito")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        return driver

    def navigate_to_page(self, url):
        self.driver.get(url)

    def add_input(self, by: By, value: str, text: str):
        field = self.driver.find_element(by, value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.driver.find_element(by, value)
        button.click()
        time.sleep(1)

    def locate_and_click_target_item(self, by, target_locator):
        try:
            target_item = self.driver.find_element(by, target_locator)
            target_item.click()
        except NoSuchElementException:
            print("Target item element not found.")