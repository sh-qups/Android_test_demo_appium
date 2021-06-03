from Pages.base_page import BasePage
from Utils.locators import IntroPageLocator, HomePageLocator
from time import sleep
import allure

class IntroPage(BasePage):

    def __init__(self, driver):
        self.locator = IntroPageLocator
        self.locatorHomepage = HomePageLocator
        super().__init__(driver)

    def go_to_home(self):
        driver = self.driver
        sleep(2)
        driver.find_element_by_xpath(self.locator.language).click()
        sleep(2)
        driver.find_element_by_id(self.locator.maybe_latter).click()
        sleep(2)
        driver.find_element_by_id(self.locator.location_permission_this_time).click()
        sleep(20)

    @allure.step('test_intro_to_home')
    def test_intro_to_home(self):
        self.go_to_home()
        pass
        # element = driver.find_element_by_xpath(self.locatorHomepage.location)
        # res = element.text
        # print(res)
        # print("element found in homepage: " + res)
        # assert res == 'Location'
