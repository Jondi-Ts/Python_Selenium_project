from selenium.webdriver.common.by import By


class AccountsOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_acount_info_taable(self):
        return self.driver.find_element(By.XPATH, "//table[@id='accountTable']")

    '''
        # Locate Table Elements using XPath
                                                  table = driver.find_element(By.XPATH, "//table[@id='accountTable']")
                                                  table_rows = table.find_elements(By.TAG_NAME, "tr")
                                                  
                                                  # Loop through each row (including headers and footer) and extract data
                                                  for row in table_rows:
                                                      cells = row.find_elements(By.TAG_NAME, "td")
                                                      for cell in cells:
                                                          print("Cell Data:", cell.text)
                                                  
                                                  # Close the Browser
                                                  driver.quit()'''
