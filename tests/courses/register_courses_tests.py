import os
import unittest
from selenium import webdriver
from pages.courses.register_courses_page import RegisterCoursesPage
import pytest
from utilities.casestatus import TestStatus

@pytest.mark.usefixtures("setUp", "oneTimeSetUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.rc = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.rc.clickAllCourses()
        self.rc.searchCourse("javascript")
        self.rc.openCourseDetail("JavaScript for beginners")
        self.rc.enrollCourse("5545345785475874", "0123", "343")
        result = self.rc.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Invalid Enrollment Failed")