from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    def get_register_btn(self):
        return self.driver.find_element_by_id(By.XPATH, "//a[contains(text(), 'Register')]")

    def get_first_name(self):
        return self.driver.find_element(By.ID, "customer.firstName")

    def get_last_name(self):
        return self.driver.find_element(By.ID, "customer.lastName")

    def get_adress_street(self):
        return self.driver.find_element(By.ID, "customer.address.street")

    def get_adress_city(self):
        return self.driver.find_element(By.ID, "customer.address.city")

    def get_adress_State(self):
        return self.driver.find_element(By.ID, "customer.address.state")

    def get_adress_zipcodee(self):
        return self.driver.find_element(By.ID, "customer.address.zipCode")

    def get_customer_ssn(self):
        return self.driver.find_element(By.ID, "customer.ssn")

    def get_user_name(self):
        return self.driver.find_element(By.ID, "customer.username")

    def get_password(self):
        return self.driver.find_element(By.ID, "customer.password")


    def get_password_confirm(self):
        return self.driver.find_element(By.ID, "customer.repeatedPassword")



