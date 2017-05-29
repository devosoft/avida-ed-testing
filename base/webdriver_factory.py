from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class WebDriverFactory:
    """
     Class that handles instantiation of a WebDriver object based on browser information. 
     
     Example Usage:
     wdf = WebDriverFactory(browser_type)
     driver = wdf.get_webdriver_instance()
     """
    def __init__(self, browser):
        """ Inits a WebDriverFactory class """

        self.browser = browser

    def get_webdriver_instance(self):
        """
        Get a WebDriver instance based on the browser configuration.
        
        :returns: A WebDriver instance that is ready for testing.
        """

        base_url = "https://avida-ed.beacon-center.org/appTest/AvidaED.html"

        # Instantiate driver using specified browser (defaults to Chrome)
        if self.browser == "firefox":
            binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
            driver = webdriver.Firefox(firefox_binary=binary)
        else:
            driver = webdriver.Chrome()

        # Prepare driver for use -- maximize window, go to avida-ED website.
        driver.maximize_window()
        driver.get(base_url)

        # Wait for splash screen to go away
        WebDriverWait(driver, 60)\
            .until(ec.invisibility_of_element_located(('id', 'splash')))

        return driver
