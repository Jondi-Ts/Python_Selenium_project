import time

import pytest

from Main import utilities
from Main.extensions.webactions import WebActions
from Main.utilities.manage_pages import Manage_Pages


class WebWorkFlow:

    def __init__(self, driver):
        self.web_actions = WebActions(driver)

    def login(self, user_name: str, password: str):
        self.web_actions.insert_text(Manage_Pages.login_page.get_username_field(), user_name, )
        self.web_actions.insert_text(Manage_Pages.login_page.get_password_field(), password, )
        self.web_actions.click_action(Manage_Pages.login_page.login_btn())

    def register(self, first_name, last_name, adress_street, adress_city, adress_state, adress_zipcode,
                 customer_ssn: int,
                 user_name, password):
        self.web_actions.click_action(Manage_Pages.register_page.get_register_btn())
        self.web_actions.insert_text(Manage_Pages.register_page.get_first_name(), first_name)
        self.web_actions.insert_text(Manage_Pages.register_page.get_last_name(), last_name)
        self.web_actions.insert_text(Manage_Pages.register_page.get_adress_street(),
                                     adress_street)
        self.web_actions.insert_text(Manage_Pages.register_page.get_adress_city(), adress_city)
        self.web_actions.insert_text(Manage_Pages.register_page.get_adress_state(), adress_state)
        self.web_actions.insert_text(Manage_Pages.register_page.get_adress_zipcode(),
                                     adress_zipcode)
        self.web_actions.insert_text(Manage_Pages.register_page.get_customer_ssn(), customer_ssn)
        self.web_actions.insert_text(Manage_Pages.register_page.get_user_name(), user_name)
        self.web_actions.insert_text(Manage_Pages.register_page.get_password(), password)
        self.web_actions.insert_text(Manage_Pages.register_page.get_password_confirm(), password)
        self.web_actions.click_action(Manage_Pages.register_page.get_complete_registration_btn())

    def log_out(self):
        self.web_actions.click_action(Manage_Pages.main_page.log_out_btn())

    def get_table_date(self, user_name, password):
        self.web_actions.insert_text(Manage_Pages.login_page.get_username_field(), user_name, )
        self.web_actions.insert_text(Manage_Pages.login_page.get_password_field(), password, )
        self.web_actions.click_action(Manage_Pages.login_page.login_btn())
        self.web_actions.click_action(Manage_Pages.main_page.acount_overview())
        time.sleep(2)
        table_rows = Manage_Pages.account_overview_page.get_table_rows()
        for table_row in table_rows:
            cell_data = Manage_Pages.account_overview_page.get_cell_data(table_row)
            print(f"cell data: {cell_data}")

            # account types CHECKING/SAVINGS

    def create_new_account(self, account_type: str):
        self.web_actions.click_action(Manage_Pages.main_page.open_new_acount())
        self.web_actions.select_from_dropdown(Manage_Pages.open_new_account_page.new_acount_type(), account_type)
        self.web_actions.click_action(Manage_Pages.open_new_account_page.open_new_account_btn())

    def transfer_money(self, amount_of_money, from_account, to_account):
        self.web_actions.click_action(Manage_Pages.main_page.transfer_funds())
        self.web_actions.insert_text(Manage_Pages.transfer_funds_page.get_amount_field(), amount_of_money)
        self.web_actions.select_from_dropdown(Manage_Pages.transfer_funds_page.get_select_from_account(),from_account)
        self.web_actions.select_from_dropdown(Manage_Pages.transfer_funds_page.get_select_to_account(), to_account)
        self.web_actions.click_action(Manage_Pages.transfer_funds_page.get_transfer_button())