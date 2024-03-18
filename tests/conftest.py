import pytest
import datetime
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import os


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--executor", default="http://192.168.0.116")
    parser.addoption("--base_url", default="http://192.168.0.116:8081/")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--logs", action="store_true", default=False)


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    executor = request.config.getoption("--executor")
    logger = logging.getLogger(request.node.name)
    log_level = request.config.getoption("--log_level")
    logger.setLevel(level=log_level)
    log_filename = f"logs/{request.node.name}.log"
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.info(f"===> Test {request.node.name} started at {datetime.datetime.now()}")

    executor_url = f"{executor}:4444/wb/hub"

    if browser_name == "chrome":
        options = ChromeOptions()
    else:
        options = FFOptions()

    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )
    driver.base_url = base_url
    yield driver

    driver.close()
