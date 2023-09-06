from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class WebActions:
    def __init__(self, driver, time_out=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, time_out)

    def insert_text(self, elem: WebElement, value):
        # elem = self.wait.until(EC.invisibility_of_element(elem))
        elem.send_keys(value)

    def click_action(self, elem: WebElement):
        element = self.wait.until(EC.element_to_be_clickable(elem))
        element.click()

    def get_text(self, elem: WebElement):
        elem = self.wait.until(EC.visibility_of(elem))
        return elem.text

    def select_from_dropdown(self, elem: WebElement, dropdown_choice_text, type, index):
        if type == "text":
            dropdown = Select(elem)
            dropdown.select_by_visible_text(dropdown_choice_text)
        elif type == "index":
            dropdown = Select(elem)
            dropdown.select_by_index(index)

    def clear_key(self, elem: WebElement):
        elem = self.wait.until(EC.element_to_be_clickable(elem))
        elem.clear()

    def refresh(self):
        self.driver.refresh()

    def is_element_present(self, locator_strategy, value):
        try:
            locator = (locator_strategy, value)
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )
            return True
        except NoSuchElementException:
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
