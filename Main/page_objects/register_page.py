import allure
from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Getting registering button")
    def get_register_btn(self):
        return self.driver.find_element(By.XPATH, "//a[contains(text(), 'Register')]")

    @allure.step("Getting filed for first naem")
    def get_first_name(self):
        return self.driver.find_element(By.ID, "customer.firstName")

    @allure.step("Getting input field for last name")
    def get_last_name(self):
        return self.driver.find_element(By.ID, "customer.lastName")

    def get_adress_street(self):
        return self.driver.find_element(By.ID, "customer.address.street")

    def get_adress_city(self):
        return self.driver.find_element(By.ID, "customer.address.city")

    def get_adress_state(self):
        return self.driver.find_element(By.ID, "customer.address.state")

    def get_adress_zipcode(self):
        return self.driver.find_element(By.ID, "customer.address.zipCode")

    def get_customer_ssn(self):
        return self.driver.find_element(By.ID, "customer.ssn")

    @allure.step("Getting user name field")
    def get_user_name(self):
        return self.driver.find_element(By.ID, "customer.username")

    @allure.step("Getting password field")
    def get_password(self):
        return self.driver.find_element(By.ID, "customer.password")

    @allure.step("Getting password confirm field")
    def get_password_confirm(self):
        return self.driver.find_element(By.ID, "repeatedPassword")

    def get_complete_registration_btn(self):
        return self.driver.find_element(By.XPATH, "//*[@value='Register']")

    # after ragistration
    def get_welcome_message(self):
        return self.driver.find_element(By.XPATH,
                                        '//p[text()="Your account was created successfully. You are now logged in."]')

    # errors for registration, 2 negative tests
    def get_username_error_message(self):
        return self.driver.find_element(By.ID, "customer.username.errors")

    def get_pass_coonfirm_error_message(self):
        return self.driver.find_element(By.ID, 'repeatedPassword.errors')
#
# if __name__ == '__main__':
#     register_page = RegisterPage()
#     register_page.get_register_btn().click()
#     register_page.get_first_name().send_keys("James")
#     time.sleep(10)
