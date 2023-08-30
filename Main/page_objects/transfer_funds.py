from selenium.webdriver.common.by import By


class TransferFundsPage:

    def __init__(self, driver):
        self.driver = driver

    def get_amount_field(self):
        self.driver.find_element(By.XPATH, "//input[@id='i']")

    def get_select_from_account(self):
        return self.driver.find_element(By.XPATH, "//select[@id='fromAccountId']")

    def get_select_to_account(self):
        return self.driver.find_element(By.XPATH, "//select[@id='toAccountId']")

    def get_transfer_button(self):
        return self.driver.find_element(By.XPATH, "//input[@type='submit']")

#todo RESULT
'''
Transfer Complete!
$56756.00 has been transferred from account #19338 to account #19338.

See Account Activity for more details.
'''