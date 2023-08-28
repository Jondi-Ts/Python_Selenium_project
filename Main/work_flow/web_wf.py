from Main import utilities
from Main.extensions.web_actions import Web_Actions
from Main.utilities.manage_pages import Manage_Pages


class Web_Wf:
    @staticmethod
    def login(user_name: str, password: str):
        Web_Actions.insert_text(user_name, utilities.manage_pages.Manage_Pages.login_page.get_username_field())
        Web_Actions.insert_text(password, utilities.manage_pages.Manage_Pages.login_page.get_password_field())
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
