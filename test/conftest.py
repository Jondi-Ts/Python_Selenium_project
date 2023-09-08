from datetime import datetime
import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from Main.utilities.manage_pages import Manage_Pages
from Main.work_flow.webworkflow import WebWorkFlow




@pytest.fixture(scope='class')
def init_web(request):
    global driver
    driver = init_chrome()
    driver.get("https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC")
    driver.maximize_window()
    Manage_Pages.init_web_pages(driver)
    wwf = WebWorkFlow(driver)  # Create a single instance of WebWorkFlow
    request.cls.wwf = wwf  # Set the instance to the test class attribute
    yield  # Yield the driver object
    time.sleep(10)
    driver.quit()


def init_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver


@pytest.hookimpl(tryfirst=True)
def pytest_exception_interact(report):
    # timestamp = datetime.now().strftime("%m-%d-%H-%M")
    if report.failed:
        timestamp = "jondi"
        print(timestamp)
        allure.attach(driver.get_screenshot_as_png(), name=f"screenshot_{timestamp}",
                      attachment_type=AttachmentType.PNG)
        print("screenshoted")
