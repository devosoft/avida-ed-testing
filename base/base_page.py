from base.driver_wrapper import DriverWrapper
from utilities.custom_logger import create_custom_logger
from utilities.util_methods import UtilityMethods


class BasePage(DriverWrapper):
    """
    Class that provides features common to all aspects of the Avida-ED website.
    """

    # Logger object for the BasePage
    log = create_custom_logger()

    # Utilities class that provides simple methods (particularly a wrapper for
    # time.sleep.
    util = UtilityMethods()

    # Locators for main sections of site.
    __population_block = "populationBlock"
    __organism_block = "organismBlock"
    __analysis_block = "analysisBlock"

    # Locator for splash screen
    __splash_screen = "splash"

    # Locators for buttons to switch between sections.
    __population_button = "populationButton"
    __organism_button = "organismButton"
    __analysis_button = "analysisButton"

    # Name of class that is applied to selected tabs in the main menu bar.
    __item_selected = "dijitMenuItemSelected"

    # Name of class that is applied to disabled menu options in main menu bar.
    __dijit_item_disabled = "dijitMenuItemDisabled"

    # Locators for dropdowns in the main menu bar.
    __avida_ed_tab = "mnAvidaEd"
    __file_tab = "mnFile"
    __freezer_tab = "mnFreezer"
    __control_tab = "mnControl"
    __help_tab = "mnHelp"

    # Locators for options within the Avida-ED dropdown.
    __avida_ed_about_menu = "dijit_Menu_0"
    __avida_ed_about_dlg = "dijit_Dialog_7"
    __avida_ed_about_closedlg = "mnHpAboutCancel"

    # Locators for options within the File dropdown.
    __file_save_workspace = "mnFlSaveWorkspace"
    __file_save_workspace_as = "mnFlSaveAs"
    __file_open_def_workspace = "mnFlOpenDefaultWS"
    __file_open_workspace = "mnFlOpenWS"
    __file_import_freezer_item = "mnFlFzItem"
    __file_export_data = "mnFlExportData"
    __file_export_graph = "mnFlExportGraph"
    __file_export_graph_dlg = "dijit_Dialog_1"
    __file_export_graph_closedlg = "mnFlExportGraphCancel"

    # Locators for options within the Freezer dropdown.
    __fz_save_exp_conf = "mnFzConfig"
    __fz_save_pop = "mnFzPopulation"
    __fz_save_org = "mnFzOrganism"
    __fz_save_offspring = "mnFzOffspring"
    __fz_add_conf_dish = "mnFzAddConfigEx"
    __fz_add_org = "mnFzAddGenomeEx"
    __fz_add_pop_dish = "mnFzAddPopEx"
    __fz_bring_org_to_org_view = "mnFzAddGenomeView"
    __fz_bring_dish_to_ana_view = "mnFzAddPopAnalysis"

    # Locators for options within the Control dropdown.
    __cn_run = "mnCnRun"
    __cn_pause = "mnCnPause"
    __cn_one_update = "mnCnOne"
    __cn_new_exp = "mnCnNewpop"
    __cn_bring_to_org = "mnCnOrganismTrace"
    __cn_bring_offspring_to_org = "mnCnOffspringTrace"

    # Locator for crash report dialog box.
    __crash_dlg = "dijit_Dialog_11"

    # Locator for items in the Freezer
    __fz_item_xpath = "//*/div[@class='dojoDndItem']"

    # Class name for highlighted items in Freezer
    __fz_highlight_class = "dojoDndItemAnchor"

    def __init__(self, driver):
        """
        Initializes the BasePage object.

        Calls the constructor for the driver object which is passed in.

        :param driver: The underlying DriverWrapper object which interacts with
        the page.
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = UtilityMethods()

    def wait_until_splash_gone(self):
        """
        Waits for splash screen to go away.

        :return: None.
        """
        self.wait_until_invisible(my_locator=self.__splash_screen)

    def refresh_avida_ed(self):
        """
        Refreshes Avida-ED webpage.

        :return: None.
        """
        self.refresh_page()
        self.wait_until_splash_gone()

    def population_displayed(self):
        """
        Checks if the population pane is currently displayed.

        :return: True if the population pane is displayed, false otherwise. 
        """
        pop_displayed = self.element_displayed(self.__population_block)
        self.log.info("Checked if population window displayed: found to be "
                      + str(pop_displayed) + ".")
        return pop_displayed

    def go_to_population(self):
        """
        Navigates to the "Population" pane of the Avida-ED website.
        :return: None.
        """
        self.click_element(self.__population_button)
        self.log.info("Navigated to population window.")

    def organism_displayed(self):
        """
        Checks if the organism pane is currently displayed.

        :return: True if the organism pane is displayed, false otherwise.
        """
        org_displayed = self.element_displayed(self.__organism_block)
        self.log.info("Checked if organism window displayed: found to be "
                      + str(org_displayed) + ".")

        return org_displayed

    def go_to_organism(self):
        """
        Navigates to the "Organism" pane of the Avida-ED website.
        :return: None.
        """
        self.click_element(self.__organism_button)
        self.log.info("Navigated to organism window.")

    def analysis_displayed(self):
        """
        Checks if the analysis pane is currently displayed.

        :return: True if the analysis pane is displayed, false otherwise. 
        """
        ana_displayed = self.element_displayed(self.__analysis_block)
        self.log.info("Checked if analysis window displayed: found to be "
                      + str(ana_displayed) + ".")
        return ana_displayed

    def go_to_analysis(self):
        """
        Navigates to the "Analysis" pane of the Avida-ED website.
        :return: None.
        """
        self.click_element(self.__analysis_button)
        self.log.info("Navigated to analysis window.")

    def crash_report_displayed(self):
        """
        Checks if the crash report dialog box is displayed.

        :return: True if the dialog is displayed, False otherwise.
        """
        return self.element_displayed(self.__crash_dlg)

    def freezer_item_highlighted(self, text_name):
        """
        Checks to see if there are any highlighted Freezer items with text
        text_name.

        :param text_name: The text title of the item (e.g. @ancestor).

        :return: True if the item exists and is highlighted, False otherwise.
        """
        item = self.__get_freezer_item(text_name)

        highlighted = False
        if item is not None:
            highlighted = self.element_has_class(
                class_name=self.__fz_highlight_class,
                element=item)

        self.log.info("Is freezer item with name " + text_name
                      + " highlighted? " + str(highlighted))
        return highlighted

    def click_freezer_item(self, text_name):
        """
        Clicks on a Freezer Item with text text_name.

        :param text_name: The text title of the item (e.g. @ancestor).

        :return: None.
        """
        item = self.__get_freezer_item(text_name)
        if item is not None:
            self.click_element(element=item)
            self.log.info("Clicked on freezer item with name " + text_name)
        else:
            self.log.info("Failed to click on any freezer item with name "
                          + text_name)

    def avida_ed_dropdown_expanded(self):
        """
        Determines whether the "Avida-ED" dropdown at the top of the page is
        expanded.

        :return: True if the dropdown is expanded, false otherwise.
        """
        expanded = self.__menu_dropdown_expanded(self.__avida_ed_tab)
        self.log.info("Is Avida-ED dropdown expanded? " + str(expanded))
        return expanded

    def open_avida_ed_dropdown(self):
        """
        Expands the Avida-ED dropdown menu at the top of the page.

        :return: None.
        """
        if not self.avida_ed_dropdown_expanded():
            self.__click_avida_ed_dropdown()
            self.log.info("Opened Avida-ED dropdown.")

    def close_avida_ed_dropdown(self):
        """
        Closes the Avida-ED dropdown menu at the top of the page.

        :return: None.
        """
        if self.avida_ed_dropdown_expanded():
            self.__click_avida_ed_dropdown()
            self.log.info("Closed Avida-ED dropdown.")

    def avida_ed_about_displayed(self):
        """
        Determines whether the "About" dialog box (accessed through the
        "Avida-ED" tab on the main menu bar) is currently displayed.

        :return: True if the dialog box is displayed, false otherwise.
        """
        displayed = self.element_displayed(self.__avida_ed_about_dlg)
        self.log.info("Is 'About' dialog box in Avida-ED tab displayed? "
                      + str(displayed))
        return displayed

    def open_avida_ed_about(self):
        """
        Attempts to open the "About" dialog box (by clicking on the "About"
        option in the "Avida-ED" dropdown in the main menu bar).

        :return: None.
        """
        self.open_avida_ed_dropdown()
        self.click_element(self.__avida_ed_about_menu)
        self.log.info("Opened 'About' dialog box in Avida-ED tab.")

        # Wait (because opening can take a while).
        self.util.sleep(1)

    def close_avida_ed_about(self):
        """
        Attempts to close the "About" dialog box if it is currently open.

        :return: None.
        """
        if self.avida_ed_about_displayed():
            self.click_element(self.__avida_ed_about_closedlg)
            self.log.info("Closed 'About' dialog box in Avida-ED tab.")

            # Wait (because closing can take a while).
            self.util.sleep(1)

    def file_dropdown_expanded(self):
        """
        Determines whether the "File" dropdown at the top of the website has
        been expanded.

        :return: True if the dropdown is expanded, false otherwise.
        """
        expanded = self.__menu_dropdown_expanded(self.__file_tab)
        self.log.info("Is File dropdown expanded? " + str(expanded))
        return expanded

    def open_file_dropdown(self):
        """
        Expands the "File" dropdown at the top of the website.

        :return: None.
        """
        if not self.file_dropdown_expanded():
            self.__click_file_dropdown()
            self.log.info("Opened File tab.")

    def close_file_dropdown(self):
        """
        Closes the "File" dropdown at the top of the website.

        :return: None.
        """
        if self.file_dropdown_expanded():
            self.__click_file_dropdown()
            self.log.info("Closed File tab.")

    def save_current_workspace(self):
        """
        Clicks on the "Save Current Workspace" option within the File tab of the
        main menu bar. This should initiate the download process of a .zip file
        containing the current workspace. On Firefox, it opens a prompt first --
        this has not been accounted for as of yet.

        *** Only works properly with Chrome for now ***

        :return: None.
        """
        self.open_file_dropdown()
        self.click_element(self.__file_save_workspace)
        self.log.info("Click on 'Save Current Workspace' in File tab.")

    def save_current_workspace_as(self, workspace_name):
        """
        Clicks on the "Save Workspace As" option within the File tab of the main
        menu bar. It then gives the resulting Javascript popup a filename for
        the workspace and accepts it, which results in the workspace being
        downloaded as a zip file.

        :param workspace_name: The name that the workspace should be saved as.

        :return: None.
        """
        self.open_file_dropdown()
        self.click_element(self.__file_save_workspace_as)
        self.log.info("Clicked on 'Save Current Workspace As' in File tab.")

        try:
            workspace_name_alert = self.switch_to_alert()
            workspace_name_alert.send_keys(workspace_name)
            workspace_name_alert.accept()
        except:
            self.log.info("Error occurred while interacting with 'Save"
                          " Workspace As' JS alert.")

    def open_default_workspace(self):
        """
        Opens the default workspace by clicking on the "Open Default Workspace"
        option within the File tab of the main menu bar.

        :return: None.
        """
        self.open_file_dropdown()
        self.click_element(self.__file_open_def_workspace)
        self.log.info("Clicked on 'Open Default Workspace' in File tab.")

    def open_workspace(self, workspace_path):
        """
        Clicks on the "Open Workspace" option within the File tab of the main
        menu bar. This should open a prompt to select a workspace on the local
        computer to open -- however, interacting with that window has not been
        implemented.

        *** Not Fully Implemented Yet ***

        :param workspace_path: The path where the workspace to be opened is
        located.

        :return: None.
        """
        self.open_file_dropdown()
        self.click_element(self.__file_open_workspace)
        self.log.info("Click on 'Open Workspace' in File tab.")

    def import_freezer_item(self, freezer_item_path):
        """
        Clicks on the "Import Freezer Item" option within the File tab of the
        main menu bar. This should open a prompt to select a saved freezer item
        on the local computer to open -- however, interacting with that window
        has not been implemented.

        *** Not Fully Implemented Yet ***

        :param freezer_item_path: The path where the freezer item to be opened
        is located.

        :return: None.
        """
        self.open_file_dropdown()
        self.click_element(self.__file_import_freezer_item)
        self.log.info("Clicked on 'Import Freezer Item' in File tab.")

    def export_data(self):
        """
        Clicks on the "Export Data" option within the File tab of the main menu
        bar. This should cause a .csv file containing Avida-ED info to be
        downloaded (or a prompt will show up in Firefox, which has not been
        accounted for yet.

        *** Only works with Chrome for now ***

        :return: None.
        """
        self.open_file_dropdown()
        self.click_element(self.__file_export_data)
        self.log.info("Clicked on 'Export Data' in the File tab.")

    def export_graphics(self):
        """
        Clicks on the "Export Graphics" option within the File tab of the main
        menu bar. Because exporting graphics from Avida-ED has not yet been
        implemented, this simply opens up a dialog box that explains how to
        take a screenshot using standard OS-level tools.

        :return: None.
        """
        if not self.export_graphics_dialog_displayed():
            self.open_file_dropdown()
            self.click_element(self.__file_export_graph)
            self.log.info("Clicked on 'Export Graphics' in File tab.")

            # Opening the dialog takes some time, so we will wait a bit.
            self.util.sleep(1)

    def export_graphics_dialog_displayed(self):
        """
        Determines whether the dialog box that appears when the "Export
        Graphics" option is clicked on is visible on-screen.

        :return: True if the dialog box is displayed, False otherwise.
        """
        displayed = self.element_displayed(self.__file_export_graph_dlg)
        self.log.info("Is 'Export Graphics' dialog box displayed? "
                      + str(displayed))
        return displayed

    def close_export_graphics_dialog(self):
        """
        Closes the dialog box that explains how to take screenshots (which
        should appear on-screen when the "Export Graphics" option is clicked),
        if it is currently displayed.

        :return: None.
        """
        if self.export_graphics_dialog_displayed():
            self.click_element(self.__file_export_graph_closedlg)
            self.log.info("Closed export graphics dialog.")

            # Closing the dialog takes some time, so we will wait a bit.
            self.util.sleep(1)

    def freezer_dropdown_expanded(self):
        """
        Determines whether the "Freezer" dropdown menu at the top of the page is
        expanded.

        :return: True if the dropdown is expanded, False otherwise.
        """
        expanded = self.__menu_dropdown_expanded(self.__freezer_tab)
        self.log.info("Is Freezer dropdown expanded? " + str(expanded))
        return expanded

    def open_freezer_dropdown(self):
        """
        Opens the "Freezer" dropdown menu.

        :return: None
        """
        if not self.freezer_dropdown_expanded():
            self.__click_freezer_dropdown()
            self.log.info("Opened Freezer dropdown.")

    def close_freezer_dropdown(self):
        """
        Closes the "Freezer" dropdown menu.

        :return: None.
        """
        if self.freezer_dropdown_expanded():
            self.__click_freezer_dropdown()
            self.log.info("Closed Freezer dropdown.")

    def save_exp_conf(self, name=None):
        """
        Clicks on the "Save Experiment Configuration" within the Freezer tab of
        the main menu bar. It then gives a name to the configuration and accepts
        the name by interacting with the Javascript alert.

        :param name: The name that the exp. configuration will be given.

        :return: None.
        """
        self.open_freezer_dropdown()
        self.click_element(self.__fz_save_exp_conf)
        self.log.info("Clicked 'Save Experiment Configuration' button in"
                      " Freezer tab.")
        try:
            name_exp_conf_alert = self.switch_to_alert()
            if name is not None:
                name_exp_conf_alert.send_keys(name)
            name_exp_conf_alert.accept()
            self.log.info("Successfully named our saved experiment "
                          " configuration '" + name + "'.")
        except:
            self.log.info("Error occurred while interacting with 'Save"
                          " Experiment Configuration' JS alert.")

    def can_save_current_pop(self):
        """
        Determines whether the option to "Save Current Population" within the
        Freezer tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, False otherwise.
        """
        clickable = not self.__menu_item_disabled(self.__fz_save_pop)
        self.log.info("Is 'Save Current Population' clickable? "
                      + str(clickable))
        return clickable

    def save_current_pop(self, name=None):
        """
        Saves the current population (if one can be saved). If the option is
        available, it should pop up an window that prompts the user to enter
        a name for the population. If a value is given to name argument, it
        will save the population with that name -- otherwise, it will save with
        whatever name Avida-ED suggests.

        :param name: The name that the population should be saved as.

        :return: None.
        """
        self.open_freezer_dropdown()
        if self.can_save_current_pop():
            self.click_element(self.__fz_save_pop)
            self.log.info("Successfully clicked on 'Save Current Population'"
                          " button in Freezer tab.")
            name_popup = self.switch_to_alert()
            if name is not None:
                name_popup.send_keys(name)
                self.log.info("Saving current population to freezer as '" + name
                              + "'.")
            else:
                self.log.info("Saving current population with default name.")
            name_popup.accept()

        else:
            self.log.info("Failed to click on 'Save Current Population' button"
                          " button in Freezer tab.")

    def can_save_selected_org(self):
        """
        Determines whether the option to "Save Selected Organism" within the
        Freezer tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, False otherwise.
        """
        clickable = not self.__menu_item_disabled(self.__fz_save_org)
        self.log.info("Is 'Save Selected Organism' clickable? "
                      + str(clickable))
        return clickable

    def save_selected_org(self, name=None):
        """
        Saves the selected organism to the Freezer (if one is selected) by
        clicking on the "Save Selected Organism" option in the main menu bar.
        This should open up a prompt to give the organism a name, but
        interacting with this has not been implemented yet.

        :param name: The name that the organism should be saved as.

        :return: None.
        """
        self.open_freezer_dropdown()
        if self.can_save_selected_org():
            self.click_element(self.__fz_save_org)
            self.log.info("Successfully clicked on 'Save Selected Organism' in"
                          " Freezer tab.")

            name_popup = self.switch_to_alert()
            if name is not None:
                name_popup.send_keys(name)
                self.log.info("Saving selected organism as '" + name + "'.")
            else:
                self.log.info("Saving selected organism with default name.")
            name_popup.accept()

        else:
            self.log.info("Failed to click on 'Save Selected Organism' in"
                          " Freezer tab.")

    def can_save_offspring_org(self):
        """
        Determines whether the "Save Offspring Organism" option in the Freezer
        tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, False otherwise.
        """
        clickable = not self.__menu_item_disabled(self.__fz_save_offspring)
        self.log.info("Can click on 'Save Offspring Organism'? "
                      + str(clickable))
        return clickable

    def save_offspring_org(self, name=None):
        """
        Saves the offspring organism from the Organism window (if possible) by
        clicking on the "Save Offspring Organism" option in the Freezer tab of
        the main menu bar. Interacting with the name prompt has not been
        implemented yet.

        :param name: The name that the offspring organism should be saved as.

        :return: None.
        """
        self.open_freezer_dropdown()
        if self.can_save_offspring_org():
            self.click_element(self.__fz_save_offspring)
            self.log.info("Successfully clicked on 'Save Offspring Organism'"
                          " button in Freezer tab.")

            name_popup = self.switch_to_alert()
            if name is not None:
                name_popup.send_keys(name)
                self.log.info("Saving offspring organism with name '" + name
                              + "'.")
            else:
                self.log.info("Saving offspring organism with default name.")
            name_popup.accept()

        else:
            self.log.info("Failed to click on 'Save Offspring Organism' button"
                          " in Freezer tab.")

    def add_config_dish_to_exp(self):
        """
        Clicks on the "Add Highlighted Configured Dish to Experiment" button in
        the Freezer tab of the main menu bar.

        *** Not Fully Implemented Yet ***

        :return: None.
        """
        self.open_freezer_dropdown()
        self.click_element(self.__fz_add_conf_dish)
        self.log.info("Clicked on 'Add Highlighted Configured Dish to"
                      " Experiment' button in Freezer tab.")

    def add_org_to_exp(self):
        """
        Clicks on the "Add Highlighted Organism to Experiment" button in the
        Freezer tab of the main menu bar.

        *** Not Fully Implemented Yet ***

        :return: None.
        """
        self.open_freezer_dropdown()
        self.click_element(self.__fz_add_org)
        self.log.info("Clicked on 'Add Highlighted Organism to Experiment'"
                      " button in Freezer tab.")

    def add_pop_dish_to_exp(self):
        """
        Clicks on the "Add Highlighted Populated Dish to Experiment" button in
        the Freezer tab of the main menu bar.

        :return: None.
        """
        self.open_freezer_dropdown()
        self.click_element(self.__fz_add_pop_dish)
        self.log.info("Clicked on 'Add Highlighted Populated Dish to"
                      " Experiment' button in Freezer tab.")

    def add_org_to_org_view(self):
        """
        Puts the currently highlighted organism into the Organism view.

        NOTE: Use of this function should be followed by
        wait_until_org_controls_enabled() call from OrganismPage. This ensures
        that the organism is fully loaded into the Organism View.

        :return: None.
        """
        self.open_freezer_dropdown()
        self.click_element(self.__fz_bring_org_to_org_view)
        self.log.info("Clicked on the 'Put Highlighted Organism in Organism"
                      " View' button in Freezer tab.")

    def add_dish_to_analysis(self):
        """
        Puts the currently highlighted populated dish into the Analysis view.

        :return: None.
        """
        self.open_freezer_dropdown()
        self.click_element(self.__fz_bring_dish_to_ana_view)
        self.log.info("Clicked on the 'Put Highlighted Populated Dish in"
                      " Analysis View' button in Freezer tab.")

    def control_dropdown_expanded(self):
        """
        Determines whether the "Control" dropdown within the menu bar is
        expanded.

        :return: True if the dropdown is expanded, false otherwise.
        """
        expanded = self.__menu_dropdown_expanded(self.__control_tab)
        self.log.info("Is Control dropdown expanded? " + str(expanded))
        return expanded

    def open_control_dropdown(self):
        """
        Opens up the "Control" dropdown in the menu bar.

        :return: None.
        """
        if not self.control_dropdown_expanded():
            self.__click_control_dropdown()
            self.log.info("Opening 'Control' dropdown menu.")

    def close_control_dropdown(self):
        """
        Closes the "Control" dropdown in the menu bar.

        :return: None.
        """
        if self.control_dropdown_expanded():
            self.__click_control_dropdown()
            self.log.info("Closing 'Control' dropdown menu.")

    def can_run_from_menu(self):
        """
        Determines whether the "Run" option in the Control tab of the main menu
        bar is clickable or grayed out.

        :return: True if the option is clickable, false otherwise.
        """
        clickable = not self.__menu_item_disabled(self.__cn_run)
        self.log.info("Is 'Run' clicakble? " + str(clickable))
        return clickable

    def run_from_menu(self):
        """
        Attempts to click on the "Run" option in the Control tab of the main
        menu.

        *** Not Fully Implemented Yet ***

        :return: None.
        """
        self.open_control_dropdown()
        if self.can_run_from_menu():
            self.click_element(self.__cn_run)
            self.log.info("Successfully clicked on 'Run' in Control tab.")
        else:
            self.log.info("Failed to click on 'Run' in Control tab.")

    def can_pause_from_menu(self):
        """
        Determines whether the "Pause" option in the Control tab of the main
        menu is clickable or grayed out.

        :return: True if the option is clickable, False otherwise.
        """
        clickable = not self.__menu_item_disabled(self.__cn_pause)
        self.log.info("Is 'Pause' clickable? " + str(clickable))
        return clickable

    def pause_from_menu(self):
        """
        Attempts to click on the "Pause" option in the Control tab of the main
        menu.

        :return: None.
        """
        self.open_control_dropdown()
        if self.can_pause_from_menu():
            self.click_element(self.__cn_pause)
            self.log.info("Successfully clicked on 'Pause' in Control tab via"
                          "the menu bar.")
        else:
            self.log.info("Failed to click on 'Pause' in Control tab via the"
                          "menu bar.")

    def forward_from_menu(self):
        """
        Clicks on the "Forward" option in the Control tab of the main menu
        bar.

        *** Not Fully Implemented Yet ***

        :return: None.
        """
        self.open_control_dropdown()
        self.click_element(self.__cn_one_update)
        self.log.info("Clicked on 'Forward' in Control tab via the menu bar.")

    def start_new_exp_from_menu(self):
        """
        Clicks on the "Start New Experiment" option in the Control tab of the
        main menu bar.

        In the future, will be able to handle prompts from Avida-ED to save work
        that pop up as a result of pressing the button.

        *** Not Fully Implemented Yet ***

        :return: None.
        """
        self.open_control_dropdown()
        self.click_element(self.__cn_new_exp)
        self.log.info("Clicked on 'Start New Experiment' in Control tab.")

    def can_bring_to_org_window(self):
        """
        Determines whether the "Put Selected Organism in Organism View" option
        in the Control tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, false otherwise.
        """
        clickable = not self.__menu_item_disabled(self.__cn_bring_to_org)
        self.log.info("Is 'Put Selected Organism in Organism View' clickable? "
                      + str(clickable))
        return clickable

    def bring_to_org_window(self):
        """
        Clicks on the "Put Selected Organism in Organism View" option in the
        Control tab of the main menu bar, if the option is available.

        :return: None.
        """
        self.open_control_dropdown()
        if self.can_bring_to_org_window():
            self.click_element(self.__cn_bring_to_org)
            self.log.info("Successfully clicked on 'Put Highlighted Organism in"
                          + " Organism View' button.")
        else:
            self.log.info("Tried but failed to click on 'Put Highlighted"
                          + " Organism in Organism View' button.")

    def can_bring_child_to_org_window(self):
        """
        Determines whether the "Put Offspring in Organism View" option in the
        Control tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, false otherwise.
        """
        clickable = not self.__menu_item_disabled(
            self.__cn_bring_offspring_to_org)

        self.log.info("Is 'Put Offspring in Organism View' button clickable? "
                      + str(clickable))
        return clickable

    def bring_child_to_org_window(self):
        """
        Clicks on the "Put Offspring in Organism View" option in the Control tab
        of the main menu bar is clickable or grayed out.

        :return: None.
        """
        self.open_control_dropdown()
        if self.can_bring_child_to_org_window():
            self.click_element(self.__cn_bring_offspring_to_org)
            self.log.info("Successfully clicked on Put Offspring in Organism "
                          + "View menu option.")
        else:
            self.log.info("Tried, but could not click on Put Organism in "
                          + "Offspring View menu option.")

    def help_dropdown_expanded(self):
        """
        Determines whether the "Help" dropdown in the main menu bar on the site
        is expanded.

        :return: True if the dropdown is expanded, False otherwise.
        """
        expanded = self.__menu_dropdown_expanded(self.__help_tab)
        self.log.info("Is Help menu dropdown expanded? "
                      + str(expanded) + ".")
        return expanded

    def open_help_dropdown(self):
        """
        Opens the "Help" dropdown in the main menu bar.

        :return: None.
        """
        if not self.help_dropdown_expanded():
            self.__click_help_dropdown()
            self.log.info("Opening Help menu dropdown.")

    def close_help_dropdown(self):
        """
        Closes the "Help" dropdown in the main menu bar.

        :return: None.
        """
        if self.help_dropdown_expanded():
            self.__click_help_dropdown()
            self.log.info("Closing Help menu dropdown.")

    def add_ancestor_to_dish(self):
        """
        Adds the @ancestor organism to the dish via the main menu.

        :return: None.
        """
        self.click_freezer_item("@ancestor")
        self.add_org_to_exp()
        self.log.info("Added @ancestor to dish.")

    def add_all_functions_to_dish(self):
        """
        Adds the @all_functions organism to the dish via the main menu.

        :return: None.
        """
        self.click_freezer_item("@all_functions")
        self.add_org_to_exp()
        self.log.info("Added @all_functions to dish.")

    ############################################################################
    # Methods below this point shouldn't be called outside this class.
    ############################################################################

    def __menu_dropdown_expanded(self, my_locator, locator_type="id"):
        """
        Determines whether the dropdown on a menu option is currently displayed.

        :param my_locator: Locator used to find the element on the site.

        :param locator_type: Type of locator that my_locator is; could be an ID,
        CSS selector, etc.

        :return: True if the dropdown is expanded, false otherwise.
        """
        expanded = self.element_has_class(my_locator, locator_type,
                                          self.__item_selected)
        self.log.info("Is dropdown menu with locator " + my_locator
                      + " of type " + locator_type + "expanded? "
                      + str(expanded) + ".")

        return expanded

    def __menu_item_disabled(self, my_locator, locator_type="id"):
        """
        Determines if a menu option in the main menu bar is disabled.

        :param my_locator: The locator used to find the menu item.

        :param locator_type: Type of locator that my_locator is; could be ID,
        CSS Selector, etc.

        :return: True if the menu item is disabled, False otherwise.
        """
        disabled = self.element_has_class(my_locator,
                                          locator_type,
                                          self.__dijit_item_disabled)
        self.log.info("Is menu item with locator " + my_locator + " of type "
                      + locator_type + " disabled? " + str(disabled))
        return disabled

    def __get_freezer_item(self, text_name):
        """
        Finds and returns a WebElement in the Freezer with matching text_name.

        :param text_name: The text title of the item (e.g. @ancestor).

        :return: The first WebElement with matching name (or None if no match
        found).
        """
        self.log.info("Attempting to find freezer item with name "
                      + text_name + ".")

        freezer_items = self.get_element_list(
            self.__fz_item_xpath,
            "xpath"
        )

        found = False

        for item in freezer_items:
            if self.get_text(element=item) == text_name:
                self.log.info("Freezer item found.")
                return item
            if not found:
                self.log.info("Freezer item not found.")
        return None

    def __click_avida_ed_dropdown(self):
        """
        Clicks on the Avida-ED dropdown menu.

        :return: None.
        """
        self.log.info("Clicking on Avida-ED main menu tab.")
        self.click_element(self.__avida_ed_tab)

    def __click_file_dropdown(self):
        """
        Clicks on the "File" dropdown menu.

        :return: None.
        """
        self.log.info("Clicking on File main menu tab.")
        self.click_element(self.__file_tab)

    def __click_freezer_dropdown(self):
        """
        Clicks on the "Freezer" dropdown menu.

        :return: None.
        """
        self.log.info("Clicking on Freezer main menu tab.")
        self.click_element(self.__freezer_tab)

    def __click_control_dropdown(self):
        """
        Clicks on the "Control" dropdown in the menu bar.

        :return: None.
        """
        self.log.info("Clicking on Control main menu tab.")
        self.click_element(self.__control_tab)

    def __click_help_dropdown(self):
        """
        Clicks on the "Help" dropdown in the main menu bar.

        :return: None.
        """
        self.click_element(self.__help_tab)
        self.log.info("Clicked on Help main menu tab.")
