import time

import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# web driver initilization
from Main.utilities.manage_pages import Manage_Pages

driver: webdriver = None


@pytest.fixture(scope='class')
def init_web():
    driver = init_chrome()
    # globals()["driver"] = driver
    driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    Manage_Pages.init_web_pages(driver)
    yield
    time.sleep(5)
    driver.quit()


def init_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver
