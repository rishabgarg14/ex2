# from selenium.webdriver.common.by import By
# from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//a[@href='/sign_in']"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _user_icon = "//li[contains(@class,'dropdown')]//img"
    _logout_link = "//a[@href='/sign_out']"
    _error_message = "//div[contains(@class,'alert')]"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    def clickLoginLink(self):
        self.elementClick(self._login_link, "xpath")

    def enterEmail(self, email):
        #self.clearElement(self._email_field)
        self.sendKeys(email, self._email_field)

    def clearEmail(self):
        self.elementClear(self._email_field)

    def enterPassword(self, password):
        #self.clearElement(self._password_field)
        self.sendKeys(password, self._password_field)

    def clearPassword(self):
        self.elementClear(self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, "name")

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearEmail()
        self.log.info("Entering email: "+email)
        self.enterEmail(email)
        self.clearPassword()
        self.log.info("Entering password: " + password)
        self.enterPassword(password)
        self.clickLoginButton()

    def logout(self):
        self.elementClick(self._user_icon, "xpath")
        self.elementClick(self._logout_link, "xpath")

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._user_icon, "xpath")
        return result

    def verifyLoginFailed(self):
        error = self.isElementPresent(self._error_message, "xpath")
        return error

    def verifyTitle(self):
        return self.verifyPageTitle("Let's Kode It")

