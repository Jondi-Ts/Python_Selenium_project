import time

import pytest

from Main.extensions.verifications import Verifications
from Main.page_objects.login_page import LoginPage
from Main.work_flow.web_wf import Web_Wf

@pytest.mark.usefixtures('init_web')
class Test_web():


    def test_01(self):
        # Web_Wf.register("Shir","Zvi", "Haporzim","Holon","Gush Daan", 1234567,987654321,"daniel2", "daniel2")
        # time.sleep(2)
        # Web_Wf.log_out()
        # time.sleep(2)
        Web_Wf.login("daniel2","daniel2")