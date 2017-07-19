from base.base_page import BasePage
from specializations.value_getter.value_getter import ValueGetter

import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup")
class PopStatsSanityTest(unittest.TestCase):
    """
    Test class that runs a simple experiment that ensures that population
    statistics information is valid.
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
    def test_pop_stats_sanity_ancestor(self):
        """
        Tests that running an experiment with @ancestor for a brief period of
        time does not lead to any unexpected values in the population statistics
        window.

        :return: None.
        """
        js_assertions = ValueGetter(self.page)

        # Add @ancestor to dish.
        self.page.click_freezer_item("@ancestor")
        self.page.add_org_to_exp()

        # Run the experiment for a while, then pause it.
        self.page.run_from_menu()
        self.page.util.sleep(15, "Waiting for updates to occur.")
        self.page.pause_from_menu()
        self.page.util.sleep(1, "Waiting for pause to take affect.")

        # Test that population stats are valid.
        assert js_assertions.get_current_update() > 0
        assert js_assertions.get_num_orgs() > 1
        assert 0.0 <= js_assertions.get_avg_fit() <= 1.0
        assert js_assertions.get_avg_energy_rate() > 0
        assert js_assertions.get_avg_offspring_cost() > 0
        assert js_assertions.get_avg_age() >= 0

