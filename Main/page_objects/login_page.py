from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_username_field(self):
        return self.driver.find_element(By.XPATH, "//input[@name='username']")

    def get_password_field(self):
        return self.driver.find_element(By.XPATH, "//input[@name='password']")

    def login_btn(self):
        return self.driver.find_element(By.XPATH, "//input[@class='button']")

    # error message when logging wrong credentials
    def get_error_login_message(self):
        return self.driver.find_element(By.CLASS_NAME, "title")

    def get_customer_login_title(self):
        parameters = [By.XPATH, "//h2[text()='Customer Login']"]
        return parameters
