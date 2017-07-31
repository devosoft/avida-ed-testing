import pytest
import unittest

from base.base_page import BasePage

from specializations.population.population_page import PopulationPage
from specializations.organism.organism_page import OrganismPage
from specializations.analysis.analysis_page import AnalysisPage
from specializations.value_getter.value_getter import ValueGetter


@pytest.mark.usefixtures("driver_setup")
class BaseTest(unittest.TestCase):
    """
    Test class that tests the initial configuration of the main menu bar at the
    top of the Avida-ED website to ensure that the correct menu options are
    accessible at startup.
    """

    @pytest.fixture(autouse=True)
    def class_setup(self, driver_setup):
        """
        Sets up class prior to run. Adds necessary variables to the class and
        waits for the splash screen to go away.

        :return: None.
        """

        # Set up base page and wait for splash screen to go away.
        self.bp = BasePage(self.driver)
        self.bp.wait_until_splash_gone()

        # Set up objects for interacting with other pages / specializations.
        self.pp = PopulationPage(self.driver)
        self.op = OrganismPage(self.driver)
        self.ap = AnalysisPage(self.driver)
        self.vg = ValueGetter(self.driver)

    @pytest.yield_fixture(autouse=True)
    def closing_assertions(self):
        """
        Performs basic assertions that should evaluate to True after every test
        (e.g. crash report not displayed, etc.).

        :return: None.
        """
        yield
        assert not self.bp.crash_report_displayed()

    @pytest.yield_fixture()
    def soft_reset(self):
        """
        Performs a 'soft reset" at the beginning of an experiment by resetting
        the dish. In the future (when tests with Organism and Analysis window
        are in place) it will also do as much as possible to reset those
        windows.

        * Not Fully Implemented Yet *

        :return:
        """
        yield
        self.pp.new_exp_discard()

    @pytest.yield_fixture()
    def hard_reset(self):
        """
        Performs a 'hard reset' at the beginning of an experiment by refreshing
        the Avida-ED webpage and waits for it to load completely.

        :return: None.
        """
        yield
        self.bp.refresh_avida_ed()

