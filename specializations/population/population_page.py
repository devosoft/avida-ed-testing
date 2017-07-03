import logging

from base.base_page import BasePage
from utilities.util_methods import UtilityMethods
from utilities.custom_logger import create_custom_logger


class PopulationPage(BasePage):
    """
    Specialization of the BasePage that is specialized to the Population page
    on the Avida-ED website.
    """

    log = create_custom_logger(logging.DEBUG)
    util = UtilityMethods()

    def __init__(self, driver):
        """
        Sets up the page for use at initialization.

        :param driver: The driver that interacts with the actual page.
        """
        super().__init__(driver)
        self.driver = driver
        self.go_to_population()

    def env_settings_displayed(self):
        """
        Determines whether the "Environmental Settings" panel within the
        "Population" page is displayed.
        
        :return: True if the "Environmental Settings" panel is displayed, false
        otherwise.
        """

        if self.population_displayed():
            setup_button_text = self.get_text("popSetupButton")
            if (self.element_displayed("setupBlock") and
                    self.util.verify_text_matches(setup_button_text, "Map")):
                return True
        return False

    def grid_displayed(self):
        """
        Determines whether the main Petri dish grid on the "Population" page
        is displayed.
        
        This is essentially the opposite of the env_settings_displayed method. 
        This method could be a reversal of env_settings_displayed, but doing
        that would reduce performance because we would have to account for the
        fact that if the population window is not displayed, both functions will
        return false.
        
        :return: True if the Petri dish is displayed, false otherwise.
        """
        if self.population_displayed():
            setup_button_text = self.get_text("popSetupButton")
            if (not self.element_displayed("setupBlock") and
                    self.util.verify_text_matches(setup_button_text, "Setup")):
                return True
        return False

    def show_env_settings(self):
        """
        Navigates to the "Environmental Settings" panel within the "Population"
        page on the Avida-ED website.
        
        :return: None 
        """
        self.go_to_population()
        if not self.env_settings_displayed():
            self.click_element("popSetupButton")

    def hide_env_settings(self):
        """
        Hides the "Environmental Settings" panel within the "Population" page on
        the Avida-ED website.
        
        :return: None 
        """
        self.go_to_population()
        if self.env_settings_displayed():
            self.click_element("popSetupButton")

    def pop_stats_displayed(self):
        """
        Checks if the stats panel within the "Population" pane of the Avida-ED
        website.

        :return: True if the stats panel is visible, false otherwise.
        """
        pop_stats_displayed = self.element_displayed("popRight")
        return pop_stats_displayed

    def show_pop_stats(self):
        """
        Shows the stats window within the Population pane.
        
        :return: None.
        """
        self.go_to_population()
        if not self.element_displayed("popRight"):
            self.click_element("popStatsButton")

    def hide_pop_stats(self):
        """
        Hides the stats window within the Population pane.
        
        :return: None.
        """
        self.go_to_population()
        if self.element_displayed("popRight"):
            self.click_element("popStatsButton")

    def get_update_ui_text(self):
        """
        Gets the text from the UI element containing information about the
        simulation update/time.

        :return: String containing update information.
        """
        return self.get_text("TimeLabel")
