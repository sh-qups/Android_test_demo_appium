from Pages.intro_page import IntroPage
from TestCase.base_test import BaseTest


class TestIntroPage(BaseTest):

    def test_intro(self):
        intro_page = IntroPage(self.driver)
        intro_page.test_intro_to_home()

# python3 -m unittest TestCase.test_01_intro_to_home
