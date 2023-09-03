import time

import pytest

from Main.extensions.verifications import Verifications
from Main.utilities import expected


@pytest.mark.usefixtures('init_web')
class Test_web():

    def test_tc_001(self):
        Verifications.verify_equals(
            self.wwf.register("Mickael", "Jackson", "Haporzim", "Holon", "Gush Daan", 1234567, 987654321, "daniel7",
                              "daniel3", "daniel3"), expected.registration_welcome)

    def test_tc_002(self):
        Verifications.verify_equals(
            self.wwf.negative_register("Mickael", "Jackson", "Haporzim", "Holon", "Gush Daan", 1234567, 987654321,
                                       "daniel7",
                                       "daniel3", "dfdefe", "password_confirm"), expected.reg_pass_confirm_wrong)

    def test_tc_003(self):
        Verifications.verify_equals(self.wwf.negative_register(
            "Mickael", "Jackson", "Haporzim", "Holon", "Gush Daan", 1234567, 987654321, "daniel7",
            "daniel3", "daniel3", None), expected.reg_username_err)
