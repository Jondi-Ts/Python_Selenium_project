import pytest

from Main.extensions.verifications import Verifications
from Main.page_objects.login_page import LoginPage

pytest.mark.usefixtures('init_web')
class Test_web():


    def test_01(self):
