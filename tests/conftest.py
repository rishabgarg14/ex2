import pytest
import utilities.custom_logger as cl
import logging
from base.webdriverfactory import WebDriverFactory
from base.selenium_driver import SeleniumDriver
from Data.config import Config

log = cl.customLogger(logging.DEBUG)

@pytest.yield_fixture()
def setUp():
    print("--Started executing test case--")
    yield
    print("--Completed executing this test case--")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    conf = Config()
    url = conf.base_url
    wdf = WebDriverFactory(browser, url)
    driver = wdf.getWebDriverInstance()
    sd = SeleniumDriver(driver)
    sd.elementClick("(//button[text()='USA'])[3]", "xpath")
    log.info("Clicked USA as country")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    log.info("Closing Browser")
    driver.quit()
    log.info("Browser Closed")


def pytest_addoption(parser):
    parser.addoption("--browser", help="Tells the browser in which u r running the tests")
    # parser.addoption("--os")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


# @pytest.fixture(scope="session")
# def osType(request):
# return request.config.getoption("--os")

"""def pytest_sessionfinish(session, exitstatus):"""
"""Whole Session Ended"""
