from Pages.home_page import HomePage
from TestCase.base_test import BaseTest


class TestSelectLocation(BaseTest):

    def test_intro(self):
        homepage = HomePage(self.driver)
        homepage.test_set_location()

# python3 -m unittest TestCase.test_02_set_location
