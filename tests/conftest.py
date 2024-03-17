import pytest
import datetime
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import os


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--base_url", default="http://192.168.0.116:8081/")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--logs", action="store_true", default=False)


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    base_url = request.config.getoption("--base_url")
    logger = logging.getLogger(request.node.name)
    log_level = request.config.getoption("--log_level")
    logger.setLevel(level=log_level)
    log_filename = f"logs/{request.node.name}.log"
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.info(f"===> Test {request.node.name} started at {datetime.datetime.now()}")

    driver = None

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "ya":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService(
            executable_path="/home/mikhail/Downloads/drivers/yandexdriver"
        )
        driver = webdriver.Chrome(service=service)

    driver.maximize_window()
    driver.log_level = log_level
    driver.logger = logger
    driver.base_url = base_url
    driver.test_name = request.node.name
    yield driver

    driver.close()
