from selenium.webdriver.remote import webelement
from selenium.webdriver.support.select import Select


class Web_Actions:

    @staticmethod
    def insert_text(elem: webelement, value):
        elem.send_keys(value)

    @staticmethod
    def click_action(elem: webelement):
        elem.click()

    @staticmethod
    def get_text(elem: webelement):
        return elem.text

    @staticmethod
    def select_from_dropdown(elem: webelement, dropwdonw_choice_text: str):
        select = Select(elem)
        select.select_by_visible_text(dropwdonw_choice_text)
