import time

import pytest as pytest
from selenium import webdriver
from urllib3.util import request
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from Main.extensions.webactions import WebActions
# web driver initilization
from Main.utilities.manage_pages import Manage_Pages
from Main.work_flow.webworkflow import WebWorkFlow

driver: webdriver = None
web_flow_actions = None

@pytest.fixture(scope='class')
def init_web(request):
    driver = init_chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    driver.maximize_window()
    Manage_Pages.init_web_pages(driver)
    wwf = WebWorkFlow(driver)  # Create a single instance of WebWorkFlow
    request.cls.wwf = wwf  # Set the instance to the test class attribute
    yield   # Yield the driver object
    time.sleep(100)
    driver.find_elements()
    # driver.quit()



def init_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


