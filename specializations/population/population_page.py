import logging

from base.base_page import BasePage
from utilities.custom_logger import create_custom_logger


class PopulationPage(BasePage):
    """
    Specialization of the BasePage that is specialized to the Population page
    on the Avida-ED website.
    """

    # Logger
    log = create_custom_logger(logging.DEBUG)\

    # Locators for population setup pane.
    __setup_button_id = "popSetupButton"
    __setup_dish = "Dish"
    __setup_setup = "Setup"
    __setup_block_id = "setupBlock"

    # Locators for population statistics window.
    __stats_window = "popRight"
    __stats_button = "popStatsButton"
    __dish_cols_box = "sizeCols"
    __dish_rows_box = "sizeRows"

    # Locators for updates and other UI information.
    __update_text = "TimeLabel"

    # Locators for buttons underneath dish.
    __run_pause_pop = "runStopButton"
    __run_text = "Run"
    __pause_text = "Pause"

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
            setup_button_text = self.get_text(self.__setup_button_id)
            if (self.element_displayed(self.__setup_block_id) and
                    self.util.verify_text_matches(setup_button_text, self.__setup_dish)):
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
            setup_button_text = self.get_text(self.__setup_button_id)
            if (not self.element_displayed(self.__setup_block_id) and
                    self.util.verify_text_matches(setup_button_text, self.__setup_setup)):
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
            self.click_element(self.__setup_button_id)

    def hide_env_settings(self):
        """
        Hides the "Environmental Settings" panel within the "Population" page on
        the Avida-ED website.
        
        :return: None 
        """
        self.go_to_population()
        if self.env_settings_displayed():
            self.click_element(self.__setup_button_id)

    def pop_stats_displayed(self):
        """
        Checks if the stats panel within the "Population" pane of the Avida-ED
        website.

        :return: True if the stats panel is visible, false otherwise.
        """
        pop_stats_displayed = self.element_displayed(self.__stats_window)
        return pop_stats_displayed

    def show_pop_stats(self):
        """
        Shows the stats window within the Population pane.
        
        :return: None.
        """
        self.go_to_population()
        if not self.element_displayed(self.__stats_window):
            self.click_element(self.__stats_button)

    def hide_pop_stats(self):
        """
        Hides the stats window within the Population pane.
        
        :return: None.
        """
        self.go_to_population()
        if self.element_displayed(self.__stats_window):
            self.click_element(self.__stats_button)

    def __click_runpause_pop_button(self):
        """
        Clicks on the main 'Run'/'Pause' button underneath the dish to start
        the experiment.

        :return: None.
        """
        self.click_element(self.__run_pause_pop)

    def runpause_text_is_run(self):
        """
        Checks whether the text of the 'Run'/'Pause' button underneath the dish
        currently says 'Run'.

        :return: True if button text is 'Run', false if it is not (in which case
        it must be 'Pause").
        """
        btn_text = self.get_text(self.__run_pause_pop)
        if self.util.verify_text_matches(btn_text, self.__run_text):
            return True
        return False

    def run_from_pop(self):
        """
        Runs the experiment via the button underneath the dish.

        :return: None.
        """
        if self.runpause_text_is_run():
            self.__click_runpause_pop_button()

    def pause_from_pop(self):
        """
        Pauses the experiment via the button underneath the dish.
        :return:
        """
        if not self.runpause_text_is_run():
            self.__click_runpause_pop_button()

    def get_update_ui_text(self):
        """
        Gets the text from the UI element containing information about the
        simulation update/time.

        :return: String containing update information.
        """
        return self.get_text(self.__update_text)

    def edit_dish_cols(self, input):
        """
        Edits the dish column number in the environmental settings panel.

        :param input: String containing input to the text box.

        :return: None.
        """
        self.show_env_settings()
        cols_box = self.get_element(self.__dish_cols_box)
        cols_box.clear()
        self.send_keys(element=cols_box, keys=input)
        self.hide_env_settings()

    def edit_dish_rows(self, input):
        """
        Edits the dish row number in the environmental settings panel.

        :param input: String containing input to the text box.

        :return: None.
        """
        self.show_env_settings()
        rows_box = self.get_element(self.__dish_rows_box)
        rows_box.clear()
        self.send_keys(element=rows_box, keys=input)
        self.hide_env_settings()