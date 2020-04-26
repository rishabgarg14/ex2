import os
import unittest
from selenium import webdriver
from pages.home.oos_login_page import LoginPage
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("setUp", "oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    def setUp(self):
        self.lp.logout()

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title is verified")
        # assert result1 == False
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login is verified")
        # assert result2 == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("abc@yahoo.com", "ab")
        error = self.lp.verifyLoginFailed()
        assert error == True
