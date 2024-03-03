from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    random_lokator1 = By.CSS_SELECTOR, '.btn-light .fa-magnifying-glass'
    random_lokator2 = By.CSS_SELECTOR, '.nav-tabs li:first-child'
    random_lokator3 = By.CSS_SELECTOR, '[href="#tab-review"]'
    random_lokator4 = By.CLASS_NAME, 'rating'
    PRICE = By.CSS_SELECTOR, '.price-new'
