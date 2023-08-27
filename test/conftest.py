import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# web driver initilization
from utilities.manage_pages import Manage_Pages

driver = None


@pytest.fixture(scope='class')
def init_web():
    driver = init_chrome()
    globals()["driver"] = driver
    Manage_Pages.init_web_pages(driver)


def init_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver
