import pytest

from tests.base_test import BaseTest


class PopStatsSanityTest(BaseTest):
    """
    Test class that runs a simple experiment that ensures that population
    statistics information is valid.
    """

    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures("hard_reset")
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
        assert self.vg.get_avg_fit() >= 0.0
        assert self.vg.get_avg_energy_rate() > 0
        assert self.vg.get_avg_offspring_cost() > 0
        assert self.vg.get_avg_age() >= 0

    @pytest.mark.run(order=2)
    def test_pop_stats_sanity_allfxns(self):
        """
        Tests that running an experiment with @all_functions does not create
        unexpected values in pop. stats window and that this window shows that
        all of the functions have been performed at least once (which should
        always happen because the starting org can perform all functions).

        :return: None.
        """
        # Add @all_functions to dish.
        self.bp.add_all_functions_to_dish()

        # Run the experiment for a while, then pause it.
        self.bp.run_from_menu()
        self.bp.util.sleep(15, "Waiting for updates to occur.")
        self.bp.pause_from_menu()
        self.bp.util.sleep(1, "Waiting for pause to take affect.")

        # Test that population stats are valid.
        assert self.vg.get_current_update() > 0
        assert self.vg.get_num_orgs() > 1
        assert self.vg.get_avg_fit() >= 0.0
        assert self.vg.get_avg_energy_rate() > 0
        assert self.vg.get_avg_offspring_cost() > 0
        assert self.vg.get_avg_age() >= 0

        # Test that all functions have occurred.
        assert self.vg.get_num_performing_not() > 0
        assert self.vg.get_num_performing_nan() > 0
        assert self.vg.get_num_performing_and() > 0
        assert self.vg.get_num_performing_orn() > 0
        assert self.vg.get_num_performing_oro() > 0
        assert self.vg.get_num_performing_ant() > 0
        assert self.vg.get_num_performing_nor() > 0
        assert self.vg.get_num_performing_xor() > 0
        assert self.vg.get_num_performing_equ() > 0

