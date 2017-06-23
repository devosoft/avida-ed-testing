from specializations.population.population_page import PopulationPage
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup")
class PopulationNavigationTest(unittest.TestCase):
    """
    Test class that tests navigation between various panels and sub-specializations within
    the Population page.
    """

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        """
        Sets up the class before the tests run.
        
        :param one_time_setup: Necessary parameter to use the one_time_setup
        Pytest fixture.
        
        :return: None.
        """
        self.page = PopulationPage(self.driver)

    @pytest.mark.run(order=1)
    def test_toggle_env_settings(self):
        """
        Tests toggling the Environmental Settings panel on and off.
        
        :return: None. 
        """
        self.page.show_env_settings()
        assert self.page.env_settings_displayed()
        assert not self.page.grid_displayed()
        self.page.hide_env_settings()
        assert not self.page.env_settings_displayed()
        assert self.page.grid_displayed()
        self.page.show_env_settings()
        assert self.page.env_settings_displayed()
        assert not self.page.grid_displayed()

    @pytest.mark.run(order=2)
    def test_toggle_pop_stats(self):
        """
        Tests toggling the Population Statistics window on and off.
        
        :return: None. 
        """
        self.page.show_pop_stats()
        assert self.page.pop_stats_displayed()
        self.page.hide_pop_stats()
        assert not self.page.pop_stats_displayed()
        self.page.show_pop_stats()
        assert self.page.pop_stats_displayed()

