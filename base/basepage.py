"""
@package base

Base Page class implementation
It implements methods which are common to all the pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Example:
    Class loginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        Inits BasePage class
        Returns: None
        """
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page title
        :param
        titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def verifyPageUrl(self, urlToVerify):
        try:
            actualUrl = self.getUrl()
            return self.util.verifyTextMatch(actualUrl, urlToVerify)
        except:
            self.log.error("Failed to get page URL")
            print_stack()
            return False

    def verifyText(self, actualText, expectedText):
        try:
            return self.util.verifyTextMatch(actualText, expectedText)
        except:
            self.log.error("Failed to match text")
            print_stack()
            return False

    def verifyTextContains(self, actualText, expectedText):
        try:
            return self.util.verifyTextContains(actualText, expectedText)
        except:
            self.log.error("Failed to find text")
            print_stack()
            return False

    def findUrlAlias(self):
        url = self.getUrl()
        urlAlias = url.split(".com")[1]
        return urlAlias
