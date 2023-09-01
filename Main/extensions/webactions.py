from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class WebActions:

    def __init__(self, driver):
        self.driver = driver

    def insert_text(self, elem: WebElement, value):
        elem.clear()
        elem.send_keys(value)

    def click_action(self, elem: WebElement):
        elem.click()

    def get_text(self, elem: WebElement):
        return elem.text

    def select_from_dropdown(self, elem: WebElement, dropdown_choice_text: str):
        select = Select(elem)
        select.select_by_visible_text(dropdown_choice_text)


    def clear_key(self, elem: webelement):
        elem.clear()
