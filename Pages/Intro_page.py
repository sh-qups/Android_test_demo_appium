from Pages.base_page import BasePage
from Utils.locators import IntroPageLocator, HomePageLocator
from time import sleep


class IntroPage(BasePage):

    def __init__(self, driver):
        self.locator = IntroPageLocator
        self.locatorHomepage = HomePageLocator
        super().__init__(driver)


    def test_into_to_home(self):
        driver = self.driver
        sleep(2)
        # print(self.locator.language)
        driver.find_element_by_xpath(self.locator.language).click()
        sleep(2)
        driver.find_element_by_id(self.locator.maybe_latter).click()
        sleep(2)
        driver.find_element_by_id(self.locator.location_permission_this_time).click()
        sleep(20)
        res = driver.find_element_by_xpath(self.locatorHomepage.location).text
        print("element found in homepage: " + res)
        assert res == 'Location'

    # def test_01(self):
    #     driver = self.driver
    #     sleep(10)
    #     driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.TextView").click()
    #     sleep(2)
    #     driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_one_time_button").click()
    #     sleep(20)
    #     driver.find_element_by_id("com.bikroy:id/main_bottom_panel_home").click()
    #     sleep(2)
    #     driver.find_element_by_id("com.bikroy:id/main_bottom_panel_search").click()
    #     sleep(2)
    #     driver.find_element_by_id("com.bikroy:id/main_bottom_panel_chat").click()
    #     sleep(2)
    #     driver.find_element_by_id("com.bikroy:id/main_bottom_panel_my_account").click()
    #     sleep(10)
