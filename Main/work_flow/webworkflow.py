import time

import pytest

from Main import utilities
from Main.extensions.webactions import WebActions
from Main.utilities.manage_pages import Manage_Pages


class WebWorkFlow:

    def __init__(self, driver):
        self.web_actions = WebActions(driver)

    def login(self, user_name: str, password: str):
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.login_page.get_username_field(), user_name, )
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.login_page.get_password_field(), password, )
        self.web_actions.click_action(utilities.manage_pages.Manage_Pages.login_page.login_btn())

    def register(self, first_name, last_name, adress_street, adress_city, adress_state, adress_zipcode,
                 customer_ssn: int,
                 user_name, password):
        self.web_actions.click_action(utilities.manage_pages.Manage_Pages.register_page.get_register_btn())
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_first_name(), first_name)
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_last_name(), last_name)
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_adress_street(),
                                     adress_street)
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_adress_city(), adress_city)
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_adress_state(), adress_state)
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_adress_zipcode(),
                                     adress_zipcode)
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_customer_ssn(), customer_ssn)
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_user_name(), user_name)
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_password(), password)
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_password_confirm(), password)
        self.web_actions.click_action(utilities.manage_pages.Manage_Pages.register_page.get_complete_registration_btn())


    def log_out(self):
        WebActions.click_action(utilities.manage_pages.Manage_Pages.main_page.log_out_btn())


    def get_table_date(self, user_name, password):
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.login_page.get_username_field(), user_name, )
        self.web_actions.insert_text(utilities.manage_pages.Manage_Pages.login_page.get_password_field(), password, )
        self.web_actions.click_action(utilities.manage_pages.Manage_Pages.login_page.login_btn())
        self.web_actions.click_action(utilities.manage_pages.Manage_Pages.main_page.acount_overview())
        time.sleep(2)
        table_rows = utilities.manage_pages.Manage_Pages.account_overview_page.get_table_rows()
        for table_row in table_rows:
            cell_data = utilities.manage_pages.Manage_Pages.account_overview_page.get_cell_data(table_row)
            print(f"cell data: {cell_data}")
