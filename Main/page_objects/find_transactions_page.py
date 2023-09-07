from selenium.webdriver.common.by import By


class FindTransferFundsPage:

    def __init__(self, driver):
        self.driver = driver

    def get_account_dropdown(self):
        return self.driver.find_element(By.XPATH, "//select[@id='accountId']")

    def get_transaction_id_field(self):
        return self.driver.find_element(By.XPATH, "//input[@id='criteria.transactionId']")

    def get_transaction_id_btn_search(self):
        return self.driver.find_element(By.XPATH, '//button[@ng-click="criteria.searchType = \'ID\'"]')

    def get_find_by_date(self):
        return self.driver.find_element(By.XPATH, "//input[@id='criteria.onDate']")

    def get_transaction_date_btn_search(self):
        return self.driver.find_element(By.XPATH, '//button[@ng-click="criteria.searchType = \'DATE\'"]')

    def get_transaction_amount_field(self):
        return self.driver.find_element(By.XPATH, "//input[@id='criteria.amount']")

    def get_transaction_amount_btn_search(self):
        return self.driver.find_element(By.XPATH, '//button[@ng-click="criteria.searchType = \'AMOUNT\'"]')

    # Todo use for tests
    def get_transaction_result_amount(self):
        return self.driver.find_element(By.XPATH, "//span[@class='ng-binding ng-scope']")


'''
Transaction Results
Date	Transaction	Debit (-)	Credit (+)
08-30-2023	Funds Transfer Sent	$56756.00	
08-30-2023	Funds Transfer Received		$56756.00

'''
