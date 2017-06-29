from base.base_page import BasePage

import unittest
import pytest

@pytest.mark.usefixtures("one_time_setup")
class AvidaEdTabTest(unittest.TestCase):
    """
    Test class that tests the Avida-ED tab of the main menu bar.
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
    def test_about_page(self):
        """
        Tests that the about page works properly.

        :return: None.
        """
        self.page.open_avida_ed_about()
        assert self.page.avida_ed_about_displayed()
        self.page.close_avida_ed_about()
        assert not self.page.avida_ed_about_displayed()

