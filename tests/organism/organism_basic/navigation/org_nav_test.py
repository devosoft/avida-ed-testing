from pages.organism.organism_page import OrganismPage
import unittest
import pytest
import time


@pytest.mark.usefixtures("one_time_setup")
class OrganismNavigationTest(unittest.TestCase):
    """
    Test class that tests navigation between the panels and other sub-pages
    within the Organism page.
    """

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        """
        Sets up the class before tests run.
        
        :param one_time_setup: Necessary parameter for running the 
        one_time_setup Pytest fixture. DO NOT REMOVE.
         
        :return: None.
        """
        self.page = OrganismPage(self.driver)

    @pytest.mark.run(order=2)
    def test_toggle_org_settings(self):
        """
        Tests closing the Organism Settings pop-up.

        :return: None.
        """
        self.page.open_org_settings()
        time.sleep(5)
        assert self.page.org_settings_displayed()
        self.page.close_org_settings()
        time.sleep(1)
        assert not self.page.org_settings_displayed()

    @pytest.mark.run(order=1)
    def test_toggle_org_details(self):
        """
        Tests toggling the Details panel within the Organism page on and off.
        
        :return: None.
        """
        self.page.open_org_details()
        time.sleep(1)
        assert self.page.org_details_displayed()
        self.page.close_org_details()
        time.sleep(1)
        assert not self.page.org_details_displayed()
        self.page.open_org_details()
        time.sleep(1)
        assert self.page.org_details_displayed()
