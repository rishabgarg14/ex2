import logging
import os
import utilities.custom_logger as cl
from selenium import webdriver

class WebDriverFactory:

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, browser):
        """
        Initiates WebDriverFactory class

        Returns:
            none
        """
        self.browser = browser
        self.baseUrl = "http://devmh-admin.bhitest.com/"

    """
    Set chrome driver and iexplorer environment based on os
    
    chromedriver = "C:/..../chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    self.driver = webdriver.Chrome(chromedriver)
    
    PREFERRED: Set the path on the machine where browser will be executed.
    """

    def getWebDriverInstance(self):
        """
        Get WebDriver instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        if self.browser == "ie":
            iePath = "C:\\Users\\rgarg\\PycharmProjects\\MattamyHomes\\Drivers\\IEDriverServer.exe"
            os.environ["webdriver.ie.driver"] = iePath
            driver = webdriver.Ie(iePath)
            self.log.info("Opening Internet Explorer")

        elif self.browser =="firefox":
            ffPath = "C:\\Users\\rgarg\\PycharmProjects\\MattamyHomes\\Drivers\\geckodriver.exe"
            os.environ["webdriver.firefox.driver"] = ffPath
            driver = webdriver.Firefox(ffPath)
            self.log.info("Opening Firefox")

        elif self.browser == "chrome":
            chromePath = "C:\\Users\\rgarg\\PycharmProjects\\MattamyHomes\\Drivers\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromePath
            driver = webdriver.Chrome(chromePath)
            self.log.info("Opening Chrome")

        else:
            chromePath = "C:\\Users\\rgarg\\PycharmProjects\\MattamyHomes\\Drivers\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromePath
            driver = webdriver.Chrome(chromePath)
            self.log.info("Opening Chrome")

        # Setting browser implicit timeout for an element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        self.log.info("Maximizing browser window")
        #Loading browser with desired URL
        driver.get(self.baseUrl)
        self.log.info("Opened Url "+self.baseUrl)
        return driver
