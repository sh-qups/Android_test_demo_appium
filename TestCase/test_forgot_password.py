from Pages.home_page import HomePage
from TestCase.base_test import BaseTest


class TestForgotPassword(BaseTest):

    def test_intro(self):
        homepage = HomePage(self.driver)
        homepage.test_forgot_password()

# python3 -m unittest TestCase.test_forgot_password
