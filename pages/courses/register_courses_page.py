import time

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _search_box = "//input[@id='search-courses']"
    _search_button = "search-course-button"
    _course = "//div[contains(@class, 'course-listing-title') and contains(text(),'{0}')]"
    _all_courses = "//a[contains(text(),'All Courses')]"
    _enroll_button = "//button[@id='enroll-button-top']"
    _cc_num = "//input[@name='cardnumber' and starts-with(@class, 'Input')]"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvv = "//input[@name='cvc']"
    _agree_checkbox = "//input[@type='checkbox' and contains(@id,'agree')]"
    _submit_enroll = "confirm-purchase"
    _enroll_error_message = "//span[contains(text(),'The card')]"

    def clickAllCourses(self):
        self.elementClick(self._all_courses, "xpath")
        self.log.info("Clicked on All Courses link")

    def searchCourse(self, text):
        self.sendKeys(text, self._search_box, "xpath")
        self.clickSearch()

    def clickSearch(self):
        self.elementClick(self._search_button, "id")

    def openCourseDetail(self, courseName):
        self.elementClick(self._course.format(courseName), "xpath")

    def clickEnrollButton(self):
        self.elementClick(self._enroll_button, "xpath")

    def scrollDown(self):
        self.webScroll("down")

    def enterCardNum(self, num):
        self.sendKeys(num, self._cc_num, "xpath")


    def enterExpiry(self, exp):
        self.sendKeys(exp, self._cc_exp)

    def enterCVV(self, cvv):
        self.sendKeys(cvv, self._cc_cvv)

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterExpiry(exp)
        self.enterCVV(cvv)

    def agreeTerms(self):
        self.elementClick(self._agree_checkbox, "xpath")

    def submitEnroll(self):
        self.elementClick(self._submit_enroll, "xpath")

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickEnrollButton()
        time.sleep(3)
        self.scrollDown()
        time.sleep(3)
        self.enterCreditCardInformation(num, exp, cvv)
        self.agreeTerms()
        self.submitEnroll()

    def verifyEnrollFailed(self):
        error = self.isElementDisplayed(self._enroll_error_message, "xpath")
        return error









