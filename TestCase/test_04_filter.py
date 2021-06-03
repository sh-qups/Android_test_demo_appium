from Pages.home_page import HomePage
from TestCase.base_test import BaseTest


class TestFilter(BaseTest):

    def test_intro(self):
        homepage = HomePage(self.driver)
        homepage.test_filter()

# python3 -m unittest TestCase.test_04_filter
