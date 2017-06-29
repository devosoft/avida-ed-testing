from base.base_page import BasePage

import unittest
import pytest
import time

@pytest.mark.usefixtures("one_time_setup")
class SimpleExperimentTest(unittest.TestCase):
    """
    Test class that runs a very simple experiment in Avida-ED.
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
    def test_simple_exp(self):
        """
        Tests that the about page works properly.

        :return: None.
        """
        self.page.click_freezer_item("@ancestor")
        self.page.add_org_to_exp()
        self.page.do_one_update()
        time.sleep(3)
