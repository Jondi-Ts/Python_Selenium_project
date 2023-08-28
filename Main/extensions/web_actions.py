from selenium.webdriver.remote import webelement


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
