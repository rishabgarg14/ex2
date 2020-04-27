"""
@package utilities

Checkpoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test name", result, ""Message")
"""
import logging
import time
import allure
from allure_commons.types import AttachmentType
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl


class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        """
        Inits Checkpoint class
        """
        # super(TestStatus, self).__init__(driver)
        super().__init__(driver)
        self.resultList = []
        self.driver = driver

    def setResult(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info(" ### Verification Pass :: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.info(" ### Verification FAIL :: " + resultMessage)
                    self.screenShot(resultMessage)
                    allure.attach(self.driver.get_screenshot_as_png(),
                                  name=resultMessage + "." + str(round(time.time() * 1000)),
                                  attachment_type=AttachmentType.PNG)
            else:
                self.resultList.append("FAIL")
                self.screenShot(resultMessage)
                allure.attach(self.driver.get_screenshot_as_png(),
                              name=resultMessage + "." + str(round(time.time() * 1000)),
                              attachment_type=AttachmentType.PNG)
                self.log.error(" ### Verification FAIL :: " + resultMessage)
        except:
            self.resultList.append("FAIL")
            self.screenShot(resultMessage)
            allure.attach(self.driver.get_screenshot_as_png(),
                          name=resultMessage + "." + str(round(time.time() * 1000)),
                          attachment_type=AttachmentType.PNG)
            self.log.error(" ### Exception Occurred !!! ")

    def mark(self, result, resultMessage):
        """
        Mark the result of verification point in a test case
        """
        self.setResult(result, resultMessage)

    def markFinal(self, testName, result, resultMessage):
        """
        Mark the final result of verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + " Test Failed")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + " Test Passed")
            self.resultList.clear()
            assert True == True
