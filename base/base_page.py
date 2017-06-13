from base.driver_wrapper import DriverWrapper
from utilities.custom_logger import create_custom_logger
from utilities.util_methods import UtilityMethods


class BasePage(DriverWrapper):
    """
    Class that provides features common to all aspects of the Avida-ED website.
    """

    log = create_custom_logger()

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
        pop_displayed = self.element_displayed("populationBlock")
        return pop_displayed

    def go_to_population(self):
        """
        Navigates to the "Population" pane of the Avida-ED website.
        :return: None.
        """
        self.click_element("populationButton")

    def organism_displayed(self):
        """
        Checks if the organism pane is currently displayed.

        :return: True if the organism pane is displayed, false otherwise.
        """
        org_displayed = self.element_displayed("organismBlock")
        return org_displayed

    def go_to_organism(self):
        """
        Navigates to the "Organism" pane of the Avida-ED website.
        :return: None.
        """
        self.click_element("organismButton")

    def analysis_displayed(self):
        """
        Checks if the analysis pane is currently displayed.

        :return: True if the analysis pane is displayed, false otherwise. 
        """
        ana_displayed = self.element_displayed("analysisBlock")
        return ana_displayed

    def go_to_analysis(self):
        """
        Navigates to the "Analysis" pane of the Avida-ED website.
        :return: None.
        """
        self.click_element("analysisButton")

    def menu_dropdown_expanded(self, my_locator, locator_type="id"):
        """
        Determines whether the dropdown on a menu option is currently displayed.

        :param my_locator: Locator used to find the element on the site.

        :param locator_type: Type of locator that my_locator is; could be an ID,
        CSS selector, etc.

        :return: True if the dropdown is expanded, false otherwise.
        """
        if self.element_has_class(my_locator, locator_type,
                                  "dijitMenuItemSelected"):
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
        if self.element_has_class(my_locator, locator_type,
                                  "dijitMenuItemDisabled"):
            return True
        return False

    def avida_ed_dropdown_expanded(self):
        """
        Determines whether the "Avida-ED" dropdown at the top of the page is
        expanded.

        :return: True if the dropdown is expanded, false otherwise.
        """
        if self.menu_dropdown_expanded("mnAvidaEd"):
            return True
        return False

    def click_avida_ed_dropdown(self):
        """
        Clicks on the Avida-ED dropdown menu.

        :return: None.
        """
        self.click_element("mnAvidaEd")

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
        if self.element_displayed("dijit_Dialog_6"):
            return True
        return False

    def open_avida_ed_about(self):
        """
        Attempts to open the "About" dialog box (by clicking on the "About"
        option in the "Avida-ED" dropdown in the main menu bar).

        :return: None.
        """
        self.open_avida_ed_dropdown()
        self.click_element("dijit_Menu_0")

    def close_avida_ed_about(self):
        """
        Attempts to close the "About" dialog box if it is currently open.

        :return: None.
        """
        if self.avida_ed_about_displayed():
            self.click_element("mnHpAboutCancel")

    def file_dropdown_expanded(self):
        """
        Determines whether the "File" dropdown at the top of the website has
        been expanded.

        :return: True if the dropdown is expanded, false otherwise.
        """
        if self.menu_dropdown_expanded("mnFile"):
            return True
        return False

    def click_file_dropdown(self):
        """
        Clicks on the "File" dropdown menu.

        :return: None.
        """
        self.click_element("mnFile")

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
        self.click_element("mnFlSaveWorkspace")

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
        self.click_element("mnFlSaveAs")

    def open_default_workspace(self):
        """
        Opens the default workspace by clicking on the "Open Default Workspace"
        option within the File tab of the main menu bar.

        :return: None.
        """
        self.open_file_dropdown()
        self.click_element("mnFlOpenDefaultWS")

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
        self.click_element("mnFlOpenWS")

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
        self.click_element("mnFlFzItem")

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
        self.click_element("mnFlExportData")

    def export_graphics(self):
        """
        Clicks on the "Export Graphics" option within the File tab of the main
        menu bar. Because exporting graphics from Avida-ED has not yet been
        implemented, this simply opens up a dialog box that explains how to
        take a screenshot using standard OS-level tools.

        :return: None.
        """
        self.open_file_dropdown()
        self.click_element("mnFlExportGraph")

    def export_graphics_dialog_displayed(self):
        """
        Determines whether the dialog box that appears when the "Export
        Graphics" option is clicked on is visible on-screen.

        :return: True if the dialog box is displayed, False otherwise.
        """
        if (self.file_dropdown_expanded() and
            self.element_displayed("dijit_Dialog_1")):
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
            self.click_element("mnFlExportGraphCancel")

    def freezer_dropdown_expanded(self):
        """
        Determines whether the "Freezer" dropdown menu at the top of the page is
        expanded.

        :return: True if the dropdown is expanded, False otherwise.
        """
        if self.menu_dropdown_expanded("mnFreezer"):
            return True
        return False

    def click_freezer_dropdown(self):
        """
        Clicks on the "Freezer" dropdown menu.

        :return: None.
        """
        self.click_element("mnFreezer")

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
        self.click_element("mnFzConfig")

    def can_save_current_pop(self):
        """
        Determines whether the option to "Save Current Population" within the
        Freezer tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, False otherwise.
        """
        if self.menu_item_disabled("mnFzPopulation"):
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
            self.click_element("mnFzPopulation")

    def can_save_selected_org(self):
        """
        Determines whether the option to "Save Selected Organism" within the
        Freezer tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, False otherwise.
        """
        if self.menu_item_disabled("mnFzOrganism"):
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
            self.click_element("mnFzOrganism")

    def can_save_offspring_org(self):
        """
        Determines whether the "Save Offspring Organism" option in the Freezer
        tab of the main menu bar is clickable or grayed out.

        :return: True if the option is clickable, False otherwise.
        """
        if self.menu_item_disabled("mnFzOffspring"):
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
            self.click_element("mnFzOffspring")

    def control_dropdown_expanded(self):
        """
        Determines whether the "Control" dropdown within the menu bar is
        expanded.

        :return: True if the dropdown is expanded, false otherwise.
        """
        if self.menu_dropdown_expanded("mnControl"):
            return True
        return False

    def click_control_dropdown(self):
        """
        Clicks on the "Control" dropdown in the menu bar.

        :return: None.
        """
        self.click_element("mnControl")

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

    def help_dropdown_expanded(self):
        """
        Determines whether the "Help" dropdown in the main menu bar on the site
        is expanded.

        :return: True if the dropdown is expanded, False otherwise.
        """
        if self.menu_dropdown_expanded("mnHelp"):
            return True
        return False

    def click_help_dropdown(self):
        """
        Clicks on the "Help" dropdown in the main menu bar.

        :return: None.
        """
        self.click_element("mnHelp")

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
