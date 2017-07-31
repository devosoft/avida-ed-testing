import pytest

from tests.base_test import BaseTest


class EnvSettingsInputTest(BaseTest):
    """
    Test class that checks the input validation on the variables that can be
    edited through the Environmental Settings pane in the Population window.
    """

    @pytest.mark.run(order=1)
    @pytest.mark.usefixtures("hard_reset")
    def test_input_dishsize_negnum(self):
        """
        Tests that crashes and unexpected behaviors do not occur if a negative
        number is given to the dish size boxes.

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

    @pytest.mark.run(order=2)
    @pytest.mark.usefixtures("hard_reset")
    def test_input_dishsize_zero(self):
        """
        Tests that crashes and unexpected behaviors do not occur if a dish size
        dimension is set to 0.

        :return: None.
        """

        # Edit dish size with nonsensical values.
        self.pp.show_env_settings()
        self.pp.edit_dish_cols("0")
        self.pp.hide_env_settings()

        # Add an organism to the experiment and try to run it.
        self.bp.click_freezer_item("@ancestor")
        self.bp.add_org_to_exp()
        self.pp.run_from_pop()

        # Wait for a short period so that response to run attempt occurs.
        self.bp.util.sleep(3)

    @pytest.mark.run(order=3)
    @pytest.mark.usefixtures("hard_reset")
    def test_input_dishsize_str(self):
        """
        Tests that crashes and unexpected behaviors do not occur if a
        non-numeric string is given to the dish size boxes.

        :return: None.
        """
        # Edit dish size with nonsensical values.
        self.pp.show_env_settings()
        self.pp.edit_dish_cols("sample text")
        self.pp.hide_env_settings()

        # Add an organism to the experiment and try to run it.
        self.bp.click_freezer_item("@ancestor")
        self.bp.add_org_to_exp()
        self.pp.run_from_pop()

        # Wait for a short period so that response to run attempt occurs.
        self.bp.util.sleep(3)

    @pytest.mark.run(order=3)
    def test_input_mut(self):
        """
        Tests that crashes and unexpected behavior do not occur if bad input is
        given to the population mutation rate boxes.

        :return: None.
        """

        # Edit pop mutation rate with nonsensical value.
        self.pp.show_env_settings()
        self.pp.edit_mut_rate("-12")
        self.pp.hide_env_settings()

        # Add an organism to the dish and try to run it.
        self.bp.click_freezer_item("@ancestor")
        self.bp.add_org_to_exp()
        self.pp.run_from_pop()

        # Wait a short period so that response to run attempt occurs.
        self.bp.util.sleep(3)
