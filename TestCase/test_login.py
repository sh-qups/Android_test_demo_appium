from Pages.home_page import HomePage
from TestCase.base_test import BaseTest


class TestLogin(BaseTest):

    def test_intro(self):
        homepage = HomePage(self.driver)
        homepage.test_login()

# python3 -m unittest TestCase.test_login