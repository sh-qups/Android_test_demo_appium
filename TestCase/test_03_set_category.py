from Pages.home_page import HomePage
from TestCase.base_test import BaseTest


class TestSetCategory(BaseTest):

    def test_intro(self):
        homepage = HomePage(self.driver)
        homepage.test_set_category()

# python3 -m unittest TestCase.test_03_set_category
