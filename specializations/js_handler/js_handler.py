import logging

from base.base_page import BasePage
from utilities.util_methods import UtilityMethods
from utilities.custom_logger import create_custom_logger


class JSHandler(BasePage):
    """
    Specialization of the BasePage that is specialized to tasks that require
    executing Javscript code on the webpage.
    """

    log = create_custom_logger(logging.DEBUG)
    util = UtilityMethods()

    def __init__(self, driver):
        """
        Sets up the page for use at initialization.

        :param driver: The driver that interacts with the actual page.
        """
        super().__init__(driver)
        self.driver = driver

    def get_current_update(self):
        """
        Gets the current update from av.grd.updateNum.

        :return: Integer value of current update.
        """
        return self.execute_script("return av.grd.updateNum")
