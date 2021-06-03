from Pages.home_page import HomePage
from TestCase.base_test import BaseTest


class TestSearch(BaseTest):

    def test_intro(self):
        homepage = HomePage(self.driver)
        homepage.test_search()

# python3 -m unittest TestCase.test_05_search
