from base.driver_wrapper import DriverWrapper
from utilities.custom_logger import create_custom_logger
from utilities.util_methods import UtilityMethods


class BasePage(DriverWrapper):
    """
    Class that provides features common to all aspects of the Avida-ED website.
    """

    # Logger object for the BasePage
    log = create_custom_logger()

    # Utilties class that provides simple methods (particularly a wrapper for
    # time.sleep.
    util = UtilityMethods()

    # Locators for main sections of site.
    _population_block = "populationBlock"
    _organism_block = "organismBlock"
    _analysis_block = "analysisBlock"

    # Locators for buttons to switch between sections.
    _population_button = "populationButton"
    _organism_button = "organismButton"
    _analysis_button = "analysisButton"

    # Name of class that is applied to selected tabs in the main menu bar.
    _item_selected = "dijitMenuItemSelected"

    # Name of class that is applied to disabled menu options in main menu bar.
    _item_disabled = "dijitMenuItemDisabled"

    #Locators for dropdowns in the main menu bar.
    _avida_ed_tab = "mnAvidaEd"
    _file_tab = "mnFile"
    _freezer_tab = "mnFreezer"
    _control_tab = "mnControl"
    _help_tab = "mnHelp"

    # Locators for options within the Avida-ED dropdown.
    _avida_ed_about_menu = "dijit_Menu_0"
    _avida_ed_about_dlg = "dijit_Dialog_6"
    _avida_ed_about_closedlg = "mnHpAboutCancel"

    # Locators for options within the File dropdown.
    _file_save_workspace = "mnFlSaveWorkspace"
    _file_save_workspace_as = "mnFlSaveAs"
    _file_open_def_workspace = "mnFlOpenDefaultWS"
    _file_open_workspace = "mnFlOpenWS"
    _file_import_freezer_item = "mnFlFzItem"
    _file_export_data = "mnFlExportData"
    _file_export_graph = "mnFlExportGraph"
    _file_export_graph_dlg = "dijit_Dialog_1"
    _file_export_graph_closedlg = "mnFlExportGraphCancel"

    # Locators for options within the Freezer dropdown.
    _fz_save_exp_conf = "mnFzConfig"
    _fz_save_pop = "mnFzPopulation"
    _fz_save_org = "mnFzOrganism"
    _fz_save_offspring = "mnFzOffspring"
    _fz_add_conf_dish = "mnFzAddConfigEx"
    _fz_add_org = "mnFzAddGenomeEx"
    _fz_add_pop_dish = "mnFzAddPopEx"

    # Locators for options within the Control dropdown.
    _cn_run = "mnCnRun"
    _cn_pause = "mnCnPause"
    _cn_one_update = "mnCnOne"
    _cn_new_exp = "mnCnNewpop"
    _cn_bring_to_org = "mnCnOrganismTrace"
    _cn_bring_offspring_to_org = "mnCnOffspringTrace"

    # Locators for options within the Help dropdown.


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

    def population_displayed(self):
        """
        Checks if the population pane is currently displayed.

        :return: True if the population pane is displayed, false otherwise. 
        """
        pop_displayed = self.element_displayed(self._population_block)
        return pop_displayed

    def go_to_population(self):
        """
        Navigates to the "Population" pane of the Avida-ED website.
        :return: None.
        """
        self.click_element(self._population_button)

    def organism_displayed(self):
        """
        Checks if the organism pane is currently displayed.

        :return: True if the organism pane is displayed, false otherwise.
        """
        org_displayed = self.element_displayed(self._organism_block)
        return org_displayed

    def go_to_organism(self):
        """
        Navigates to the "Organism" pane of the Avida-ED website.
        :return: None.
        """
        self.click_element(self._organism_button)

    def analysis_displayed(self):
        """
        Checks if the analysis pane is currently displayed.

        :return: True if the analysis pane is displayed, false otherwise. 
        """
        ana_displayed = self.element_displayed(self._analysis_block)
        return ana_displayed

    def go_to_analysis(self):
        """
        Navigates to the "Analysis" pane of the Avida-ED website.
        :return: None.
        """
        self.click_element(self._analysis_button)

    def menu_dropdown_expanded(self, my_locator, locator_type="id"):
        """
        Determines whether the dropdown on a menu option is currently displayed.

        :param my_locator: Locator used to find the element on the site.

        :param locator_type: Type of locator that my_locator is; could be an ID,
        CSS selector, etc.

        :return: True if the dropdown is expanded, false otherwise.
        """
        if self.element_has_class(my_locator, locator_type,
                                  self._item_selected):
            return True
        return False

    def menu_item_disabled(self, my_locator, locator_type="id"):
        """
        Determines if a menu option in the main menu bar is disabled.

        :param my_locator: The locator used to find the menu item.

        :param locator_type: Type of locator that my_locator is; could be ID,
        CSS Selector, etc.

        :return: True if the menu item is disabled, False otherwise.
        """
        if self.element_has_class(my_locator,
                                  locator_type,
                                  self._item_disabled):
            return True
        return False

    def avida_ed_dropdown_expanded(self):
        """
        Determines whether the "Avida-ED" dropdown at the top of the page is
        expanded.

        :return: True if the dropdown is expanded, false otherwise.
        """
        if self.menu_dropdown_expanded(self._avida_ed_tab):
            return True
        return False

    def click_avida_ed_dropdown(self):
        """
        Clicks on the Avida-ED dropdown menu.

        :return: None.
        """
        self.click_element(self._avida_ed_tab)

    def open_avida_ed_dropdown(self):
        """
        Expands the Avida-ED dropdown menu at the top of the page.

        :return: None.
        """
        if not self.avida_ed_dropdown_expanded():
            self.click_avida_ed_dropdown()

    def close_avida_ed_dropdown(self):
        """
        Closes the Avida-ED dropdown menu at the top of the page.

        :return: None.
        """
        if self.avida_ed_dropdown_expanded():
            self.click_avida_ed_dropdown()

    def avida_ed_about_displayed(self):
        """
        Determines whether the "About" dialog box (accessed through the
        "Avida-ED" tab on the main menu bar) is currently displayed.

        :return: True if the dialog box is displayed, false otherwise.
        """
        if self.element_displayed(self._avida_ed_about_dlg):
            return True
        return False

    def open_avida_ed_about(self):
        """
        Attempts to open the "About" dialog box (by clicking on the "About"
        option in the "Avida-ED" dropdown in the main menu bar).

        :return: None.
        """
        self.open_avida_ed_dropdown()
        self.click_element(self._avida_ed_about_menu)
        self.util.sleep(1)

    def close_avida_ed_about(self):
        """
        Attempts to close the "About" dialog box if it is currently open.

        :return: None.
        """
        if self.avida_ed_about_displayed():
            self.click_element(self._avida_ed_about_closedlg)
            self.util.sleep(1)

    def file_dropdown_expanded(self):
        """
        Determines whether the "File" dropdown at the top of the website has
        been expanded.

        :return: True if the dropdown is expanded, false otherwise.
        """
        if self.menu_dropdown_expanded(self._file_tab):
            return True
        return False

    def click_file_dropdown(self):
        """
        Clicks on the "File" dropdown menu.

        :return: None.
        """
        self.click_element(self._file_tab)

    def open_file_dropdown(self):
        """
        Expands the "File" dropdown at the top of the website.

        :return: None.
        """
        if not self.file_dropdown_expanded():
            self.click_file_dropdown()

    def close_file_dropdown(self):
        """
        Closes the "File" dropdown at the top of the website.

        :return: None.
        """
        if self.file_dropdown_expanded():
            self.click_file_dropdown()

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
        self.click_element(self._file_save_workspace)

    def save_current_workspace_as(self, workspace_name):
        """
        Clicks on the "Save Workspace As" option within the File tab of the main
        menu bar. This should cause a prompt to pop up asking for the name the
        workspace. Actually filling in this prompt with the given workspace name
        will be implemented later.

        ***Not Fully Implemented Yet ***

        :param workspace_name: The name that the workspace should be saved as.

        :return: None.
        """
        self.open_file_dropdown()
        self.click_element(self._file_save_workspace_as)

    def open_default_workspace(self):
        """
        Opens the default workspace by clicking on the "Open Default Workspace"
        option within the File tab of the main menu bar.

        :return: None.
        """
        self.open_file_dropdown()
        self.click_element(self._file_open_def_workspace)

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
        self.click_element(self._file_open_workspace)

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
        self.click_element(self._file_import_freezer_item)

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
        self.click_element(self._file_export_data)

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
            self.click_element(self._file_export_graph)

            # Opening the dialog takes some time, so we will wait a bit.
            self.util.sleep(1)

    def export_graphics_dialog_displayed(self):
        """
        Determines whether the dialog box that appears when the "Export
        Graphics" option is clicked on is visible on-screen.

        :return: True if the dialog box is displayed, False otherwise.
        """
        if self.element_displayed(self._file_export_graph_dlg):
            return True
        return False

    def close_export_graphics_dialog(self):
        """
        Closes the dialog box that explains how to take screenshots (which
        should appear on-screen when the "Export Graphics" option is clicked),
        if it is currently displayed.

        :return: None.
        """
        if self.export_graphics_dialog_displayed():
            self.click_element(self._file_export_graph_closedlg)

            # Closing the dialog takes some time, so we will wait a bit.
            self.util.sleep(1)
    def freezer_dropdown_expanded(self):
        """
        Determines whether the "Freezer" dropdown menu at the top of the page is
        expanded.

        :return: True if the dropdown is expanded, False otherwise.
        """
        if self.menu_dropdown_expanded(self._freezer_tab):
            return True
        return False

    def click_freezer_dropdown(self):
        """
        Clicks on the "Freezer" dropdown menu.

        :return: None.
        """
        self.click_element(self._freezer_tab)

    def open_freezer_dropdown(self):
        """
        Opens the "Freezer" dropdown menu.

        :return: None
        """
        if not self.freezer_dropdown_expanded():
            self.click_freezer_dropdown()

    def close_freezer_dropdown(self):
        """
        Closes the "Freezer" dropdown menu.

        :return: None.
        """
        if self.freezer_dropdown_expanded():
            self.click_freezer_dropdown()

    def save_exp_conf(self):
        """
        Clicks on the "Save Experiment Configuration" within the Freezer tab of
        the main menu bar.

        :return: None.
        """
        self.open_freezer_dropdown()
        self.click_element(self._fz_save_exp_conf)

    def can_save_current_pop(self):
        """
        Determines whether the option to "Save Current Population" within the
        Freezer tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, False otherwise.
        """
        if self.menu_item_disabled(self._fz_save_pop):
            return False
        return True

    def save_current_pop(self):
        """
        Saves the current population (if one can be saved). If the option is
        available, it should pop up an window that prompts the user to enter
        a name for the population. However, interacting with this prompt has not
        yet been implemented.

        *** Not Fully Implemented ***

        :return: None.
        """
        self.open_freezer_dropdown()
        if self.can_save_current_pop():
            self.click_element(self._fz_save_pop)

    def can_save_selected_org(self):
        """
        Determines whether the option to "Save Selected Organism" within the
        Freezer tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, False otherwise.
        """
        if self.menu_item_disabled(self._fz_save_org):
            return False
        return True

    def save_selected_org(self):
        """
        Saves the selected organism to the Freezer (if one is selected) by
        clicking on the "Save Selected Organism" option in the main menu bar.
        This should open up a prompt to give the organism a name, but
        interacting with this has not been implemented yet.

        *** Not Fully Implemented Yet ***

        :return: None.
        """
        self.open_freezer_dropdown()
        if self.can_save_selected_org():
            self.click_element(self._fz_save_org)

    def can_save_offspring_org(self):
        """
        Determines whether the "Save Offspring Organism" option in the Freezer
        tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, False otherwise.
        """
        if self.menu_item_disabled(self._fz_save_offspring):
            return False
        return True

    def save_offspring_org(self):
        """
        Saves the offspring organism from the Organism window (if possible) by
        clicking on the "Save Offspring Organism" option in the Freezer tab of
        the main menu bar. Interacting with the name prompt has not been
        implemented yet.

        *** Not Fully Implemented Yet ***

        :return: None.
        """
        self.open_freezer_dropdown()
        if self.can_save_offspring_org():
            self.click_element(self._fz_save_offspring)

    def add_config_dish_to_exp(self):
        """
        Clicks on the "Add Highlighted Configured Dish to Experiment" button in
        the Freezer tab of the main menu bar.

        *** Not Fully Implemented Yet ***

        :return: None.
        """
        self.open_freezer_dropdown()
        self.click_element(self._fz_add_conf_dish)

    def add_org_to_exp(self):
        """
        Clicks on the "Add Highlighted Organism to Experiment" button in the
        Freezer tab of the main menu bar.

        *** Not Fully Implemented Yet ***

        :return: None.
        """
        self.open_freezer_dropdown()
        self.click_element(self._fz_add_org)

    def add_pop_dish_to_exp(self):
        """
        Clicks on the "Add Highlighted Populated Dish to Experiment" button in
        the Freezer tab of the main menu bar.

        :return: None.
        """
        self.open_freezer_dropdown()
        self.click_element(self._fz_add_pop_dish)

    def control_dropdown_expanded(self):
        """
        Determines whether the "Control" dropdown within the menu bar is
        expanded.

        :return: True if the dropdown is expanded, false otherwise.
        """
        if self.menu_dropdown_expanded(self._control_tab):
            return True
        return False

    def click_control_dropdown(self):
        """
        Clicks on the "Control" dropdown in the menu bar.

        :return: None.
        """
        self.click_element(self._control_tab)

    def open_control_dropdown(self):
        """
        Opens up the "Control" dropdown in the menu bar.

        :return: None.
        """
        if not self.control_dropdown_expanded():
            self.click_control_dropdown()

    def close_control_dropdown(self):
        """
        Closes the "Control" dropdown in the menu bar.

        :return: None.
        """
        if self.control_dropdown_expanded():
            self.click_control_dropdown()

    def can_run_from_menu(self):
        """
        Determines whether the "Run" option in the Control tab of the main menu
        bar is clickable or grayed out.

        :return: True if the option is clickable, false otherwise.
        """
        if self.menu_item_disabled(self._cn_run):
            return False
        return True

    def run_from_menu(self):
        """
        Attempts to click on the "Run" option in the Control tab of the main
        menu.

        *** Not Fully Implemented Yet ***

        :return: None.
        """
        self.open_control_dropdown()
        if self.can_run_from_menu():
            self.click_element(self._cn_run)

    def can_pause_from_menu(self):
        """
        Determines whether the "Pause" option in the Control tab of the main
        menu is clickable or grayed out.

        :return: True if the option is clickable, False otherwise.
        """
        if self.menu_item_disabled(self._cn_pause):
            return False
        return True

    def pause_from_menu(self):
        """
        Attempts to click on the "Pause" option in the Control tab of the main
        menu.

        :return: None.
        """
        self.open_control_dropdown()
        if self.can_pause_from_menu():
            self.click_element(self._cn_pause)

    def do_one_update(self):
        """
        Clicks on the "Do One Update" option in the Control tab of the main menu
        bar.

        *** Not Fully Implemented Yet ***

        :return: None.
        """
        self.open_control_dropdown()
        self.click_element(self._cn_one_update)

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
        self.click_element(self._cn_new_exp)

    def can_bring_to_org_window(self):
        """
        Determines whether the "Put Selected Organism in Organism View" option
        in the Control tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, false otherwise.
        """
        if self.menu_item_disabled(self._cn_bring_to_org):
            return False
        return True

    def bring_to_org_window(self):
        """
        Clicks on the "Put Selected Organism in Organism View" option in the
        Control tab of the main menu bar, if the option is available.

        :return: None.
        """
        self.open_control_dropdown()
        if self.can_bring_to_org_window():
            self.click_element(self._cn_bring_to_org)

    def can_bring_child_to_org_window(self):
        """
        Determines whether the "Put Offspring in Organism View" option in the
        Control tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, false otherwise.
        """
        if self.menu_item_disabled(self._cn_bring_offspring_to_org):
            return False
        return True

    def bring_child_to_org_window(self):
        """
        Clicks on the "Put Offspring in Organism View" option in the Control tab
        of the main menu bar is clickable or grayed out.

        :return: None.
        """
        self.open_control_dropdown()
        if self.can_bring_child_to_org_window():
            self.click_element(self._cn_bring_offspring_to_org)

    def help_dropdown_expanded(self):
        """
        Determines whether the "Help" dropdown in the main menu bar on the site
        is expanded.

        :return: True if the dropdown is expanded, False otherwise.
        """
        if self.menu_dropdown_expanded(self._help_tab):
            return True
        return False

    def click_help_dropdown(self):
        """
        Clicks on the "Help" dropdown in the main menu bar.

        :return: None.
        """
        self.click_element(self._help_tab)

    def open_help_dropdown(self):
        """
        Opens the "Help" dropdown in the main menu bar.

        :return: None.
        """
        if not self.help_dropdown_expanded():
            self.click_help_dropdown()

    def close_help_dropdown(self):
        """
        Closes the "Help" dropdown in the main menu bar.

        :return: None.
        """
        if self.help_dropdown_expanded():
            self.click_help_dropdown()
