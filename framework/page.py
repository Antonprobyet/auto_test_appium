from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logging.basicConfig(filename='app_ajax_android.log',
                    filemode='a',
                    format='%(asctime)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
# Спроба написато логер. Невдала.

class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=8):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        logger.info(f"'{locator[1]}' is found.")
        return element

    def click_element(self, locator, timeout=6):
        element = self.find_element(locator, timeout)
        element.click()
        logger.info(f"'{locator[1]}' is clicked.")

    def enter_text(self, locator, text, timeout=6):
        element = self.find_element(locator, timeout)
        element.clear()
        logger.info(f"'{locator[1]}' is cleared.")
        element.send_keys(text)
        logger.info(f"'{locator[1]}' added test: '{text}'.")


