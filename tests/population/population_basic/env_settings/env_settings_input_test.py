import pytest

from tests.base_test import BaseTest


class EnvSettingsInputTest(BaseTest):
    """
    Test class that checks the input validation on the variables that can be
    edited through the Environmental Settings pane in the Population window.
    """

    @pytest.mark.run(order=1)
    def test_input_dishsize(self):
        """
        Tests that crashes and unexpected behaviors do not occur if bad input
        is given to the dish size boxes.

        :return: None.
        """

        # Edit dish size with nonsensical values.
        self.pp.show_env_settings()
        self.pp.edit_dish_cols("-12")
        self.pp.hide_env_settings()

        # Add an organism to the experiment and try to run it.
        self.bp.click_freezer_item("@ancestor")
        self.bp.add_org_to_exp()
        self.pp.run_from_pop()

        # Wait for a short period so that response to run attempt occurs.
        self.bp.util.sleep(3)
