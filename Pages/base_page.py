
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

class BasePage(object):

    def __init__(self, driver, base_url="about:blank"):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def go_back_custom(self):
        self.driver.back()

    def implicit_wait_custom(self, seconds):
        self.driver.implicitly_wait(seconds)

    def element_exist_or_not_custom(self):
        try:
            return
        except:
            print('element not found')

    def scroll_to_element_custom(self,element):
        # from appium.webdriver.common.touch_action import TouchAction
        actions = TouchAction(self.driver)
        actions.scroll_from_element(element, 10, 100)
        actions.scroll(10, 100)
        actions.perform()

    def single_tap_custom(self, element):
        actions = TouchAction(self.driver)
        actions.tap(element)
        actions.perform()

    def double_tap_custom(self, element):
        actions = TouchAction(self.driver)
        actions.double_tap(element)
        actions.perform()

    # Long tap
    def double_tap_custom(self, element):
        actions = TouchAction(self.driver)
        actions.long_press(element)
        actions.perform()

    # Finger move on the screen
    def move_to_custom(self, element):
        actions = TouchAction(self.driver)
        actions.tap_and_hold(element)
        actions.move_to(element, 50, 50)
        actions.perform()

    # Finger down on the screen
    def touch_down_custom(self, element):
        actions = TouchAction(self.driver)
        actions.tap_and_hold(element)
        actions.move(50, 50)
        actions.perform()

    # Finger down on the screen
    def touch_up_custom(self, element):
        actions = TouchAction(self.driver)
        actions.tap_and_hold(20, 20)
        actions.release(50, 50)
        actions.perform()

    # Flick on the touch screen using finger motion events
    def flick_custom_custom(self,element):
        actions = TouchAction(self.driver)
        actions.flick_element(element, 1, 10, 10)
        actions.perform()

    # Perform a multi touch action sequence
    def multi_touch_custom(self,element):
        # from appium.webdriver.common.multi_action import MultiAction
        a1 = TouchAction()
        a1.press(10, 20)
        a1.move_to(10, 200)
        a1.release()

        a2 = TouchAction()
        a2.press(10, 10)
        a2.move_to(10, 100)
        a2.release()

        ma = MultiAction(self.driver)
        ma.add(a1, a2)
        ma.perform()

        # Perform a touch action sequence
        def flick_custom_custom(self, element):
            actions = TouchAction(self.driver)
            actions.tap_and_hold(20, 20)
            actions.move_to(10, 100)
            actions.release()
            actions.perform()

        # def find_element(self, *locator):
            #     return self.driver.find_element(*locator)


            # def find_elements(self, *locator):
            #     return self.driver.find_elements(*locator)
            #
            # def open(self, url):
            #     url = self.base_url + url
            #     self.driver.get(url)
            #
            # def get_title(self):
            #     return self.driver.title
            #
            # def get_url(self):
            #     return self.driver.current_url
            #
            # def refresh(self):
            #     return self.driver.refresh()
            #
            # def hover(self, *locator):
            #     element = self.find_element(*locator)
            #     hover = ActionChains(self.driver).move_to_element(element)
            #     hover.perform()
            #
            # def wait_element(self, *locator):
            #     try:
            #         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            #     except TimeoutException:
            #         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            #         self.driver.quit()
            #
            # def wait_element1(self, *locator):
            #     try:
            #         ignored_exceptions = (NoSuchElementException, StaleElementReferenceException )
            #         WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located(locator))
            #     except TimeoutException:
            #         print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" %(locator[1]))
            #         self.driver.quit()