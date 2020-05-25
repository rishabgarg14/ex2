import logging
import os
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as co
from selenium.webdriver.firefox.options import Options as fo
# from shutil import which
import utilities.custom_logger as cl
from selenium import webdriver


class WebDriverFactory:
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, browser, url):
        """
        Initiates WebDriverFactory class

        Returns:
            none
        """
        self.browser = browser
        self.baseUrl = url
        currentDirectory = os.path.dirname(__file__)
        driverDirectory = "../Drivers"
        self.browserDirectory = os.path.join(currentDirectory, driverDirectory)
        self.log.debug("Browser directory" + self.browserDirectory)

    """
    Set chrome driver and iexplorer environment based on os
    
    PREFERRED: Set the path on the machine where browser will be executed.
    """

    def getWebDriverInstance(self):
        """
        Get WebDriver instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        if self.browser == "edge":
            edgePath = self.browserDirectory + "\\msedgedriver.exe"
            os.environ["webdriver.edge.driver"] = edgePath
            driver = webdriver.Edge(edgePath)
            self.log.info("Opening Edge Browser")

        elif self.browser == "ff":
            # FIREFOXPATH = which("firefox")
            # self.log.info("Firefox path is "+str(FIREFOXPATH))
            # options = fo()
            # options.add_argument("-headless") options=options,
            # options.binary = FIREFOXPATH
            ffPath = self.browserDirectory + "\\geckodriver.exe"
            os.environ["webdriver.firefox.driver"] = ffPath
            driver = webdriver.Firefox(executable_path=ffPath)
            self.log.info("Opening Firefox")

        elif self.browser == "chrome":
            chromePath = self.browserDirectory + "\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromePath
            driver = webdriver.Chrome(chromePath)
            self.log.info("Opening Chrome")

        elif self.browser == "headlesschrome":
            opts = co()
            # opts.add_argument("user-agent=MMozilla/5.0 (Windows NT 10.0; Win64; x64) "
            #                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
            opts.add_argument("--headless")
            opts.add_argument("start-maximized")
            opts.add_argument('disable-infobars')
            chromePath = self.browserDirectory + "\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromePath
            driver = webdriver.Chrome(options=opts, executable_path=chromePath)
            agent = driver.execute_script("return navigator.userAgent")
            print("User Agent is: " + agent)
            self.log.info("Opening Headless Chrome")

        else:
            chromePath = self.browserDirectory + "\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromePath
            driver = webdriver.Chrome(executable_path=chromePath)
            self.log.info("Opening Chrome")

        # Setting browser implicit timeout for an element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        self.log.info("Maximizing browser window")
        # Loading browser with desired URL
        driver.get(self.baseUrl)
        self.log.info("Opened Url " + self.baseUrl)
        return driver
