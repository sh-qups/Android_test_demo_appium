from Pages.base_page import BasePage
from Pages.intro_page import IntroPage
from Utils.locators import *
from time import sleep
import allure


class HomePage(BasePage):

    def __init__(self, driver):
        self.locator = HomePageLocator
        self.locatorLocationPage = LocationPageLocator
        self.locatorCategoryPage = CategoryPageLocator
        self.locatorFilterPage = FilterPageLocator
        self.locatorSearchPage = SearchPageLocator
        self.locatorChatsPage = ChatsPageLocator
        self.locatorAccountPage = AccountPageLocator
        self.locatorLoginPage = LoginPageLocator
        self.locatorSignupPage = SignupPageLocator
        self.locatorForgotPasswordPage = ForgotPasswordPageLocator
        super().__init__(driver)

    def go_to_home_page(self):
        page = IntroPage(self.driver)
        page.go_to_home()

    def login(self):
        email = ''
        password = ''
        driver = self.driver
        driver.find_element_by_xpath(self.locatorLoginPage.email).click()
        sleep(2)
        driver.find_element_by_xpath(self.locatorLoginPage.email_input).send_keys(email)
        sleep(2)
        driver.find_element_by_xpath(self.locatorLoginPage.password_input).send_keys(password)
        sleep(2)
        driver.find_element_by_xpath(self.locatorLoginPage.login).click()

    def signup(self):
        name = 'shashwata'
        email = ''
        password = ''
        driver = self.driver
        driver.find_element_by_xpath(self.locatorLoginPage.email).click()
        sleep(2)
        driver.find_element_by_xpath(self.locatorLoginPage.signup).click()
        sleep(2)
        driver.find_element_by_xpath(self.locatorSignupPage.name_input).send_keys(name)
        sleep(2)
        driver.find_element_by_xpath(self.locatorSignupPage.email_input).send_keys(email)
        sleep(2)
        driver.find_element_by_xpath(self.locatorSignupPage.password_input).send_keys(password)
        sleep(2)
        driver.find_element_by_xpath(self.locatorSignupPage.password_again_input).send_keys(password)
        sleep(2)
        driver.find_element_by_xpath(self.locatorSignupPage.signup).click()
        sleep(2)

    @allure.step('test_set_location')
    def test_set_location(self):

        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_xpath(self.locator.location).click()
        sleep(2)
        driver.find_element_by_id(self.locatorLocationPage.user_location).click()
        sleep(4)
        driver.find_element_by_id(self.locatorLocationPage.all_location).click()
        sleep(2)

    @allure.step('test_set_category')
    def test_set_category(self):

        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_id(self.locator.category).click()
        sleep(2)
        driver.find_element_by_id(self.locatorCategoryPage.category_all).click()
        sleep(4)

    @allure.step('test_filter')
    def test_filter(self):

        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_id(self.locator.filter).click()
        sleep(2)
        driver.find_element_by_xpath(self.locatorFilterPage.sort_by).click()
        sleep(4)
        driver.find_element_by_xpath(self.locatorFilterPage.sort_by_low_to_hi).click()
        sleep(4)
        driver.find_element_by_xpath(self.locatorFilterPage.Type_of_poster).click()
        sleep(4)
        driver.find_element_by_xpath(self.locatorFilterPage.authorize_dealler).click()
        sleep(4)
        driver.find_element_by_id(self.locatorFilterPage.apply_filter).click()
        sleep(4)

    @allure.step('test_switch')
    def test_switch(self):

        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_id(self.locator.filter_switch).click()
        sleep(2)

    @allure.step('test_search')
    def test_search(self):
        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_id(self.locator.search).click()
        sleep(2)
        driver.find_element_by_id(self.locatorSearchPage.search_main).click()
        sleep(4)
        driver.find_element_by_id(self.locatorSearchPage.search_category_selected).click()
        sleep(4)
        driver.find_element_by_xpath(self.locatorSearchPage.popular_search_1).click()
        sleep(4)

    @allure.step('test_chats')
    def test_chats(self):
        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_id(self.locator.chat).click()
        sleep(2)
        self.go_back()
        sleep(4)

    @allure.step('test_account')
    def test_account(self):
        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_id(self.locator.account).click()
        sleep(2)
        self.go_back()
        sleep(4)

    @allure.step('test_click_add')
    def test_click_add(self):
        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_id(self.locator.first_add).click()
        sleep(4)
        self.go_back()
        sleep(4)

    @allure.step('test_post_add')
    def test_post_add(self):
        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_id(self.locator.add_post_plus_sign).click()
        sleep(4)
        self.login()
        sleep(4)

        # TODO: post an add

    @allure.step('test_login')
    def test_login(self):
        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_id(self.locator.add_post_plus_sign).click()
        sleep(4)
        self.login()
        sleep(4)

    @allure.step('test_forgot_password')
    def test_forgot_password(self):
        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_id(self.locator.add_post_plus_sign).click()
        sleep(4)
        self.login()
        sleep(4)

    @allure.step('test_signup')
    def test_signup(self):
        self.go_to_home_page()
        driver = self.driver
        driver.find_element_by_id(self.locator.add_post_plus_sign).click()
        sleep(4)
        self.signup()
        sleep(4)
        self.go_back()
        self.go_back()
        sleep(4)
