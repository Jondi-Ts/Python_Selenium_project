import pytest

from Main.extensions.verifications import Verifications
from Main.page_objects.login_page import LoginPage
from Main.work_flow.web_wf import Web_Wf

@pytest.mark.usefixtures('init_web')
class Test_web():


    def test_01(self):
        Web_Wf.register("Shir","Zvi", "Haporzim","Holon","Gush Daan", 1234567,987654321,"shirush2000", "shirush2000")
        # Web_Wf.login("vladdu","vladdu")