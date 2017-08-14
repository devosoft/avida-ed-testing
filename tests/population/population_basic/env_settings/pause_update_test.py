import pytest

from tests.base_test import BaseTest


class PauseUpdateTest(BaseTest):
    """
    Test class that checks the input validation on the variables that can be
    edited through the Environmental Settings pane in the Population window.
    """

    @pytest.mark.run(order=1)
    def test_startup_pause_settings(self):
        """
        Tests that pause settings are correct on startup.

        :return: None.
        """
        assert self.pp.pause_manually_enabled()
        assert not self.pp.pause_at_update_enabled()

    @pytest.mark.run(order=2)
    def test_pause_at_update(self):
        """
        Tests that 'Pause at Update' setting will allow user to automatically
        pause the experiment at the given update.

        :return: None.
        """
        # Setup pause settings.
        self.pp.enable_pause_at_update()
        self.pp.edit_pause_update(9)

        # Set up the rest of the experiment.
        self.bp.add_ancestor_to_dish()

        # Run the experiment.
        self.bp.run_from_menu()

        # Wait long enough for experiment to have reached update 9.
        self.bp.util.sleep(10, "Waiting for experiment to pause automatically.")

        # Check that pause worked properly.
        assert self.vg.get_pop_current_update() == 9

        # Wait to make sure it is paused.
        self.bp.util.sleep(1, "Ensuring that experiment is paused.")
        assert self.vg.get_pop_current_update() == 9
