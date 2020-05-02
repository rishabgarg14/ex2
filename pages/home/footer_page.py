import time

import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class FooterPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    #Locators
    _facebook_social_icon = "//a[contains(@href,'facebook')]"
    _insta_social_icon = "//a[contains(@href,'instagram')]"
    _pinterest_social_icon = "//a[contains(@href,'pinterest')]"
    _linkedin_social_icon = "//a[contains(@href,'linkedin')]"
    _youtube_social_icon = "//a[contains(@href,'youtube')]"
    _homeowners_link = "//a[text()='Homeowners']"
    _faq_link = "FAQ"
    _email_signup_link = "Email Signup"
    _contact_us_link = "Contact Us"
    _careers_link = "Careers"
    _media_link = "For Media"
    _realtors_link = "For Realtors"
    _investors_link = "Investors"
    _privacy_link = "Privacy Policy"
    _tnc_link = "Terms & Conditions"
    _accessibility_link = "Accessibility"
    _copyright_text = "//*[contains(text(),'©2')]/../span"

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def scrollToFooter(self):
        element = self.getElement(self._facebook_social_icon, "xpath")
        self.webScroll(element=element)
        self.log.info("Scrolled down to footer")

    def getFacebookIconStatus(self):
        return self.verifyURLStatus(locator=self._facebook_social_icon, locatorType="xpath")

    def getInstagramIconStatus(self):
        return self.verifyURLStatus(locator=self._insta_social_icon, locatorType="xpath")

    def getPinterestStatus(self):
        return self.verifyURLStatus(locator=self._pinterest_social_icon, locatorType="xpath")

    def getLinkedInIconStatus(self):
        self.elementClick(locator=self._linkedin_social_icon, locatorType="xpath")
        url = self.getUrl()
        result = self.verifyTextContains(url, "https://www.linkedin.com/")
        self.driver.back()
        return result

    def getYoutubeIconStatus(self):
        return self.verifyURLStatus(locator=self._youtube_social_icon, locatorType="xpath")

    def getHomeownersLinkStatus(self):
        self.log.info("Verifying Homeowners Link in the footer")
        return self.verifyURLStatus(locator=self._homeowners_link, locatorType="xpath")


