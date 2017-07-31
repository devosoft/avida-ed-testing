import pytest

from tests.base_test import BaseTest


class PopStatsSanityTest(BaseTest):
    """
    Test class that runs a simple experiment that ensures that population
    statistics information is valid.
    """

    @pytest.mark.run()
    def test_pop_stats_sanity_ancestor(self):
        """
        Tests that running an experiment with @ancestor for a brief period of
        time does not lead to any unexpected values in the population statistics
        window.

        :return: None.
        """

        # Add @ancestor to dish.
        self.bp.add_ancestor_to_dish()

        # Run the experiment for a while, then pause it.
        self.bp.run_from_menu()
        self.bp.util.sleep(15, "Waiting for updates to occur.")
        self.bp.pause_from_menu()
        self.bp.util.sleep(1, "Waiting for pause to take affect.")

        # Test that population stats are valid.
        assert self.vg.get_current_update() > 0
        assert self.vg.get_num_orgs() > 1
        assert 0.0 <= self.vg.get_avg_fit() <= 1.0
        assert self.vg.get_avg_energy_rate() > 0
        assert self.vg.get_avg_offspring_cost() > 0
        assert self.vg.get_avg_age() >= 0

