import pytest

from tests.base_test import BaseTest


class OrgRepStatsTest(BaseTest):
    """
    Test class that runs simple experiments with the organism window
    reproduction, specifically regarding to statistics.
    """

    @pytest.mark.run(order=1)
    def test_org_rep_stats_startup(self):
        """
        Tests that the stats for Organism Reproduction are set to 0 at startup.

        :return: None.
        """
        self.op.go_to_organism()
        assert self.op.get_org_num_not_performed() == 0
        assert self.op.get_org_num_nan_performed() == 0
        assert self.op.get_org_num_and_performed() == 0
        assert self.op.get_org_num_orn_performed() == 0
        assert self.op.get_org_num_oro_performed() == 0
        assert self.op.get_org_num_ant_performed() == 0
        assert self.op.get_org_num_nor_performed() == 0
        assert self.op.get_org_num_xor_performed() == 0
        assert self.op.get_org_num_equ_performed() == 0

    @pytest.mark.run(order=2)
    def test_org_rep_stats_functionality(self):
        """
        Tests that the controls for Organism Reproduction work as intended when
        an organism that can perform all functions is added to the dish.

        :return: None.
        """
        # Put all_functions in organism view
        self.op.go_to_organism()
        self.bp.click_freezer_item("@all_functions")
        self.bp.add_org_to_org_view()

        # Wait for ancestor to be in org view, ensure initial values sensible.
        self.op.wait_until_org_controls_enabled()

        # Make sure at beginning of reproduction, all stats 0.
        assert self.op.get_org_num_not_performed() == 0
        assert self.op.get_org_num_nan_performed() == 0
        assert self.op.get_org_num_and_performed() == 0
        assert self.op.get_org_num_orn_performed() == 0
        assert self.op.get_org_num_oro_performed() == 0
        assert self.op.get_org_num_ant_performed() == 0
        assert self.op.get_org_num_nor_performed() == 0
        assert self.op.get_org_num_xor_performed() == 0
        assert self.op.get_org_num_equ_performed() == 0

        # Go to end of reproduction.
        self.op.end_org_rep()

        # Assert that all functions have been performed.
        assert self.op.get_org_num_not_performed() == 1
        assert self.op.get_org_num_nan_performed() == 1
        assert self.op.get_org_num_and_performed() == 1
        assert self.op.get_org_num_orn_performed() == 1
        assert self.op.get_org_num_oro_performed() == 1
        assert self.op.get_org_num_ant_performed() == 1
        assert self.op.get_org_num_nor_performed() == 1
        assert self.op.get_org_num_xor_performed() == 1
        assert self.op.get_org_num_equ_performed() == 1
