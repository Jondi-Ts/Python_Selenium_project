from selenium import webdriver

from Main.page_objects.accounts_overview import AccountsOverviewPage
from Main.page_objects.find_transactions_page import FindTransferFundsPage
from Main.page_objects.login_page import LoginPage
from Main.page_objects.main_page import MainPage
from Main.page_objects.open_new_acount_page import OpenNewAccountPage
from Main.page_objects.register_page import RegisterPage
from Main.page_objects.transfer_funds import TransferFundsPage



class Manage_Pages:
    login_page = None
    register_page = None
    main_page = None
    open_new_account_page = None
    account_overview_page = None
    transfer_funds_page = None
    find_transactions_page = None

    @classmethod
    def init_web_pages(cls, driver):
        cls.login_page = LoginPage(driver)
        cls.register_page = RegisterPage(driver)
        cls.main_page = MainPage(driver)
        cls.open_new_account_page = OpenNewAccountPage(driver)
        cls.account_overview_page = AccountsOverviewPage(driver)
        cls.transfer_funds_page = TransferFundsPage(driver)
        cls.find_transactions_page = FindTransferFundsPage(driver)
