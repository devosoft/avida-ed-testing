import pytest
import time

from tests.base_test import BaseTest


class OrganismNavigationTest(BaseTest):
    """
    Test class that tests navigation between the panels and other sub-specializations
    within the Organism page.
    """

    @pytest.mark.run(order=2)
    def test_toggle_org_settings(self):
        """
        Tests closing the Organism Settings pop-up.

        :return: None.
        """
        self.bp.go_to_organism()
        self.op.open_org_settings()
        assert self.op.org_settings_displayed()
        self.op.close_org_settings()
        time.sleep(1)
        assert not self.op.org_settings_displayed()

    @pytest.mark.run(order=1)
    def test_toggle_org_details(self):
        """
        Tests toggling the Details panel within the Organism page on and off.
        
        :return: None.
        """
        self.bp.go_to_organism()
        self.op.open_org_details()
        time.sleep(1)
        assert self.op.org_details_displayed()
        self.op.close_org_details()
        time.sleep(1)
        assert not self.op.org_details_displayed()
        self.op.open_org_details()
        time.sleep(1)
        assert self.op.org_details_displayed()
