from base.base_page import BasePage

import pytest
import unittest

@pytest.mark.usefixtures("one_time_setup")
class MenuBarStartupTest(unittest.TestCase):
    """
    Test class that tests the initial configuration of the main menu bar at the
    top of the Avida-ED website to ensure that the correct menu options are
    accessible at startup.
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
    def test_freezer_menu_launch(self):
        """
        Tests that the correct menu options in the Freezer tab are usable on
        startup.

        :return: None.
        """
        assert not self.page.can_save_current_pop()
        assert not self.page.can_save_selected_org()
        assert not self.page.can_save_offspring_org()

    @pytest.mark.run()
    def test_control_menu_launch(self):
        """
        Tests that the correct menu options in the Control tab are usable on
        startup.

        :return: None.
        """
        assert self.page.can_run_from_menu()
        assert not self.page.can_pause_from_menu()
        assert not self.page.can_bring_to_org_window()
        assert not self.page.can_bring_child_to_org_window()

