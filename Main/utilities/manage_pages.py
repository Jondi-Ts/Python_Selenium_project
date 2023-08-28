from selenium import webdriver

from Main.page_objects.accounts_overview import AccountsOverviewPage
from Main.page_objects.login_page import LoginPage
from Main.page_objects.main_page import MainPage
from Main.page_objects.open_new_acount_po import OpenNewAccountPo
from Main.page_objects.register_page import RegisterPage

login_page = None
register_page = None


class Manage_Pages:
    login_page = None
    register_page = None
    main_page = None
    open_new_account_page = None
    acount_overview = None

    @classmethod
    def init_web_pages(cls, driver):
        cls.login_page = LoginPage(driver)
        cls.register_page = RegisterPage(driver)
        cls.main_page = MainPage(driver)
        cls.open_new_account_page = OpenNewAccountPo(driver)
        cls.acount_overview = AccountsOverviewPage(driver)
