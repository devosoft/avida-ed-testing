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
