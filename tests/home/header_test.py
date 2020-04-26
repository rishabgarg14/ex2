import os
import time
import unittest
from selenium import webdriver
from pages.home.header_page import HeaderPage
import pytest
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp")
class HeaderTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.hp = HeaderPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_logoRedirect(self):
        result = self.hp.verifyLogoRedirect()
        self.ts.markFinal("test_logoRedirect", result, "logo redirection test case executed")

    @pytest.mark.run(order=2)
    def test_FindYourDreamHomeExist(self):
        result = self.hp.verifyFYDHExist()
        self.ts.markFinal("test_FindYourDreamHomeExist", result, "Verify 'Find Your Dream Home' executed")

    @pytest.mark.run(order=7)
    def test_FindYourDreamHomeDropdownExist(self):
        result = self.hp.verifyFYDHElement()
        self.hp.clickFindYourDreamHome()
        self.ts.markFinal("test_FindYourDreamHomeDropdownExist", result,
                          "Verify that element exist under 'Find Your Dream Home' dropdown executed")

    @pytest.mark.run(order=3)
    def test_expressYourStyleRedirect(self):
        result = self.hp.verifyExpressYourStyleRedirect()
        self.ts.markFinal("test_expressYourStyleRedirect", result,
                          "'Express Your Style' redirection test case executed")

    @pytest.mark.run(order=4)
    def test_makeItRealRedirect(self):
        result = self.hp.verifyMakeItRealRedirect()
        self.ts.markFinal("test_makeItRealRedirect", result,
                          "'Make It real' redirection test case executed")

    @pytest.mark.run(order=5)
    def test_experienceMattamyRedirect(self):
        result = self.hp.verifyExperienceMattamyRedirect()
        self.ts.markFinal("test_experienceMattamyRedirect", result,
                          "'Experience Mattamy' redirection test case executed")

    @pytest.mark.run(order=6)
    def test_countryToggleClick(self):
        result = self.hp.verifyToggleClick()
        self.ts.markFinal("test_countryToggleClickable", result,
                          "Country selector test case executed")
