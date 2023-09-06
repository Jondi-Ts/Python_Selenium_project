import time

import pytest
from selenium.webdriver.common.by import By

from Main import utilities
from Main.extensions.webactions import WebActions
from Main.utilities.manage_pages import Manage_Pages


class WebWorkFlow:

    def __init__(self, driver):
        self.web_actions = WebActions(driver)

    def login(self, user_name: str, password: str, login_type):
        self.web_actions.insert_text(Manage_Pages.login_page.get_username_field(), user_name)
        self.web_actions.insert_text(Manage_Pages.login_page.get_password_field(), password)
        self.web_actions.click_action(Manage_Pages.login_page.login_btn())
        if login_type == "negative":
            return Manage_Pages.login_page.get_error_login_message().text
        elif login_type == "positive":
            return Manage_Pages.main_page.account_overview_title().text
        else:
            return None

    def common_register_actions(self, first_name, last_name, adress_street, adress_city, adress_state,
                                adress_zipcode,
                                customer_ssn: int, user_name, password, confirm_password):
        self.web_actions.click_action(Manage_Pages.register_page.get_register_btn())
        self.web_actions.insert_text(Manage_Pages.register_page.get_first_name(), first_name)
        self.web_actions.insert_text(Manage_Pages.register_page.get_last_name(), last_name)
        self.web_actions.insert_text(Manage_Pages.register_page.get_adress_street(), adress_street)
        self.web_actions.insert_text(Manage_Pages.register_page.get_adress_city(), adress_city)
        self.web_actions.insert_text(Manage_Pages.register_page.get_adress_state(), adress_state)
        self.web_actions.insert_text(Manage_Pages.register_page.get_adress_zipcode(), adress_zipcode)
        self.web_actions.insert_text(Manage_Pages.register_page.get_customer_ssn(), customer_ssn)
        self.web_actions.insert_text(Manage_Pages.register_page.get_user_name(), user_name)
        self.web_actions.insert_text(Manage_Pages.register_page.get_password(), password)
        self.web_actions.insert_text(Manage_Pages.register_page.get_password_confirm(), confirm_password)
        self.web_actions.click_action(Manage_Pages.register_page.get_complete_registration_btn())

    def register(self, first_name, last_name, adress_street, adress_city, adress_state, adress_zipcode,
                 customer_ssn: int, user_name, password, confirm_password):
        self.common_register_actions(first_name, last_name, adress_street, adress_city, adress_state,
                                     adress_zipcode,
                                     customer_ssn, user_name, password, confirm_password)
        return Manage_Pages.register_page.get_welcome_message().text

    def negative_register(self, first_name, last_name, adress_street, adress_city, adress_state, adress_zipcode,
                          customer_ssn: int, user_name, password, confirm_password, type):
        self.common_register_actions(first_name, last_name, adress_street, adress_city, adress_state,
                                     adress_zipcode,
                                     customer_ssn, user_name, password, confirm_password)
        if type == "password_confirm":
            return Manage_Pages.register_page.get_pass_coonfirm_error_message().text
        else:
            return Manage_Pages.register_page.get_username_error_message().text

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
        time.sleep(1)
        self.web_actions.select_from_dropdown(Manage_Pages.open_new_account_page.new_acount_type(), account_type,
                                              "text", None)
        time.sleep(1)
        self.web_actions.click_action(Manage_Pages.open_new_account_page.open_new_account_btn())
        if self.web_actions.is_element_present(By.XPATH, "//h1[text()='Account Opened!']"):
            return Manage_Pages.open_new_account_page.get_account_opened_message().text

    # Todo find better way to handle transfering money bug with entering ammount without refresh drop down info is undefined
    def transfer_money(self, amount_of_money, to_account):
        self.web_actions.click_action(Manage_Pages.main_page.transfer_funds())
        time.sleep(1)
        self.web_actions.refresh()
        time.sleep(1)
        self.web_actions.insert_text(Manage_Pages.transfer_funds_page.get_amount_field(), amount_of_money)
        drop_down = Manage_Pages.transfer_funds_page.get_select_to_account()
        self.web_actions.select_from_dropdown(drop_down, to_account, "index", to_account)
        self.web_actions.click_action(Manage_Pages.transfer_funds_page.get_transfer_button())
        if self.web_actions.is_element_present(By.XPATH, "//h1[text()='Transfer Complete!']"):
            return Manage_Pages.transfer_funds_page.get_transfer_result_message().text

    def find_transaction_by_amount(self, account_number, transsaction_amount):
        self.web_actions.click_action(Manage_Pages.main_page.find_transactions())
        accounts_drop = Manage_Pages.find_transactions_page.get_account_dropdown()
        self.web_actions.select_from_dropdown(accounts_drop, account_number, "text", None)
        self.web_actions.insert_text(Manage_Pages.find_transactions_page.get_transaction_amount_field(),
                                     transsaction_amount)
        self.web_actions.click_action(Manage_Pages.find_transactions_page.get_transaction_amount_btn_search())

    def check_username_field_presence(self):
        parameters = Manage_Pages.login_page.get_customer_login_title()
        return self.web_actions.is_element_present(parameters[0], parameters[1])
