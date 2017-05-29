from base.base_page import BasePage

import unittest
import pytest
import time


@pytest.mark.usefixtures("one_time_setup")
class BasicNavigationTest(unittest.TestCase):
    """
    Test class that tests navigation between the major pages
    within the Avida-ED website.
    
    Note that "pages" are logical rather than real, URL-level separations
    within the site. They are divided into the major parts of the website --
    Population, Organism, and Analysis -- because a user will always be within
    one of those three parts of the site.
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

    @pytest.mark.run(order=3)
    def test_go_to_population(self):
        """
        Tests navigating to the Population page.
        
        Should not be run first, because the site loads this page as the
        default.
        
        :return: None. 
        """
        self.page.go_to_population()
        assert self.page.population_displayed()
        time.sleep(3)

    @pytest.mark.run(order=1)
    def test_go_to_organism(self):
        """
        Tests navigating to the Organism page.
        
        :return: None.
        """
        self.page.go_to_organism()
        assert self.page.organism_displayed()
        time.sleep(3)

    @pytest.mark.run(order=2)
    def test_go_to_analysis(self):
        """
        Tests navigating to the Analysis page.
        
        :return: None. 
        """
        self.page.go_to_analysis()
        assert self.page.analysis_displayed()
        time.sleep(3)
