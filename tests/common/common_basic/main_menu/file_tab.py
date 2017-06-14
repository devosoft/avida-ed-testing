from base.base_page import BasePage

import unittest
import pytest
import time

@pytest.mark.usefixtures("one_time_setup")
class FileTabTest(unittest.TestCase):
    """
    Test class that tests the File tab of the main menu bar.
    """

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        """
        Sets up the class before the tests run.

        :param one_time_setup: Necessary parameter
        for the running of the one_time_setup Pytest fixture. DO NOT REMOVE.

        :return: None.
        """
        self.page = BasePage(self.driver)

    @pytest.mark.run()
    def test_export_graphics(self):
        """
        Tests that the "Export Graphics" option in the File tab works as
        expected.

        :return: None.
        """
        assert not self.page.export_graphics_dialog_displayed()
        self.page.export_graphics()
        assert self.page.export_graphics_dialog_displayed()
        self.page.close_export_graphics_dialog()
        assert not self.page.export_graphics_dialog_displayed()
