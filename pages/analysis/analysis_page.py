import logging

from base.base_page import BasePage
from utilities.custom_logger import create_custom_logger


class AnalysisPage(BasePage):
    """
    Specialization of the BasePage that allows use of the Analysis page within
    the Avida-ED website.
    """

    log = create_custom_logger(logging.DEBUG)
