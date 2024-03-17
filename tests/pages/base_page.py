from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
import logging


class BasePage:
    SUCCESS_ALERT = By.CSS_SELECTOR, '.alert-success'

    def __init__(self, browser):
        self.browser = browser
        self._config_logger()

    def _config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(f"logs/{self.browser.test_name}.log"))
        self.logger.setLevel(level=self.browser.log_level)

    def open(self, dop=''):
        self.browser.get(self.browser.base_url + dop)
        self.logger.info(f"Opened link: {self.browser.base_url + dop}")

    def unique_name(self):
        name = datetime.now().strftime("%H_%M_%S")
        unique_name = 'test'+str(name)
        return unique_name

    def get_element(self, locator, timeout=5):
        self.logger.info(f"Found element: {locator}")
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((locator)))

    def wait_to_vanish(self, locator, timeout=5):
        return WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((locator)))

    def click_element(self, locator, timeout=5):
        self.get_element(locator, timeout).click()
        self.logger.info(f"Clicked element: {locator}")

    def js_click_element(self, locator, timeout=5):
        self.browser.execute_script("arguments[0].click();", self.get_element(locator, timeout))
        self.logger.info(f"Clicked element: {locator} with javascript")

    def correct_input(self, locator, timeout, text):
        element = self.get_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        self.logger.info(f"Sent '{text}' in element:{locator}")

    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()
        self.logger.info(f"Scrolled to element: {locator}")
