import time

import pytest

from Main.extensions.verifications import Verifications
from Main.page_objects.login_page import LoginPage
from Main.work_flow.webworkflow import WebWorkFlow


@pytest.mark.usefixtures('init_web')
class Test_web():

    def test_01(self):
        self.wwf.register("Mickael", "Jackson", "Haporzim", "Holon", "Gush Daan", 1234567, 987654321, "daniel3", "daniel3")
    # time.sleep(2)
    # Web_Wf.log_out()
    # time.sleep(2)
    # Web_Wf.login("daniel2","daniel2")
    #     self.wwf.get_table_date("daniel3", "daniel3")
