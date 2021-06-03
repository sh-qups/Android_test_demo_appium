from Pages.home_page import HomePage
from TestCase.base_test import BaseTest


class TestSignup(BaseTest):

    def test_intro(self):
        homepage = HomePage(self.driver)
        homepage.test_signup()

# python3 -m unittest TestCase.test_signup
