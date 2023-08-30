from selenium.webdriver.common.by import By


class AccountsOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.table_locator = (By.XPATH, "//table[@id='accountTable']")

    def get_table_rows(self):
        table = self.driver.find_element(*self.table_locator)
        return table.find_elements(By.TAG_NAME, "tr")

    def get_cell_data(self, row):
        cells = row.find_elements(By.TAG_NAME, "td")
        cell_data = []
        for cell in cells:
            cell_data.append(cell.text)
        return cell_data

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
