import sys
import os

from base_test import BaseTest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class TestDate(BaseTest):

    def test_1(self):
        el = self.driver.find_element_by_accessibility_id('item')
        el.click()

# python3 -m unittest test_1

