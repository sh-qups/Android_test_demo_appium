
import sys
import os

import unittest
import pathlib
from appium import webdriver

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


class BaseTest(unittest.TestCase):

    def setUp(self):
        desired_caps = dict(
            platformName='Android',
            platformVersion='10',
            automationName='uiautomator2',
            deviceName='Android Emulator',
            app=pathlib.Path('../../../apps/selendroid-test-app.apk')
        )
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        el = self.driver.find_element_by_accessibility_id('item')
        el.click()

    def test_1(self):
        el = self.driver.find_element_by_accessibility_id('item')
        el.click()

    def tearDown(self):
        self.driver.close()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
