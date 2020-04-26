import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class HomePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _logo = "//img[@alt='Logo']"

    def clickLogo(self):
        self.elementClick(self._logo, "xpath")
