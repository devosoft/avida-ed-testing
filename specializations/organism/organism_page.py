import logging

from base.base_page import BasePage
from utilities.custom_logger import create_custom_logger


class OrganismPage(BasePage):
    """
    Specialization of the BasePage that is specialized for use on the Organism
    Page within the Avida-ED website.
    """

    # Logger
    log = create_custom_logger(logging.DEBUG)

    # Locators for Organism Settings
    __org_settings_dlg = "dijit_Dialog_5"
    __org_settings_btn = "OrgSetting"
    __org_settings_btn_text = "Settings"
    __org_settings_close = "indDone"

    # Locators for Organism Details
    __org_details_pane = "rightDetail"
    __org_details_btn = "OrgDetailsButton"

    def __init__(self, driver):
        """
        Sets up the page at initialization.

        :param driver: The driver that is interacting with the actual page.
        """
        super().__init__(driver)
        self.driver = driver
        self.go_to_organism()

    def org_settings_displayed(self):
        """
        Checks if the Organism Settings popup is currently displayed.

        :return: True if the organism settings popup currently displayed, false
        otherwise.
        """
        org_sett_displayed = self.__element_displayed(self.__org_settings_dlg)
        self.log.info("Is Organism Settings dialog displayed? "
                      + str(org_sett_displayed))
        return org_sett_displayed

    def open_org_settings(self):
        """
        Navigates to the "Organism Settings" popup from within the "Organism" 
        pane.

        :return: None.
        """
        self.go_to_organism()
        button = self.__get_element(self.__org_settings_btn)
        button_text = self.get_text(element=button)
        if button_text == self.__org_settings_btn_text:
            self.__click_element(element=button)
            self.log.info("Opened Organism Settings dialog.")

    def close_org_settings(self):
        """
        Closes the "Organism Settings" popup if it is open.

        :return: None.
        """
        if self.org_settings_displayed():
            self.__click_element(self.__org_settings_close)
            self.log.info("Closed Organism Settings dialog.")

    def org_details_displayed(self):
        """
        Determines whether the details panel within the Organism window is
        currently displayed.
        
        :return: True if the details panel displayed, otherwise false. 
        """
        org_details_displayed = self.__element_displayed(self.__org_details_pane)
        self.log.info("Is Organism details pane displayed? "
                      + str(org_details_displayed))
        return org_details_displayed

    def open_org_details(self):
        """
        Displays the Details panel within the Organism window if it is not
        already displayed.
        
        :return: None.
        """

        self.go_to_organism()
        if not self.org_details_displayed():
            self.__click_element(self.__org_details_btn)
            self.log.info("Opened organism details pane.")

    def close_org_details(self):
        """
        Hides the Details panel within the Organism window if it is currently
        displayed.
        
        :return: None. 
        """
        self.go_to_organism()
        if self.org_details_displayed():
            self.__click_element(self.__org_details_btn)
            self.log.info("Closed organism details pane.")
