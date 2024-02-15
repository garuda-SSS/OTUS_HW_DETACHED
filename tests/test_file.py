from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_add_to_busket_1(browser):
    browser.get(browser.base_url)
    browser.set_window_size(1920,1080)
    product = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]')
    product.click()


def test_add_to_busket_2(browser):
    browser.get(browser.base_url)
    assert WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]'))
    )
    product = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]')
    product.click()


def test_add_to_busket_3(browser):
    browser.get(browser.base_url)
    product = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/form/div/button[1]')
    actions = ActionChains(browser)
    actions.move_to_element(product).perform()
    product.click()
