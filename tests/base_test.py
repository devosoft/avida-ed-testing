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
        Sets up class prior to run.

        :return: None.
        """
        self.bp = BasePage(self.driver)

        self.pp = PopulationPage(self.driver)
        self.op = OrganismPage(self.driver)
        self.ap = AnalysisPage(self.driver)
        self.vg = ValueGetter(self.driver)
