from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=8):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element

    def click_element(self, locator, timeout=4):
        element = self.find_element(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=4):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)


