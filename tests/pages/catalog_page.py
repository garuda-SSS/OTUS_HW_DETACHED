from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CatalogPage(BasePage):
    random_lokator1 = By.ID, 'compare-total'
    random_lokator2 = By.ID, 'content'
    random_lokator3 = By.CSS_SELECTOR, '.row #header-cart'
    random_lokator4 = By.CSS_SELECTOR, '.col .row:first-of-type'
    random_lokator5 = By.CSS_SELECTOR, '.offset-lg-1 .input-group-text'
