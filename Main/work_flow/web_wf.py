import time

from Main import utilities
from Main.extensions.web_actions import Web_Actions
from Main.utilities.manage_pages import Manage_Pages


class Web_Wf:
    @staticmethod
    def login(user_name: str, password: str):
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.login_page.get_username_field(), user_name, )
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.login_page.get_password_field(), password, )
        Web_Actions.click_action(utilities.manage_pages.Manage_Pages.login_page.login_btn())

    @staticmethod
    def register(first_name, last_name, adress_street, adress_city, adress_state, adress_zipcode, customer_ssn: int,
                 user_name, password):
        Web_Actions.click_action(utilities.manage_pages.Manage_Pages.register_page.get_register_btn())
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_first_name(), first_name)
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_last_name(), last_name)
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_adress_street(), adress_street)
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_adress_city(), adress_city)
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_adress_state(), adress_state)
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_adress_zipcode(), adress_zipcode)
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_customer_ssn(), customer_ssn)
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_user_name(), user_name)
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_password(), password)
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.register_page.get_password_confirm(), password)
        Web_Actions.click_action(utilities.manage_pages.Manage_Pages.register_page.get_complete_registration_btn())

    @staticmethod
    def log_out():
        Web_Actions.click_action(utilities.manage_pages.Manage_Pages.main_page.log_out_btn())

    @staticmethod
    def get_table_date(user_name, password):
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.login_page.get_username_field(), user_name, )
        Web_Actions.insert_text(utilities.manage_pages.Manage_Pages.login_page.get_password_field(), password, )
        Web_Actions.click_action(utilities.manage_pages.Manage_Pages.login_page.login_btn())
        Web_Actions.click_action(utilities.manage_pages.Manage_Pages.main_page.acount_overview())
        time.sleep(2)
        table_rows = utilities.manage_pages.Manage_Pages.acount_overview.get_table_rows()
        for table_row in table_rows:
            cell_data = utilities.manage_pages.Manage_Pages.acount_overview.get_cell_data(table_row)
            print(f"cell data: {cell_data}")
