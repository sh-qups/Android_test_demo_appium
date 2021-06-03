from Pages.home_page import HomePage
from TestCase.base_test import BaseTest


class TestClickAdd(BaseTest):

    def test_intro(self):
        homepage = HomePage(self.driver)
        homepage.test_switch()

# python3 -m unittest TestCase.test_switch
