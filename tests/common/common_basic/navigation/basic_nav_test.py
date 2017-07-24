import unittest
import pytest
import time


@pytest.mark.usefixtures("bp_setup")
class BasicNavigationTest(unittest.TestCase):
    """
    Test class that tests navigation between the major specializations
    within the Avida-ED website.
    
    Note that "specializations" are logical rather than real, URL-level separations
    within the site. They are divided into the major parts of the website --
    Population, Organism, and Analysis -- because a user will always be within
    one of those three parts of the site.
    """

    @pytest.mark.run(order=3)
    def test_go_to_population(self):
        """
        Tests navigating to the Population page.
        
        Should not be run first, because the site loads this page as the
        default.
        
        :return: None. 
        """
        self.bp.go_to_population()
        assert self.bp.population_displayed()
        time.sleep(3)

    @pytest.mark.run(order=1)
    def test_go_to_organism(self):
        """
        Tests navigating to the Organism page.
        
        :return: None.
        """
        self.bp.go_to_organism()
        assert self.bp.organism_displayed()
        time.sleep(3)

    @pytest.mark.run(order=2)
    def test_go_to_analysis(self):
        """
        Tests navigating to the Analysis page.
        
        :return: None. 
        """
        self.bp.go_to_analysis()
        assert self.bp.analysis_displayed()
        time.sleep(3)
