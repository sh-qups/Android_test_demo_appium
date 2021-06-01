import time

from appium import webdriver
import unittest


class AndroidCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            # need add two extra capabilities for native app, appium requires app-package and app-activity: testing will start from this activity
            desired_capabilities={'platformName': 'Android',
                                  'deviceName' : 'emulator-5554',
                                  'app-package': 'com.bikroy',
                                  'app-activity': 'se.saltside.activity.main.MainActivity',
                                  # 'app': '/home/asif-rouf/software/Bikroy Sell Rent Buy Find Jobs_v1.2.01_apkpure.com.apk'
                                  'app': '/home/asif-rouf/Sh/Android_test_demo_appium/Apk/Bikroy Sell Rent Buy Find Jobs_v1.2.01_apkpure.com.apk'
        })

    # test case to test addition operation
    def test_01(self):
        driver = self.driver
        time.sleep(10)
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.TextView").click()
        time.sleep(2)
        driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_one_time_button").click()
        time.sleep(10)
        driver.find_element_by_id("com.bikroy:id/main_bottom_panel_home").click()
        time.sleep(2)
        driver.find_element_by_id("com.bikroy:id/main_bottom_panel_search").click()
        time.sleep(2)
        driver.find_element_by_id("com.bikroy:id/main_bottom_panel_chat").click()
        time.sleep(2)
        driver.find_element_by_id("com.bikroy:id/main_bottom_panel_my_account").click()
        time.sleep(10)

        pass

    # # test case to test addition operation
    # def test_add_operation(self):
    #     driver = self.driver
    #     driver.find_element_by_name("2").click()
    #     driver.find_element_by_name("+").click()
    #     driver.find_element_by_name("4").click()
    #     driver.find_element_by_name("=").click()
    #     result = driver.find_element_by_tag_name("EditText").text
    #     self.assertIn("6", result)

    # # test case to test substraction operation
    # def test_sub_operation(self):
    #     driver = self.driver
    #     driver.find_element_by_name("9").click()
    #     driver.find_element_by_name("minus").click()
    #     driver.find_element_by_name("4").click()
    #     driver.find_element_by_name("=").click()
    #     result = driver.find_element_by_tag_name("EditText").text
    #     self.assertIn("5", result)
    #
    # # test case to test multiplication operation
    # def test_mul_operation(self):
    #     driver = self.driver
    #     driver.find_element_by_name("9").click()
    #     driver.find_element_by_name("multiply").click()
    #     driver.find_element_by_name("4").click()
    #     driver.find_element_by_name("=").click()
    #     result = driver.find_element_by_tag_name("EditText").text
    #     self.assertIn("36", result)
    #
    # # test case to test division operation
    # def test_div_operation(self):
    #     driver = self.driver
    #     driver.find_element_by_name("9").click()
    #     driver.find_element_by_name("divide").click()
    #     driver.find_element_by_name("3").click()
    #     driver.find_element_by_name("=").click()
    #     result = driver.find_element_by_tag_name("EditText").text
    #     self.assertIn("3", result)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

