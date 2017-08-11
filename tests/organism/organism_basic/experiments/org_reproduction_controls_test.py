import pytest

from tests.base_test import BaseTest


class OrgRepControlsTest(BaseTest):
    """
    Test class that runs simple experiments with the organism window
    reproduction.
    """

    @pytest.mark.run(order=1)
    def test_org_rep_startup(self):
        """
        Tests that the control for Organism Reproduction are not enabled on
        startup.

        :return: None.
        """
        self.op.go_to_organism()
        assert not self.op.org_rep_controls_enabled()
        assert self.op.org_rep_controls_disabled()
        assert self.op.get_cycle() == 0

    @pytest.mark.run(order=2)
    def test_org_rep_functionality(self):
        """
        Tests that the controls for Organism Reproduction work as intended once
        an organism is loaded into the dish.

        :return: None.
        """
        # Put ancestor in organism view
        self.op.go_to_organism()
        self.bp.click_freezer_item("@ancestor")
        self.bp.add_org_to_org_view()

        # Wait for ancestor to be in org view, ensure initial values sensible.
        self.op.wait_until_org_controls_enabled()
        assert self.op.get_cycle() == 0

        # Test that forward and back options work.
        self.op.forward_org_rep()
        assert self.op.get_cycle() == 1
        self.op.back_org_rep()
        assert self.op.get_cycle() == 0

        # Test that running works.
        self.op.run_org_rep()
        self.op.util.sleep(1)
        assert self.op.get_cycle() > 0

        # Test that pausing works.
        self.op.stop_org_rep()
        cycle = self.op.get_cycle()
        self.op.util.sleep(1)
        assert self.op.get_cycle() == cycle

        # Test that End goes to end of reproduction.
        self.op.end_org_rep()
        assert self.op.get_cycle() == 189

        # Test that Reset goes back to 0.
        self.op.reset_org_rep()
        assert self.op.get_cycle() == 0
