from Pages.Intro_page import IntroPage
from TestCase.base_test import BaseTest




class TestIntroPage(BaseTest):

    def test_intro(self):
        pageIntro= IntroPage(self.driver)
        pageIntro.test_into_to_home()

# python3 -m unittest TestCase.test_01_intro_page
# python -m pytest -s TestCase/test_01_intro_page.py --alluredir=ReportAllure &&  allure serve ReportAllure/



