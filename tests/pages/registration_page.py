from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class RegistrationPage(BasePage):
    CONTINUE_BTN = By.CSS_SELECTOR, '.btn.btn-primary'
    PASSWORD = By.CSS_SELECTOR, '[name="password"]'
    FIRSTNAME = By.CSS_SELECTOR, '[name="firstname"]'
    LASTNAME = By.CSS_SELECTOR, '[name="lastname"]'
    EMAIL = By.CSS_SELECTOR, '[name="email"]'
    POLICY_AGREE_BTN = By.CSS_SELECTOR, '#form-register > div > div > input'
    TITTLE = By.CSS_SELECTOR, '#content h1'

    @allure.step('Создаем нового пользователя')
    def create_new_user(self):
        email = self.unique_name()+'@test.test'
        self.correct_input(RegistrationPage.FIRSTNAME, timeout=5, text='test')
        self.correct_input(RegistrationPage.LASTNAME, timeout=5, text='test')
        self.correct_input(RegistrationPage.EMAIL, timeout=5, text=email)
        self.correct_input(RegistrationPage.PASSWORD, timeout=5, text='password')
        self.scroll_to_element(RegistrationPage.POLICY_AGREE_BTN)
        self.click_element(RegistrationPage.POLICY_AGREE_BTN)
        self.click_element(RegistrationPage.CONTINUE_BTN)
        self.wait_to_vanish(RegistrationPage.POLICY_AGREE_BTN)
        assert 'Your Account Has Been Created!' == self.get_element(RegistrationPage.TITTLE).text,\
            "Пользователь не создан"
