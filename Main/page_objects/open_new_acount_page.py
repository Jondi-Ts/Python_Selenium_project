from selenium.webdriver.common.by import By


class OpenNewAccountPage:

    def __init__(self, driver):
        self.driver = driver

    def new_acount_type(self):
        return self.driver.find_element(By.XPATH, "//select[@id = 'type']")

    def account_for_transfering_to_new_one(self):
        return self.driver.find_element(By.XPATH, "//select[@id = 'fromAccountId']")

    def open_new_account_btn(self):
        return self.driver.find_element(By.XPATH, "//input[@class= 'button']")

    # after opening
    def get_account_opened_message(self):
        return self.driver.find_element(By.XPATH, "//h1[text()='Account Opened!']")

    # TODO add test logic

    '''
    Account Opened!
Congratulations, your account is now open.

Your new account number: 14565'''
