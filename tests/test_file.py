import pytest
from pages.main_page import MainPage
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
import allure


class Test_part_two():
    @allure.title('Проверка поиска локаторов на главной странице')
    @pytest.mark.parametrize('locator', [MainPage.random_lokator1,
                                         MainPage.random_lokator2,
                                         MainPage.OPEN_PRODUCT,
                                         MainPage.CURRENCY_LIST,
                                         MainPage.ADD_TO_BASKET_BTN])
    def test_main_page(self, browser, locator):
        page = MainPage(browser)
        page.open()
        page.get_element(locator)

    @allure.title('Проверка поиска локаторов на странице каталога')
    @pytest.mark.parametrize('locator', [CatalogPage.random_lokator1,
                                         CatalogPage.random_lokator2,
                                         CatalogPage.random_lokator3,
                                         CatalogPage.random_lokator4,
                                         CatalogPage.random_lokator5])
    def test_catalog_page(self, browser, locator):
        page = CatalogPage(browser)
        page.open(dop='/en-gb/catalog/laptop-notebook')
        page.get_element(locator)

    @allure.title('Проверка поиска локаторов на странице товара')
    @pytest.mark.parametrize('locator', [ProductPage.random_lokator1,
                                         ProductPage.random_lokator2,
                                         ProductPage.random_lokator3,
                                         ProductPage.random_lokator4,
                                         ProductPage.PRICE])
    def test_product_page(self, browser, locator):
        page = ProductPage(browser)
        page.open(dop='/en-gb/product/laptop-notebook/hp-lp3065')
        page.get_element(locator)

    @allure.title('Проверка поиска локаторов на странице авторизации')
    @pytest.mark.parametrize('locator', [LoginPage.random_lokator1,
                                         LoginPage.random_lokator2,
                                         LoginPage.LOGIN_BTN,
                                         LoginPage.PASSWORD,
                                         LoginPage.USERNAME])
    def test_login_page(self, browser, locator):
        page = LoginPage(browser)
        page.open(dop='/administration')
        page.get_element(locator)

    @allure.title('Проверка поиска локаторов на странице регистрации')
    @pytest.mark.parametrize('locator', [RegistrationPage.CONTINUE_BTN,
                                         RegistrationPage.PASSWORD,
                                         RegistrationPage.FIRSTNAME,
                                         RegistrationPage.LASTNAME,
                                         RegistrationPage.EMAIL])
    def test_registration_page(self, browser, locator):
        page = RegistrationPage(browser)
        page.open(dop='/index.php?route=account/register')
        page.get_element(locator)


@allure.title('Проверка логина и разлогина')
def test_login_razlogin(browser):
    page = LoginPage(browser)
    page.open(dop='/administration')
    page.authentication(5, 'user', 'bitnami')
    page.exit()


@allure.title('Проверка добавления в корзину товара')
def test_add_to_busket(browser):
    page = MainPage(browser)
    page.open()
    page.add_product_to_basket(MainPage.ADD_TO_BASKET_BTN)


@allure.title('Проверка смены валюты на главной странице')
@pytest.mark.parametrize('currency_name', ['euro',
                                           'dollar',
                                           'pound'])
def test_currency_on_main_page(browser, currency_name):
    page = MainPage(browser)
    page.open()
    page.change_currency(currency_name, MainPage.PRICE)


@allure.title('Проверка смены валюты на странице товара')
@pytest.mark.parametrize('currency_name', ['euro',
                                           'dollar',
                                           'pound'])
def test_currency_on_product_page(browser, currency_name):
    page = MainPage(browser)
    page.open()
    page.click_element(MainPage.OPEN_PRODUCT)
    page.change_currency(currency_name, ProductPage.PRICE)


@allure.title('Проверка добавления нового товара')
def test_add_new_product(browser):
    page = LoginPage(browser)
    page.open(dop='/administration')
    page.authentication(5, 'user', 'bitnami')
    page.add_new_product()


@allure.title('Проверка удаления товара')
def test_delete_product(browser):
    page = LoginPage(browser)
    page.open(dop='/administration')
    page.authentication(5, 'user', 'bitnami')
    page.add_new_product()
    page.open_menu_catalog_product()
    page.delete_product()


@allure.title('Проверка регистрации нового пользователя')
def test_new_user(browser):
    page = RegistrationPage(browser)
    page.open(dop='/index.php?route=account/register')
    page.create_new_user()
