import pytest
import datetime
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
import os
from selenium.webdriver.chrome.service import Service as ChromeService


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--executor", default="http://127.0.0.1")
    parser.addoption("--base_url", default="http://192.168.0.116:8081/")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--type_start", default="local")
    parser.addoption("--vnc", action="store_true")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--base_url")
    executor = request.config.getoption("--executor")
    headless = request.config.getoption("--headless")
    type_start = request.config.getoption("--type_start")
    logger = logging.getLogger(request.node.name)
    log_level = request.config.getoption("--log_level")
    logger.setLevel(level=log_level)
    vnc = request.config.getoption("--vnc")
    log_filename = f"logs/{request.node.name}.log"
    os.makedirs(os.path.dirname(log_filename), exist_ok=True)
    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.info(f"===> Test {request.node.name} started at {datetime.datetime.now()}")
    executor_url = f"{executor}:4444/wd/hub"

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        service = ChromeService()
        if type_start == "local":
            driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless:
            options.add_argument("-headless")
        if type_start == "local":
            driver = webdriver.Firefox(options=options)
    if type_start == "selenoid":
        caps = {
            "browserName": browser_name,
            "selenoid:options": {
                "enableVNC": vnc,
                "screenResolution": "1280x2000"
            }
        }

        for k, v in caps.items():
            options.set_capability(k, v)

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options
        )
    driver.base_url = base_url
    driver.test_name = request.node.name
    driver.log_level = log_level
    yield driver
    driver.close()
