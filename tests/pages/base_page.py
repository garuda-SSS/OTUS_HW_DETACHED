from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    SUCCESS_ALERT = By.CSS_SELECTOR, '.alert-success'

    def __init__(self, browser):
        self.browser = browser

    def open(self, dop=''):
        self.browser.get(self.browser.base_url + dop)

    def unique_name(self):
        name = datetime.now().strftime("%H_%M_%S")
        unique_name = 'test'+str(name)
        return unique_name

    def get_element(self, locator, timeout=5):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((locator)))

    def wait_to_vanish(self, locator, timeout=5):
        return WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((locator)))

    def click_element(self, locator, timeout=5):
        self.get_element(locator, timeout).click()

    def js_click_element(self, locator, timeout=5):
        self.browser.execute_script("arguments[0].click();", self.get_element(locator, timeout))

    def correct_input(self, locator, timeout, text):
        element = self.get_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.get_element(locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(element).perform()
