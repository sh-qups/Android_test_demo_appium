from Pages.home_page import HomePage
from TestCase.base_test import BaseTest


class TestPostAdd(BaseTest):

    def test_intro(self):
        homepage = HomePage(self.driver)
        homepage.test_post_add()

# python3 -m unittest
