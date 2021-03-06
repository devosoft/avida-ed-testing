from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from utilities.simple_web_server import CustomWebServer
from base.config import Configuration

from os import path, getcwd, makedirs

class WebDriverFactory:
    """
     Class that handles instantiation of a WebDriver object based on browser information. 
     
     Example Usage:
     wdf = WebDriverFactory(browser_type)
     driver = wdf.get_webdriver_instance()
     """

    # Path for downloads to go to
    __dwn_path = path.join(getcwd(), "downloads")
    if not path.exists(__dwn_path):
        makedirs(__dwn_path)

    def __init__(self, browser, is_local, ui_path, ff_path, av_url):
        """
        Initializes a WebDriverFactory object.

        :param browser: The browser that the driver will be used with.

        :param is_local: True if the driver will test a local version of the
        app, False otherwise.

        :param ui_path: The path to the Avida-ED app's lccal files (if running
        locally).

        :param ff_path: The path to the Firefox binary (needed when running with
        FF).

        :param av_url: The URL of a web-hosted version of Avida-ED (needed when
        not running locally).
        """
        self.config = Configuration()
        if ui_path is not None:
            self.config.set_ui_path(ui_path)
        if ff_path is not None:
            self.config.set_ff_path(ff_path)
        if av_url is not None:
            self.config.set_av_url(av_url)
        if browser is None:
            browser = "chrome"
        self.browser = browser.lower()
        if is_local is None or is_local.lower() != "false":
            self.is_local = True
        else:
            self.is_local = False

        self.server = CustomWebServer()

    def get_webdriver_instance(self):
        """
        Get a WebDriver instance based on the browser configuration.
        
        :returns: A WebDriver instance that is ready for testing.
        """
        if self.is_local:
            self.server.run_http_server()
            base_url = "http://127.0.0.1:8000/av_ui/AvidaED.html"
        else:
            base_url = self.config.get_av_url()

        # Instantiate driver using specified browser (defaults to Chrome)
        if self.browser == "firefox":
            binary = FirefoxBinary(self.config.get_ff_path())

            # Set FF preferences up for downloads.
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.download.folderList", 2)
            profile.set_preference("browser.download.manager.showWhenStarting",
                                   False)
            profile.set_preference("browser.download.dir", self.__dwn_path)
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                   "application/zip")

            # Create the driver itself.
            driver = webdriver.Firefox(firefox_binary=binary,
                                       firefox_profile=profile)
        else:
            driver = webdriver.Chrome()

        # Prepare driver for use -- maximize window, go to avida-ED website.
        driver.maximize_window()
        driver.get(base_url)

        return driver

    def clean_webdriver_instance(self):
        """
        Clean up after a driver instance (specifically the web server if running
         locally).

        :return: None.
        """
        if self.is_local:
            self.server.cleanup()
