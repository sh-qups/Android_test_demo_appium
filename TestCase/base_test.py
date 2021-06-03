import unittest
from appium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={'platformName': 'Android',
                                  'deviceName': 'emulator-5554',
                                  'app-package': 'com.bikroy',
                                  'app-activity': 'se.saltside.activity.main.MainActivity',
                                  'app': '/home/asif-rouf/Sh/Android_test_demo_appium/Apk/Bikroy Sell Rent Buy Find Jobs_v1.2.01_apkpure.com.apk'
                                  # 'app': '/home/rk/PycharmProjects/Android_test_demo_appium/Apk/Bikroy Sell Rent Buy Find Jobs_v1.2.01_apkpure.com.apk'
                                  })

        # desired_capabilities = {'platformName': 'Android',
        #                         # 'automationName': 'UiAutomator2',
        #                         'deviceName': 'emulator-5554',
        #                         # 'platformVersion': '11.0.0',
        #                         'app-package': 'com.bikroy',
        #                         'app-activity': 'se.saltside.activity.main.MainActivity',
        #                         # 'app': '/home/asif-rouf/software/Bikroy Sell Rent Buy Find Jobs_v1.2.01_apkpure.com.apk'
        #                         'app': '/home/rk/PycharmProjects/Android_test_demo_appium/Apk/Bikroy Sell Rent Buy Find Jobs_v1.2.01_apkpure.com.apk'
        #                         }
        # self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_capabilities)

    def tearDown(self):
        # self.driver.close()
        self.driver.quit()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
