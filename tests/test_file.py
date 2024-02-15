import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_part_two():
    @pytest.mark.parametrize('selector, value', [(By.CLASS_NAME, 'toast-container'),
                                                 (By.NAME, 'description'),
                                                 (By.ID, 'alert'),
                                                 (By.CSS_SELECTOR, '.nav.float-start'),
                                                 (By.CSS_SELECTOR, '.container .float-start .list-inline li form')])
    def test_main_page(self, browser, selector, value):
        browser.get(browser.base_url)
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((selector, value))
        )

    @pytest.mark.parametrize('selector, value', [(By.ID, 'compare-total'),
                                                 (By.ID, 'content'),
                                                 (By.CSS_SELECTOR, '.row #header-cart'),
                                                 (By.CSS_SELECTOR, '.col .row:first-of-type'),
                                                 (By.CSS_SELECTOR, '.offset-lg-1 .input-group-text')])
    def test_catalog_page(self, browser, selector, value):
        browser.get(browser.base_url + '/en-gb/catalog/laptop-notebook')
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((selector, value))
        )

    @pytest.mark.parametrize('selector, value', [(By.CSS_SELECTOR, '.btn-light .fa-magnifying-glass'),
                                                 (By.CSS_SELECTOR, '.nav-tabs li:first-child'),
                                                 (By.CSS_SELECTOR, '[href="#tab-review"]'),
                                                 (By.CLASS_NAME, 'rating'),
                                                 (By.CSS_SELECTOR, '.btn-primary#button-cart')])
    def test_product_page(self, browser, selector, value):
        browser.get(browser.base_url + '/en-gb/product/laptop-notebook/hp-lp3065')
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((selector, value))
        )

    @pytest.mark.parametrize('selector, value', [(By.ID, 'footer'),
                                                 (By.CLASS_NAME, 'btn-primary'),
                                                 (By.CSS_SELECTOR, '.card-header .fa-lock'),
                                                 (By.CSS_SELECTOR, '[name="password"]'),
                                                 (By.CSS_SELECTOR, '[name="username"]')])
    def test_login_page(self, browser, selector, value):
        browser.get(browser.base_url + '/administration')
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((selector, value))
        )

    @pytest.mark.parametrize('selector, value', [(By.ID, 'form-register'),
                                                 (By.CSS_SELECTOR, '.col-sm-10 .form-check'),
                                                 (By.CLASS_NAME, 'text-end'),
                                                 (By.CSS_SELECTOR, '[name="lastname"]'),
                                                 (By.CSS_SELECTOR, '[name="email"]')])
    def test_registration_page(self, browser, selector, value):
        browser.get(browser.base_url + '/index.php?route=account/register')
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((selector, value))
        )


def test_login_razlogin(browser):
    browser.get(browser.base_url + '/administration')
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[name="username"]'))
    )
    username = browser.find_element(By.CSS_SELECTOR, '[name="username"]')
    username.send_keys('user')
    password = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    password.send_keys('bitnami')
    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'fa-home'))
    )
    assert 'user_token' in browser.current_url, "Вход не выполнен"
    button_out = browser.find_element(By.ID, 'nav-logout')
    button_out.click()
    assert 'login' in browser.current_url, "Выход не выполнен"


def test_add_to_busket(browser):
    browser.get(browser.base_url)
    product = browser.find_element(By.CSS_SELECTOR,
                                   '.row-cols-md-3 .col.mb-3:first-of-type .image [href ^= "h"]')
    product.click()
    button_add = browser.find_element(By.CSS_SELECTOR, '.mb-3 #button-cart')
    button_add.click()
    assert WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.alert-success'))
    ), "Товар не добавлен"


def test_currency_on_main_page(browser):
    browser.get(browser.base_url)
    currency = browser.find_element(By.CSS_SELECTOR, '#form-currency .fa-caret-down')
    currency.click()
    euro = browser.find_element(By.CSS_SELECTOR, '[href="EUR"]')
    euro.click()
    price = browser.find_element(By.CSS_SELECTOR, '.row-cols-md-3 .mb-3:first-of-type .price-new')
    assert '€' in price.text, "Цены не изменились"


def test_currency_on_product_page(browser):
    browser.get(browser.base_url)
    product = browser.find_element(By.CSS_SELECTOR,
                                   '.row-cols-md-3 .col.mb-3:first-of-type .image [href ^= "h"]')
    product.click()
    currency = browser.find_element(By.CSS_SELECTOR, '#form-currency .fa-caret-down')
    currency.click()
    euro = browser.find_element(By.CSS_SELECTOR, '[href="EUR"]')
    euro.click()
    price = browser.find_element(By.CSS_SELECTOR, '.price-new')
    assert '€' in price.text, "Цены не изменились"
