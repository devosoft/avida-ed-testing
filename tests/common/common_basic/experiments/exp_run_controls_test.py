import pytest

from tests.base_test import BaseTest


class ExperimentControlsTest(BaseTest):
    """
    Test class that runs a very simple experiment in Avida-ED.
    """

    @pytest.mark.run()
    def test_exp_run_controls(self):
        """
        Tests that a simple experiment can be run and that running, pausing, and
        doing one update work as expected.

        :return: None.
        """

        # Add @ancestor to dish.
        self.bp.click_freezer_item("@ancestor")
        self.bp.add_org_to_exp()

        # Run the experiment.
        self.bp.run_from_menu()
        self.bp.util.sleep(3, "Waiting for updates to occur.")

        # Assert that updates have occurred.
        assert self.vg.get_current_update() > 0
        assert self.vg.gr_get_current_update() > 0

        # Pause the experiment.
        self.bp.pause_from_menu()
        self.bp.util.sleep(1, "Making sure pause goes into effect.")

        # Get current update, wait a few seconds, assert it has not changed.
        current_update = self.vg.get_current_update()
        self.bp.util.sleep(3, "Ensuring no updates occur after pause.")
        assert self.vg.get_current_update() == current_update

        # Do one update
        self.bp.forward_from_menu()
        self.bp.util.sleep(1, "Making sure update has time to occur.")
        assert (self.vg.get_current_update() - current_update) == 1
