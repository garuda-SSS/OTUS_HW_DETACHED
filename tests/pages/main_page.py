from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    random_lokator1 = By.CLASS_NAME, 'toast-container'
    random_lokator2 = By.NAME, 'description'
    OPEN_PRODUCT = By.CSS_SELECTOR, '.row-cols-md-3 .col.mb-3:first-of-type .image [href ^= "h"]'
    CURRENCY_LIST = By.CSS_SELECTOR, '#form-currency .fa-caret-down'
    ADD_TO_BASKET_BTN = By.CSS_SELECTOR, '.row-cols-1 .mb-3:first-child form [type="submit"]:first-child'
    EURO = By.CSS_SELECTOR, '[href="EUR"]'
    POUND_STERLIND = By.CSS_SELECTOR, '[href="GBP"]'
    US_DOLLAR = By.CSS_SELECTOR, '[href="USD"]'
    PRICE = By.CSS_SELECTOR, '.row-cols-md-3 .mb-3:first-of-type .price-new'

    def add_product_to_basket(self, locator, timeout=5):
        self.js_click_element(locator, timeout)
        assert self.get_element(BasePage.SUCCESS_ALERT), "Товар не добавлен"

    def change_currency(self, currency, price_locator):
        self.click_element(MainPage.CURRENCY_LIST)
        if currency == 'euro':
            self.js_click_element(MainPage.EURO)
            assert '€' in self.get_element(price_locator).text, "Цены не изменились"
        elif currency == 'pound':
            self.js_click_element(MainPage.POUND_STERLIND)
            assert '£' in self.get_element(price_locator).text, "Цены не изменились"
        elif currency == 'dollar':
            self.js_click_element(MainPage.US_DOLLAR)
            assert '$' in self.get_element(price_locator).text, "Цены не изменились"
        else:
            raise ValueError("Данной валюты не предусмотрено")
