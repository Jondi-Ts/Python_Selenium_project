from selenium import webdriver

from Main.page_objects.login_page import LoginPage
from Main.page_objects.register_page import RegisterPage


class Manage_Pages:

    def init_web_pages(driver):
        globals()['login_page'] = LoginPage(driver)
        globals()['register_page'] = RegisterPage(driver)