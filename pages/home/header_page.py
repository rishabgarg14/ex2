import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from base.webdriverfactory import WebDriverFactory


class HeaderPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _logo = "(//a[starts-with(@class,'w-32')])[1]"
    _find_your_dream_home = "(//button/p[text()='Find Your Dream Home'])[1]"
    _express_your_style = "(//a[starts-with(@href,'/express-your-style')])[1]"
    _make_it_real = "(//a[contains(@href,'/make-it-real')])[1]"
    _experience_mattamy = "(//a[starts-with(@href,'/experience-mattamy')])[1]"
    _country_selector = "(//button[starts-with(@class,'border')])[1]"
    _usa_text = "(//button[text()='USA'])[1]"
    _header_metro = "(//h3[starts-with(@class,'uppercase')])[1]"

    def clickLogo(self):
        self.elementClick(locator=self._logo, locatorType="xpath")

    def clickFindYourDreamHome(self):
        self.elementClick(self._find_your_dream_home, "xpath")

    def clickExpressYourStyle(self):
        self.elementClick(self._express_your_style, "xpath")

    def clickMakeItReal(self):
        self.elementClick(self._make_it_real, "xpath")

    def clickExperienceMattamy(self):
        self.elementClick(self._experience_mattamy, "xpath")

    def clickCountrySelector(self):
        self.elementClick(self._country_selector,"xpath")

    def verifyLogoRedirect(self):
        self.clickLogo()
        attribute = self.getAttribute(locator=self._logo, locatorType="xpath", attribute="href")
        urlAlias = attribute.partition(".com")[2]
        self.log.info("URL alias is "+urlAlias)
        return self.verifyText(urlAlias, "/")

    def verifyFYDHExist(self):
        return self.isElementDisplayed(self._find_your_dream_home, "xpath")

    def verifyFYDHElement(self):
        self.clickFindYourDreamHome()
        return self.isElementDisplayed(self._header_metro, "xpath")

    def verifyExpressYourStyleRedirect(self):
        self.clickExpressYourStyle()
        urlAlias = self.findUrlAlias()
        return self.verifyText(urlAlias, "/express-your-style")

    def verifyMakeItRealRedirect(self):
        self.clickMakeItReal()
        urlAlias = self.findUrlAlias()
        return self.verifyText(urlAlias, "/make-it-real")

    def verifyExperienceMattamyRedirect(self):
        self.clickExperienceMattamy()
        urlAlias = self.findUrlAlias()
        return self.verifyText(urlAlias, "/experience-mattamy")

    def verifyToggleClick(self):
        oldAttribute = self.getAttribute(self._usa_text, "xpath", "class")
        newValue = ""
        self.clickCountrySelector()
        newAttribute = self.getAttribute(self._usa_text, "xpath", "class")

        if "text-action-blue" in oldAttribute:
            if "text-mattamy-gray" in newAttribute:
                self.log.info("Toggle is working fine")
                return True
            else:
                self.log.info("Toggle didn't work")
                return False
        elif "text-mattamy-gray" in oldAttribute:
            if "text-action-blue" in newAttribute:
                self.log.info("Toggle is working fine")
                return True
            else:
                self.log.info("Toggle didn't work")
                return False
        else:
            self.log.info("Toggle didn't work")
            return False






