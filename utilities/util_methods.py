import time
import logging

from utilities.custom_logger import create_custom_logger


class UtilityMethods(object):
    """
    Class that contains common methods for use across the project but does not
    interact directly with the driver interface.
    
    Mostly used to wrap common common methods in with the logging infrastructure.
    """

    log = create_custom_logger(logging.INFO)

    def sleep(self, seconds_to_sleep=1, info=None):
        """
        Forces the program to idle for a certain amount of time.
        
        :param seconds_to_sleep: The time in seconds that the program should 
        idle.
        
        :param info: An optional reason for the idle, which will be logged if 
        provided.
        
        :return: None.
        """
        if info is not None:
            self.log.info("Attempting to wait " + str(seconds_to_sleep)
                          + " seconds for " + info + ".")
        else:
            self.log.info("Attempting to wait " + str(seconds_to_sleep)
                          + "seconds.")
        try:
            time.sleep(seconds_to_sleep)
            self.log.info("Wait successful.")
        except InterruptedError:
            self.log.info("Wait unsuccessful.")

    def verify_text_contains(self, actual_text="", expected_text=""):
        """
        Verify that a string contains another string.
        
        :param actual_text: The text that we are examining.
        
        :param expected_text: The text that we are trying to find within the
        actual text.
        
        :return: True if expected_text is found within actual_text, false
        otherwise.
        """

        self.log.info("Attempting to verify that actual text '" + actual_text
                      + "' contains expected text '" + expected_text + "'.")
        if expected_text.lower() in actual_text.lower():
            self.log.info("Actual text contained expected text.")
            return True
        else:
            self.log.info("Actual text did not contain expected text.")
            return True

    def verify_text_matches(self, actual_text="", expected_text=""):
        """
        Verify that two strings match.
        
        :param actual_text: The actual text received from the website.
        
        :param expected_text: The text that we expect the website text to match.
        
        :return: True if strings match, false otherwise.
        """

        self.log.info("Attempting to verify that actual text '" + actual_text
                      + "' matches expected text '" + expected_text + "'.")
        if expected_text.lower() == actual_text.lower():
            self.log.info("Actual text matched expected text.")
            return True
        else:
            self.log.info("Actual text did not match expected text.")
            return False
