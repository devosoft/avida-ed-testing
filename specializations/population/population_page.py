import logging

from base.base_page import BasePage
from utilities.custom_logger import create_custom_logger


class PopulationPage(BasePage):
    """
    Specialization of the BasePage that is specialized to the Population page
    on the Avida-ED website.
    """

    # Logger
    log = create_custom_logger(logging.DEBUG)

    # Locators for population setup pane.
    __setup_button_id = "popSetupButton"
    __setup_dish = "Map"
    __setup_setup = "Setup"
    __setup_block_id = "setupBlock"
    __mut_rate_input = "muteInput"
    __update_radio_attr = "aria-checked"
    __manual_update_btn = "manualUpdateRadio"
    __auto_update_btn = "autoUpdateRadio"
    __pause_update_input = "autoUpdateSpinner"

    # Locators for population statistics window.
    __stats_window = "popRight"
    __stats_button = "popStatsButton"
    __dish_cols_box = "sizeCols"
    __dish_rows_box = "sizeRows"


    # Locators for updates and other UI information.
    __update_text = "TimeLabel"

    # Locators for buttons underneath dish.
    __run_pause_pop_button = "runStopButton"
    __run_text = "Run"
    __pause_text = "Pause"
    __new_dish_button = "newDishButton"
    __forward_button = "oneUpdateButton"

    # Locators for new dish dialog box.
    __new_dish_dlg = "dijit_Dialog_4"
    __new_dish_cancel_xpath = "//*/span[@widgetid='newCancel']"
    __new_dish_discard_xpath = "//*/span[@widgetid='newDiscard']"
    __new_dish_saveconf_xpath = "//*/span[@widgetid='newSaveConfig']"
    __new_dish_savepop_xpath = "//*/span[@widgetid='newSaveWorld']"

    def __init__(self, driver):
        """
        Sets up the page for use at initialization.

        :param driver: The driver that interacts with the actual page.
        """
        super().__init__(driver)
        self.driver = driver

    def env_settings_displayed(self):
        """
        Determines whether the "Environmental Settings" panel within the
        "Population" page is displayed.
        
        :return: True if the "Environmental Settings" panel is displayed, false
        otherwise.
        """

        setup_button_text = self.get_text(self.__setup_button_id)
        displayed = (self.element_displayed(self.__setup_block_id) and
                     self.util.verify_text_matches(setup_button_text,
                                                   self.__setup_dish))
        self.log.info("Is Environmental Settings displayed? " + str(displayed))
        return displayed

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
        setup_button_text = self.get_text(self.__setup_button_id)
        displayed = (not self.element_displayed(self.__setup_block_id) and
                     self.util.verify_text_matches(setup_button_text,
                                                   self.__setup_setup))
        self.log.info("Is grid displayed? " + str(displayed))
        return displayed

    def show_env_settings(self):
        """
        Navigates to the "Environmental Settings" panel within the "Population"
        page on the Avida-ED website.
        
        :return: None 
        """
        self.go_to_population()
        if not self.env_settings_displayed():
            self.click_element(self.__setup_button_id)
            if self.wait_until_visible(self.__setup_block_id):
                self.log.info("Showed environmental settings window.")
            else:
                self.log.warning("Failed to show environmental settings window.")

    def hide_env_settings(self):
        """
        Hides the "Environmental Settings" panel within the "Population" page on
        the Avida-ED website.
        
        :return: None 
        """
        self.go_to_population()
        if self.env_settings_displayed():
            self.click_element(self.__setup_button_id)
            if self.wait_until_invisible(self.__setup_block_id):
                self.log.info("Hid environmental settings window.")
            else:
                self.log.warning("Failed to hide environmental settings window.")

    def pop_stats_displayed(self):
        """
        Checks if the stats panel within the "Population" pane of the Avida-ED
        website.

        :return: True if the stats panel is visible, false otherwise.
        """
        pop_stats_displayed = self.element_displayed(self.__stats_window)
        self.log.info("Is population statistics displayed? "
                      + str(pop_stats_displayed))
        return pop_stats_displayed

    def show_pop_stats(self):
        """
        Shows the stats window within the Population pane.
        
        :return: None.
        """
        self.go_to_population()
        if not self.element_displayed(self.__stats_window):
            self.click_element(self.__stats_button)
            if self.wait_until_visible(self.__stats_window):
                self.log.info("Showed population statistics window.")
            else:
                self.log.warning("Failed to show population statistics window.")

    def hide_pop_stats(self):
        """
        Hides the stats window within the Population pane.
        
        :return: None.
        """
        self.go_to_population()
        if self.element_displayed(self.__stats_window):
            self.click_element(self.__stats_button)
            if self.wait_until_invisible(self.__stats_window):
                self.log.info("Hid population statistics window.")
            else:
                self.log.warning("Failed to hide population statistics window.")

    def __click_runpause_pop_button(self):
        """
        Clicks on the main 'Run'/'Pause' button underneath the dish to start
        the experiment.

        :return: None.
        """
        self.click_element(self.__run_pause_pop_button)

    def runpause_text_is_run(self):
        """
        Checks whether the text of the 'Run'/'Pause' button underneath the dish
        currently says 'Run'.

        :return: True if button text is 'Run', false if it is not (in which case
        it must be 'Pause").
        """
        btn_text = self.get_text(self.__run_pause_pop_button)
        is_run = self.util.verify_text_matches(btn_text, self.__run_text)
        self.log.info("Is Run/Pause button text 'Run'? " + str(is_run))
        return is_run

    def run_from_pop(self):
        """
        Runs the experiment via the button underneath the dish.

        :return: None.
        """
        if self.runpause_text_is_run():
            self.__click_runpause_pop_button()
            self.log.info("Started running experiment via button under dish.")

    def pause_from_pop(self):
        """
        Pauses the experiment via the button underneath the dish.
        :return:
        """
        if not self.runpause_text_is_run():
            self.__click_runpause_pop_button()
            self.log.info("Paused experiment via button under dish.")

    def new_exp_dlg_displayed(self):
        """
        Determines if the dialog that is supposed to appear after clicking on
        the 'New' button under the dish is currently displayed on-screen.

        :return: True if dialog is displayed, False otherwise.
        """
        displayed = self.element_displayed(self.__new_dish_dlg)
        self.log.info("Is new experiment dialog displayed? " + str(displayed))
        return displayed

    def click_new_exp_nodlg(self):
        """
        Clicks on the 'New' button under the dish to create a new experiment.
        This method does not have any way of handling the dialog that may appear
        afterwards. Typically this would be a private method, but it is not
        because this method may be useful for testing purposes.

        :return: None.
        """
        self.click_element(self.__new_dish_button)
        self.log.info("Clicked on New button without plan for dialog.")

    def __click_new_exp(self):
        """
        Clicks on the 'New' button under the dish to create a new experiment.
        This method should be used only when expecting the new experiment dialog
        (which contains options for what to do with previous dish) to pop up, i.e.
        when there is something in the old dish.

        :return: None.
        """
        self.click_element(self.__new_dish_button)
        if self.wait_until_visible(self.__new_dish_dlg) and self.new_exp_dlg_displayed():
            self.log.info("Opened new experiment dialog.")
        else:
            self.log.warning("Failed to open new dish dialog.")

    def new_exp_cancel(self):
        """
        Clicks on the 'New' button under the dish to create a new experiment. It
        will cancel the operation once the dialog box comes up.

        :return: None.
        """
        self.__click_new_exp()
        self.click_element(self.__new_dish_cancel_xpath, "xpath")
        if self.wait_until_invisible(self.__new_dish_dlg):
            self.log.info("Cancelled New dish and closed dialog box.")
        else:
            self.log.warning("Dialog box still open -- attempt to cancel new dish action failed.")

    def new_exp_discard(self):
        """
        Clicks on the 'New' button under the dish to create a new experiment. It
        will discard the contents of the dish.

        :return: None.
        """
        self.__click_new_exp()
        self.click_element(self.__new_dish_discard_xpath, "xpath")
        if self.wait_until_invisible(self.__new_dish_dlg):
            self.log.info("Created new dish, closing dialog and discarding previous dish.")
        else:
            self.log.warning("Dialog box still open -- attempt to create new dish & discard old failed.")

    def new_exp_saveconf(self, name=None):
        """
        Clicks on the 'New' button under the dish to create a new experiment. It
        will save the dish configuration to the freezer.

        :param name: The name that the experiment configuration should be saved
        as.

        :return: None.
        """
        self.__click_new_exp()
        self.click_element(self.__new_dish_saveconf_xpath, "xpath")
        name_popup = self.switch_to_alert()
        passing_log_text = ""
        failing_log_text = ""
        if name is not None:
            name_popup.send_keys(name)
            passing_log_text = "Created new dish, saved old dish conf. as " + name + "."
            failing_log_text = "Dialog box still open -- attempt to create new dish & save old dish conf. as " + name  \
                               + " failed."
        else:
            passing_log_text = "Carried through with New, saved dish conf. with default name."
            failing_log_text = "Dialog box still open -- attempt to create new dish & save old dish conf. w/def. name" \
                               " failed."
        name_popup.accept()
        if self.wait_until_invisible(self.__new_dish_dlg):
            self.log.info(passing_log_text)
        else:
            self.log.warning(failing_log_text)

    def new_exp_savepop(self, name=None):
        """
        Clicks on the 'New' button under the dish to create a new experiment. It
        will save the populated dish to the freezer.

        :param name: The name that the populated dish should be saved as.

        :return: None.
        """
        self.__click_new_exp()
        self.click_element(self.__new_dish_savepop_xpath, "xpath")
        passing_log_text=""
        failing_log_text=""
        name_popup = self.switch_to_alert()
        if name is not None:
            name_popup.send_keys(name)
            passing_log_text = "Created new dish, saved populated dish as " + name + "."
            failing_log_text = "Dialog box still open -- attempt to create new dish & save old dish pop. as " + name   \
                               + " failed."
        else:
            passing_log_text = "Carried through with New, saved populated dish with default name."
            failing_log_text = "Dialog box still open -- attempt to create new dish & save old dish pop w/def. name"   \
                               " failed."
        name_popup.accept()
        if self.wait_until_invisible(self.__new_dish_dlg):
            self.log.info(passing_log_text)
        else:
            self.log.warning(failing_log_text)

    def forward_from_pop(self):
        """
        Moves the experiment forward by one update by clicking on the 'Forward'
        button
        :return:
        """
        self.click_element(self.__forward_button)
        self.log.info("Moved forward one update via 'Forward' button under dish"
                      ".")

    def get_update_ui_text(self):
        """
        Gets the text from the UI element containing information about the
        simulation update/time.

        :return: String containing update information.
        """
        update_text = self.get_text(self.__update_text)
        self.log.info("Got update number from ui: text is " + update_text)
        return update_text

    def edit_dish_cols(self, cols_num):
        """
        Edits the dish column number in the environmental settings panel.

        :param cols_num: String containing input to the text box.

        :return: None.
        """
        self.show_env_settings()
        cols_box = self.get_element(self.__dish_cols_box)
        cols_box.clear()
        self.send_keys(element=cols_box, keys=cols_num)
        self.hide_env_settings()
        self.log.info("Edited dish column number to " + str(cols_num))

    def edit_dish_rows(self, rows_num):
        """
        Edits the dish row number in the environmental settings panel.

        :param rows_num: String containing input to the text box.

        :return: None.
        """
        self.show_env_settings()
        rows_box = self.get_element(self.__dish_rows_box)
        rows_box.clear()
        self.send_keys(element=rows_box, keys=rows_num)
        self.hide_env_settings()
        self.log.info("Edited dish row number to " + str(rows_num))

    def edit_mut_rate(self, rate):
        """
        Edits the dish mutation rate in the environmental settings panel.

        :param rate: The input to be sent to the mutation rate box.

        :return: None.
        """
        self.show_env_settings()
        mut_rate_box = self.get_element(self.__mut_rate_input)
        mut_rate_box.clear()
        self.send_keys(element=mut_rate_box, keys=str(rate))
        self.hide_env_settings()
        self.log.info("Edited population mutation rate to " + str(rate))

    def pause_at_update_enabled(self):
        """
        Determines if 'Pause at update' feature is turned on.

        :return: True if pause on update enabled; False otherwise.
        """
        self.show_env_settings()
        is_enabled = self.get_attr_value(my_locator=self.__auto_update_btn,
                                         attr=self.__update_radio_attr)
        to_return = False
        if is_enabled == "true":
            to_return = True
        self.log.info("Is 'pause on update' enabled? " + str(to_return))
        self.hide_env_settings()
        return to_return

    def enable_pause_at_update(self):
        """
        Enables 'Pause on update' feature.

        :return: None.
        """
        if not self.pause_at_update_enabled():
            self.show_env_settings()
            self.click_element(self.__auto_update_btn)
            self.log.info("Set Pause mode to 'Pause on Update'.")
            self.hide_env_settings()

    def pause_manually_enabled(self):
        """
        Determines if 'Pause at' is set to 'manual'.

        :return: True if pause is set to manual; False otherwise.
        """
        self.show_env_settings()
        is_enabled = self.get_attr_value(my_locator=self.__manual_update_btn,
                                         attr=self.__update_radio_attr)
        to_return = False
        if is_enabled == "true":
            to_return = True
        self.log.info("Is 'pause manually' enabled? " + str(to_return))
        self.hide_env_settings()
        return to_return

    def enable_pause_manually(self):
        """
        Enables 'Pause Manually' mode (which turns on 'Pause at Update').

        :return: None.
        """
        if not self.pause_manually_enabled():
            self.show_env_settings()
            self.click_element(self.__manual_update_btn)
            self.log.info("Set pause mode to 'Pause Manually'.")
            self.hide_env_settings()

    def edit_pause_update(self, update):
        """
        Edits the update at which the experiment will pause if the 'Pause at
        Update' feature is turned on.

        :param update: The integer value of the update that the experiment
        should pause at.

        :return: None.
        """
        self.show_env_settings()
        pause_update_box = self.get_element(self.__pause_update_input)
        pause_update_box.clear()
        self.send_keys(element=pause_update_box, keys=str(update))
        self.hide_env_settings()
        self.log.info("Edited 'pause at update' to update " + str(update))

    def get_pop_current_update(self):
        """
        Gets the current update from av.grd.PopStatsMsg.

        This is the main storage for this value as opposed to the info stored in
        the Plotly graph.

        :return: Integer value of current update.
        """
        return self.execute_script("return av.grd.popStatsMsg.update")

    def get_pop_num_orgs(self):
        """
        Gets the current number of organisms from av.grd.PopStatsMsg.

        This is the main storage for this value as opposed to the info stored in
        the Plotly graph.

        :return: Integer value of current count of all organisms in dish.
        """
        return self.execute_script("return av.grd.popStatsMsg.organisms")

    def get_pop_avg_fit(self):
        """
        Gets the current average organism fitness from av.grd.PopStatsMsg.

        This is the main storage for this value as opposed to the info stored in
        the Plotly graph.

        :return: Float value of the average fitness.
        """
        return self.execute_script("return av.grd.popStatsMsg.ave_fitness")

    def get_pop_avg_age(self):
        """
        Gets the current average organism age from av.grd.PopStatsMsg.

        :return: Float value of the average age.
        """
        return self.execute_script("return av.grd.popStatsMsg.ave_age")

    def get_pop_avg_offspring_cost(self):
        """
        Gets the current average offspring cost from av.grd.PopStatsMsg.

        This is the main storage for this value as opposed to the info stored in
        the Plotly graph.

        :return: Integer value of current update.
        """
        return self.execute_script("return av.grd.popStatsMsg.ave_gestation_time")

    def get_pop_avg_energy_rate(self):
        """
        Gets the current avg. energy acquisition rate from av.grd.PopStatsMsg.

        This is the main storage for this value as opposed to the info stored in
        the Plotly graph.

        :return: Integer value of avg. energy acquisition rate.
        """
        return self.execute_script("return av.grd.popStatsMsg.ave_metabolic_rate")

    def get_pop_num_performing_not(self):
        """
        Gets the current number of organisms that can take advantage of notose
        resource.

        :return: Number of orgs that can perform 'not'.
        """
        return self.execute_script("return av.grd.popStatsMsg.not")

    def get_pop_num_performing_nan(self):
        """
        Gets the current number of organisms that can take advantage of nanose
        resource.

        :return: Number of orgs that can perform 'nan'.
        """
        return self.execute_script("return av.grd.popStatsMsg.nand")

    def get_pop_num_performing_and(self):
        """
        Gets the current number of organisms that can take advantage of andose
        resource.

        :return: Number of orgs that can perform 'and'.
        """
        return self.execute_script("return av.grd.popStatsMsg.and")

    def get_pop_num_performing_orn(self):
        """
        Gets the current number of organisms that can take advantage of ornose
        resource.

        :return: Number of orgs that can perform 'orn'.
        """
        return self.execute_script("return av.grd.popStatsMsg.orn")

    def get_pop_num_performing_oro(self):
        """
        Gets the current number of organisms that can take advantage of orose
        resource.

        :return: Number of orgs that can perform 'oro'.
        """
        return self.execute_script("return av.grd.popStatsMsg.or")

    def get_pop_num_performing_ant(self):
        """
        Gets the current number of organisms that can take advantage of andnose
        resource.

        :return: Number of orgs that can perform 'ant'.
        """
        return self.execute_script("return av.grd.popStatsMsg.andn")

    def get_pop_num_performing_nor(self):
        """
        Gets the current number of organisms that can take advantage of norose
        resource.

        :return: Number of orgs that can perform 'nor'.
        """
        return self.execute_script("return av.grd.popStatsMsg.nor")

    def get_pop_num_performing_xor(self):
        """
        Gets the current number of organisms that can take advantage of xorose
        resource.

        :return: Number of orgs that can perform 'xor'.
        """
        return self.execute_script("return av.grd.popStatsMsg.xor")

    def get_pop_num_performing_equ(self):
        """
        Gets the current number of organisms that can take advantage of equose
        resource.

        :return: Number of orgs that can perform 'equ'.
        """
        return self.execute_script("return av.grd.popStatsMsg.equ")

    def gr_get_pop_current_update(self):
        """
        Gets the current update from av.grd.updateNum.

        Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: Integer value of the current update.
        """
        return self.execute_script("return av.grd.updateNum")

    def __gr_get_pop_num_orgs_list(self):
        """
        Gets the list of the current amount of organisms for each update from
        av.pch.

         Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: List of integers with number of organisms in dish at each
        update.
        """
        return self.execute_script("return av.pch.aveNum")

    def gr_get_pop_curr_num_orgs(self):
        """
        Gets the current number of organisms from av.pch.

        :return: Integer value of current number of organisms.
        """
        return self.__gr_get_pop_num_orgs_list()[-1]

    def __gr_get_pop_avg_fitness_list(self):
        """
        Gets the list of average fitnesses for each update in experiment.

        :return: List of average fitnesses (floats).
        """
        return self.execute_script("return av.pch.aveFit")

    def gr_get_pop_curr_avg_fit(self):
        """
        Gets the current average fitness from av.pch.

        Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: Float value of average fitness.
        """
        return self.__gr_get_pop_avg_fitness_list()[-1]

    def __gr_get_pop_avg_rate(self):
        """
        Gets list of average energy acquisition rates for each update in exp.

        Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: List of average rates.
        """
        return self.execute_script("return av.pch.aveEar")

    def gr_get_pop_curr_avg_rate(self):
        """
        Gets the current average energy acquisition rate from av.pch.

        Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: Float value of average energy acquisition rate.
        """
        return self.__gr_get_pop_avg_rate()[-1]

    def __gr_get_pop_avg_cost(self):
        """
        Gets list of average offspring cost for each update in experiment.

        :return: List of average offspring cost.
        """
        return self.execute_script("return av.pch.aveCst")

    def gr_get_pop_curr_avg_cost(self):
        """
        Gets the current average offspring cost from av.pch.

        Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: Float value of average offspring cost.
        """
        return self.__gr_get_pop_avg_cost()[-1]

    def get_pop_cols(self):
        """
        Gets the current number of columns in the dish grid.

        :return: Integer value of columns in dish.
        """
        return self.execute_script("return av.grd.cols")

    def get_pop_rows(self):
        """
        Gets the current number of columns in the dish grid.

        :return: Integer value of rows in dish.
        """
        return self.execute_script("return av.grd.rows")

    def get_pop_mute_rate_string(self):
        """
        Gets the current mutation rate (for the experiment in the population
        window.

        NOTE: Returns the string because although the mutation rate should be an
        integer, you can easily put in a non-integer value.

        :return: String containing the current mutation rate.
        """
        return self.execute_script("return av.dom.muteInput.value")
