from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    random_lokator1 = By.ID, 'footer'
    random_lokator2 = By.CLASS_NAME, 'btn-primary'
    LOGIN_BTN = By.CSS_SELECTOR, '.btn.btn-primary'
    PASSWORD = By.CSS_SELECTOR, '[name="password"]'
    USERNAME = By.CSS_SELECTOR, '[name="username"]'
    WORLD_MAP = By.CSS_SELECTOR, '.card-body #vmap'
    LOGOUT_BTN = By.ID, 'nav-logout'
    MENU_CATALOG = By.CSS_SELECTOR, '[href="#collapse-1"]'
    MENU_CATALOG_PRODUCT = (By.CSS_SELECTOR,
                            '[href*="http://192.168.0.116:8081/administration/index.php?route=catalog/product"]')
    PLUS = (By.CSS_SELECTOR,
            '[href*="http://192.168.0.116:8081/administration/index.php?route=catalog/product.form')
    GENERAL_PRODUCT_NAME = By.CSS_SELECTOR, '#input-name-1'
    GENERAL_META_TAG_TITTLE = By.CSS_SELECTOR, '#input-meta-title-1'
    SEO = By.CSS_SELECTOR, '[href = "#tab-seo"]'
    SEO_INPUT = By.CSS_SELECTOR, '#input-keyword-0-1'
    DATA = By.CSS_SELECTOR, '[href="#tab-data"]'
    DATA_MODEL = By.CSS_SELECTOR, '#input-model'
    SAVE_BTN = By.CSS_SELECTOR, '.float-end .btn.btn-primary'
    BACK_BTN = By.CSS_SELECTOR, 'button[aria-label="Save"]'
    PRODUCT_CHECKBOX = By.CSS_SELECTOR, '.table-hover tbody tr:first-child .text-center .form-check-input'
    DELETE_BTN = By.CSS_SELECTOR, '.fa-trash-can'

    @allure.step('Авторизация в роли администратора')
    def authentication(self, timeout, username, password):
        self.correct_input(LoginPage.USERNAME, timeout, username)
        self.correct_input(LoginPage.PASSWORD, timeout, password)
        self.click_element(LoginPage.LOGIN_BTN)
        assert self.get_element(LoginPage.WORLD_MAP), "Вход не выполнен"

    @allure.step('Выход из аккаунта')
    def exit(self):
        self.click_element(LoginPage.LOGOUT_BTN)
        assert self.get_element(LoginPage.PASSWORD), "Выход не выполнен"

    @allure.step('Переход в каталог товаров')
    def open_menu_catalog_product(self):
        self.click_element(LoginPage.MENU_CATALOG)
        self.js_click_element(LoginPage.MENU_CATALOG_PRODUCT)

    @allure.step('Добавляем новый товар')
    def add_new_product(self):
        self.open_menu_catalog_product()
        self.click_element(LoginPage.PLUS, timeout=40)
        self.correct_input(LoginPage.GENERAL_PRODUCT_NAME, timeout=10, text='1Product Test')
        self.correct_input(LoginPage.GENERAL_META_TAG_TITTLE, timeout=10, text='Tag test')
        self.click_element(LoginPage.DATA)
        self.correct_input(LoginPage.DATA_MODEL, timeout=10, text=LoginPage.unique_name(self))
        self.click_element(LoginPage.SEO)
        self.correct_input(LoginPage.SEO_INPUT, timeout=10, text=LoginPage.unique_name(self))
        self.click_element(LoginPage.SAVE_BTN)
        assert self.get_element(BasePage.SUCCESS_ALERT), "Новый товар не создан"

    @allure.step('Удаляем первый в списке товар')
    def delete_product(self):
        self.open_menu_catalog_product()
        self.click_element(LoginPage.PRODUCT_CHECKBOX)
        self.click_element(LoginPage.DELETE_BTN, timeout=20)
        alert = self.browser.switch_to.alert
        alert.accept()
        assert self.get_element(BasePage.SUCCESS_ALERT), "Товар не удален"
