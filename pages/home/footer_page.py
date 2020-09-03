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
    _homeowners_link = "Homeowners"
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
        self.elementClick(locator=self._insta_social_icon, locatorType="xpath")
        url = self.getUrl()
        result = self.verifyTextContains(url, "https://www.instagram.com/mattamyhomes/")
        self.driver.back()
        return result

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
        return self.verifyURLStatus(locator=self._homeowners_link, locatorType="link")

    def getFAQLinkStatus(self):
        return self.verifyURLStatus(locator=self._faq_link, locatorType="link")

    def getEmailSignupLinkStatus(self):
        return self.verifyURLStatus(locator=self._email_signup_link, locatorType="link")

    def getContactUsLinkStatus(self):
        return self.verifyURLStatus(locator=self._contact_us_link, locatorType="link")

    def getCareersLinkStatus(self):
        return self.verifyURLStatus(locator=self._careers_link, locatorType="link")

    def getForMediaLinkStatus(self):
        return self.verifyURLStatus(locator=self._media_link, locatorType="link")

    def getForRealtorsLinkStatus(self):
        return self.verifyURLStatus(locator=self._realtors_link, locatorType="link")

    def getInvestorsLinkStatus(self):
        return self.verifyURLStatus(locator=self._investors_link, locatorType="link")

    def getPrivacyLinkStatus(self):
        return self.verifyURLStatus(locator=self._privacy_link, locatorType="link")

    def getTnCLinkStatus(self):
        return self.verifyURLStatus(locator=self._tnc_link, locatorType="link")

    def getAccessibilityLinkStatus(self):
        return self.verifyURLStatus(locator=self._accessibility_link, locatorType="link")

    def getCopyrightTextStatus(self):
        cpText = self.getElementList(self._copyright_text, "xpath")
        if len(cpText) == 3:
            self.log.info("Entire Copyright Text is present")
            return True
        else:
            self.log.error("Copyright text is not as per expectation")
            return False



