from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def log_out_btn(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Log Out']")

    def open_new_acount(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Open New Account']")

    def acount_overview(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Accounts Overview']")

    def transfer_funds(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Transfer Funds]")

    def bill_pay(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Bill Pay]")

    def find_transactions(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Find Transactions]")

    def update_contact_info(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Update Contact Info]")

    def request_loan(self):
        return self.driver.find_element(By.XPATH, "//a[text()='Request Loan]")
