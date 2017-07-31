import time
import os
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utilities.custom_logger import create_custom_logger


class DriverWrapper:
    """
    Class that creates a wrapper for the Selenium WebDriver.
    
    This wrapper provides methods for manipulating the driver and other common
    tasks that are more specific to this application of the driver.
    """
    log = create_custom_logger(logging.DEBUG)

    def __init__(self, driver):
        """ Initializes a DriverWrapper object. """
        self.driver = driver

    def send_keys(self, my_locator="", locator_type="id", element=None, keys=""):
        """
        Sends keyboard input to an element.
        
        If the element is specified (in the element param), the input will be
        sent to that element.
        
        If the element is not specified, the input will be sent to the first
        element found that matches the locator and type given.
        
        :param my_locator: A string containing the locator that will be searched
        for.
        
        :param locator_type: A string representing the type of locator that 
        my_locator is. Can be an id, a class name, link text, XPATH, CSS
        selector, or name.
        
        :param element: The element that will receive the input.
        
        :param keys: A string containing the keys that should be sent to the
        element.
        
        :return: None.
        """

        try:
            if element is None:
                element = self.__get_element(my_locator, locator_type)
            element.send_keys(keys)
            self.log.info("Input '" + keys + "' sent to element with locator "
                          + my_locator + " of type " + locator_type)
        except:
            self.log.info("Failed to send input '" + keys
                          + "'sent to element with locator " + my_locator
                          + " of type " + locator_type)

    def get_text(self, my_locator="", locator_type="id", element=None):
        """
        Gets text from an on-screen element.
        
        If the element is specified (in the element param), the text from that
        method will be returned.
        
        If the element is not specified, the text from the first element found
        that matches the locator and type given.
        
        :param my_locator: A string containing the locator that will be searched
        for if element is not specified.
        
        :param locator_type: A string representing the type of locator that
         my_locator is. Can be an id, a class name, link text, XPATH, CSS
         selector, or name.
         
        :param element: The element that is to be clicked. If this is None,
        it will be set equal to the first found by searching with my_locator and
        locator_type.
        
        :return: String containing the text from the chosen element.
        """
        text = None
        try:
            if element is None:
                element = self.__get_element(my_locator, locator_type)
            text = element.text
            text = text.strip()
            self.log.info("Got text '" + text + "' from element with locator "
                          + my_locator + " of type " + locator_type + ".")

        except:
            self.log.info("Unable to get text from element with locator "
                          + my_locator + " of type " + locator_type + ".")
        return text

    def take_screenshot(self, description):
        """
        Takes a screenshot of the webpage that is currently open.
    
        :param description: A description that will become part of the filename
        of the screenshot.
        
        :return: None 
        """
        file_name = description + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory,
                                             screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot taken. Saved at directory "
                          + destination_directory + ".")
        except:
            self.log.info("Attempt to take screenshot failed.")

    ############################################################################
    # Methods below this point should not be used outside this class or its
    # direct descendants.
    ############################################################################

    def __get_title(self):
        """
        Gets the title of the page the WebDriver is currently on.

        :return: Title of the page.
        """
        return self.driver.title

    def __get_by_type(self, locator_type):
        """
        Finds a locator type from within the By class that corresponds to the
        type of locator specified in the input.

        :param locator_type: A string representing the locator type will be used
        for locating an element.

        :return: An object from within the By class if locator_type is valid,
        else returns False.
        """
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type + " not supported.")
        return False

    def __get_element(self, my_locator, locator_type="id"):
        """
        Attempts to get an element on the webpage from the driver.

        :param my_locator: A string containing the locator that will be searched
        for. The driver will search the HTML using this locator.

        :param locator_type: A string representing the type of locator that
        my_locator is. Can be an id, a class name, link text, XPATH, CSS
        selector, or name.

        :return: The first element that is found when searching using the given
        locator and locator type. Returns None if no matching element is found.
        """
        element = None

        try:
            locator_type = locator_type.lower()
            by = self.__get_by_type(locator_type)
            element = self.driver.find_element(by, my_locator)
            self.log.info("Element found with locator " + my_locator
                          + " of type " + locator_type + ".")

        except:
            self.log.info("Element with locator " + my_locator
                          + " of type " + locator_type + " not found.")

        return element

    def __get_element_list(self, my_locator, locator_type="id"):
        """
        Attempts to get a group of elements on the webpage from the driver.

        :param my_locator: A string containing the locator that will be searched
        for. The driver will search the HTML using this locator.

        :param locator_type: A string representing the type of locator that
        my_locator is. Can be an id, a class name, link text, XPATH, CSS
        selector, or name.

        :return: A list containing all of the elements found when searching
        using the given locator and locator type. Returns None if no matching
        element is found.
        """

        elements = None

        try:
            locator_type = locator_type.lower()
            by = self.__get_by_type(locator_type)
            elements = self.driver.find_elements(by, my_locator)
            self.log.info("List of " + str(len(elements))
                          + " elements found with locator " + my_locator
                          + " of type " + locator_type + " found.")

        except:
            self.log.info("No elements with locator " + my_locator + " of type "
                          + locator_type + " found.")

        return elements

    def __click_element(self, my_locator="", locator_type="id", element=None):
        """
        Clicks on an element.

        If the element is specified (in the element param), that element will
        be clicked.

        If the element is not specified, we will search for a matching element
        with the locator and type provided.

        :param my_locator: A string containing the locator that will be searched
        for.

        :param locator_type: A string representing the type of locator that
        my_locator is. Can be an id, a class name, link text, XPATH, CSS
        selector, or name.

        :param element: The element that will be clicked -- either none,
        implying we have to use the locators, or some element that will be
        clicked, bypassing the search.

        :return: None.
        """
        try:
            if element is None:
                element = self.__get_element(my_locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator " + my_locator
                          + " of type " + locator_type + ".")

        except:
            self.log.info("Failed to click on any element with locator "
                          + my_locator + " of type " + locator_type + ".")

    def __element_present(self, my_locator="", locator_type="id"):
        """
        Checks if an element is present on the page the driver is on.

        It will check for any elements that can be found with the locator
        my_locator of type locator_type.

        :param my_locator: A string containing the locator that will be searched
        for.

        :param locator_type: A string representing the type of locator that
        my_locator is. Can be an id, a class name, link text, XPATH, CSS
        selector, or name attribute.

        :return: True if the element is present -- false otherwise.
        """

        try:
            element = self.__get_element(my_locator, locator_type)
            if element is not None:
                self.log.info("Element with locator " + my_locator
                              + " of type " + locator_type
                              + " found to be present.")
                return True
            else:
                self.log.info("Element with locator " + my_locator
                              + " of type " + locator_type
                              + " not found to be present.")
                return False

        except:
            return False

    def __element_displayed(self, my_locator="",
                            locator_type="id",
                            element=None):
        """
        Checks if an element is displayed on the web page.

        If element is specified (via element param), we will check that exact
        element.

        If the element is not specified, we will check whether the first
        element that matches the locator is displayed.

        :param my_locator: A string containing the locator that will be used
        to conduct the search if the element is not specified.

        :param locator_type: A string representing the type of locator that
        my_locator is. Can be an id, a class name, link text, XPATH, CSS
        selector, or name attribute.

        :param element: The element which we will be examining.

        :return: True if the element is displayed -- false otherwise.
        """
        is_displayed = False
        try:
            if element is None:
                element = self.__get_element(my_locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
            if is_displayed:
                self.log.info("Element with locator " + my_locator
                              + " of type " + locator_type
                              + " found to be displayed.")
            else:
                self.log.info("Element with locator " + my_locator
                              + " of type " + locator_type
                              + " found not to be displayed.")
            return is_displayed
        except:
            self.log.info("Error occurred trying to find element with locator "
                          + my_locator + " of type " + locator_type)
            return False

    def __element_has_class(self, my_locator="",
                            locator_type="id",
                            class_name="",
                            element=None):
        """
        Determines whether the specified element is of class class_name.

        :param my_locator: Locator used to find the element on the site.

        :param locator_type: Type of locator that my_locator is; could be a ID,
        CSS selector, etc.

        :param class_name: Name of the class that we are looking for in the list
        of classes that have been applied to the element.

        :param element: Optional argument for an element that has already been
        located.

        :return: True if the specified element exists and class class_name has
        been applied to the element; False otherwise.
        """
        if element is None:
            element = self.__get_element(my_locator, locator_type)
        if element is not None:
            class_list = element.get_attribute("class")
            if class_list is not None and class_name in class_list:
                return True
        return False

    def __execute_script(self, script_text):
        """
        Executes arbitrary Javascript code to interact with the page.

        :param script_text: The Javascript code to be executed.

        :return: None.
        """

        try:
            value = self.driver.execute_script(script_text)
            self.log.info("Run Javascript code: '" + script_text + "'.")
            return value
        except:
            self.log.info("Attempt to run Javascript code failed.")

    def __switch_to_alert(self):
        """
        Allows interaction with Javscript alerts.

        :return: Object that allows interaction with the alert.
        """
        return self.driver.switch_to.alert

    def __wait_until_invisible(self, my_locator="", locator_type="id"):
        """
        Use WebdriverWait to wait until an element is no longer visible on the
        screen.

        :return: None.
        """
        WebDriverWait(self.driver, 60) \
            .until(ec.invisibility_of_element_located((locator_type,
                                                       my_locator)))

    def __refresh_page(self):
        """
        Refreshes the page.

        :return: None.
        """
        self.driver.refresh()
