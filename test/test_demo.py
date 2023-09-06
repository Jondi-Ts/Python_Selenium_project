import time

import pytest

from Main.extensions.verifications import Verifications
from Main.utilities import expected
from Main.utilities.expected import *
from Main.utilities.manage_pages import Manage_Pages


@pytest.mark.usefixtures('init_web')
class TestBank:

    def test_tc_001(self):
        Verifications.verify_equals(
            self.wwf.register("Mickael", "Jackson", "Haporzim", "Holon", "Gush Daan", 1234567, 987654321, "daniel3",
                              "daniel3", "daniel3"),    registration_welcome)

    def test_tc_002(self):
        Verifications.verify_equals(
            self.wwf.negative_register("Mickael", "Jackson", "Haporzim", "Holon", "Gush Daan", 1234567, 987654321,
                                       "daniel7",
                                       "daniel3", "dfdefe", "password_confirm"), reg_pass_confirm_wrong)

    def test_tc_003(self):
        Verifications.verify_equals(self.wwf.negative_register(
            "Mickael", "Jackson", "Haporzim", "Holon", "Gush Daan", 1234567, 987654321, "daniel7",
            "daniel3", "daniel3", None), reg_username_err)

    def test_tc_004(self):
        Verifications.verify_equals(self.wwf.login("daniel3", "daniel3", None), title_after_login)

    def test_tc_005(self):
        Verifications.verify_equals(self.wwf.login("jndi", "sf", "negative"), wrong_login_message)

    def test_tc_006(self):
        self.wwf.login("daniel3", "daniel3", None)
        self.wwf.log_out()
        Verifications.verify_true(self.wwf.check_username_field_presence())

    def test_tc_007(self):
        self.wwf.login("daniel3", "daniel3", None)
        Verifications.verify_equals(self.wwf.create_new_account("SAVINGS"), new_account_opened_message)
