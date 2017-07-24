import unittest
import pytest


@pytest.mark.usefixtures("bp_setup")
class PopulationNavigationTest(unittest.TestCase):
    """
    Test class that tests navigation between various panels and sub-specializations within
    the Population page.
    """

    @pytest.mark.run(order=1)
    def test_toggle_env_settings(self):
        """
        Tests toggling the Environmental Settings panel on and off.
        
        :return: None. 
        """
        self.bp.go_to_population()
        self.pp.show_env_settings()
        assert self.pp.env_settings_displayed()
        assert not self.pp.grid_displayed()
        self.pp.hide_env_settings()
        assert not self.pp.env_settings_displayed()
        assert self.pp.grid_displayed()
        self.pp.show_env_settings()
        assert self.pp.env_settings_displayed()
        assert not self.pp.grid_displayed()

    @pytest.mark.run(order=2)
    def test_toggle_pop_stats(self):
        """
        Tests toggling the Population Statistics window on and off.
        
        :return: None. 
        """
        self.bp.go_to_population()
        self.pp.show_pop_stats()
        assert self.pp.pop_stats_displayed()
        self.pp.hide_pop_stats()
        assert not self.pp.pop_stats_displayed()
        self.pp.show_pop_stats()
        assert self.pp.pop_stats_displayed()

