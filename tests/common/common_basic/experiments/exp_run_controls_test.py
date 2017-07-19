from base.base_page import BasePage
from specializations.js_handler.js_handler import JSHandler

import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup")
class ExperimentControlsTest(unittest.TestCase):
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
    def test_exp_run_controls(self):
        """
        Tests that a simple experiment can be run and that running, pausing, and
        doing one update work as expected.

        :return: None.
        """
        js_assertions = JSHandler(self.page)

        # Add @ancestor to dish.
        self.page.click_freezer_item("@ancestor")
        self.page.add_org_to_exp()

        # Run the experiment.
        self.page.run_from_menu()
        self.page.util.sleep(3, "Waiting for updates to occur.")

        # Assert that updates have occurred.
        assert js_assertions.get_current_update() > 0
        assert js_assertions.gr_get_current_update() > 0

        # Pause the experiment.
        self.page.pause_from_menu()
        self.page.util.sleep(1, "Making sure pause goes into effect.")

        # Get current update, wait a few seconds, assert it has not changed.
        current_update = js_assertions.get_current_update()
        self.page.util.sleep(3, "Ensuring no updates occur after pause.")
        assert js_assertions.get_current_update() == current_update

        # Do one update
        self.page.do_one_update()
        self.page.util.sleep(1, "Making sure update has time to occur.")
        assert (js_assertions.get_current_update() - current_update) == 1
