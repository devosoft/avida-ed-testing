import pytest

from tests.base_test import BaseTest


class MenuBarStartupTest(BaseTest):
    """
    Test class that tests the initial configuration of the main menu bar at the
    top of the Avida-ED website to ensure that the correct menu options are
    accessible at startup.
    """

    @pytest.mark.run()
    def test_freezer_menu_launch(self):
        """
        Tests that the correct menu options in the Freezer tab are usable on
        startup.

        :return: None.
        """
        assert not self.bp.can_save_current_pop()
        assert not self.bp.can_save_selected_org()
        assert not self.bp.can_save_offspring_org()

    @pytest.mark.run()
    def test_control_menu_launch(self):
        """
        Tests that the correct menu options in the Control tab are usable on
        startup.

        :return: None.
        """
        assert self.bp.can_run_from_menu()
        assert not self.bp.can_pause_from_menu()
        assert not self.bp.can_bring_to_org_window()
        assert not self.bp.can_bring_child_to_org_window()
