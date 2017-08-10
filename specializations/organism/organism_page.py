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

    # Locators for Active Organism
    __active_org_xpath = "//*/div[@id='activeOrgan']/div"

    # Locator for current cycle number
    __current_cycle_xpath = "//*/input[@name='cycle']"
    __cycle_val = "value"

    # Locators/identifiers/class names for Org. Reproduction control buttons
    __org_rep_disabled = "disabled"
    __org_rep_controls = ["orgReset",
                          "orgBack",
                          "orgRun",
                          "orgForward",
                          "orgEnd"]

    def __init__(self, driver):
        """
        Sets up the page at initialization.

        :param driver: The driver that is interacting with the actual page.
        """
        super().__init__(driver)
        self.driver = driver

    def org_settings_displayed(self):
        """
        Checks if the Organism Settings popup is currently displayed.

        :return: True if the organism settings popup currently displayed, false
        otherwise.
        """
        org_sett_displayed = self.element_displayed(self.__org_settings_dlg)
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
        button = self.get_element(self.__org_settings_btn)
        button_text = self.get_text(element=button)
        if button_text == self.__org_settings_btn_text:
            self.click_element(element=button)
            self.log.info("Opened Organism Settings dialog.")

    def close_org_settings(self):
        """
        Closes the "Organism Settings" popup if it is open.

        :return: None.
        """
        if self.org_settings_displayed():
            self.click_element(self.__org_settings_close)
            self.log.info("Closed Organism Settings dialog.")

    def org_details_displayed(self):
        """
        Determines whether the details panel within the Organism window is
        currently displayed.
        
        :return: True if the details panel displayed, otherwise false. 
        """
        org_details_displayed = self.element_displayed(self.__org_details_pane)
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
            self.click_element(self.__org_details_btn)
            self.log.info("Opened organism details pane.")

    def close_org_details(self):
        """
        Hides the Details panel within the Organism window if it is currently
        displayed.
        
        :return: None. 
        """
        self.go_to_organism()
        if self.org_details_displayed():
            self.click_element(self.__org_details_btn)
            self.log.info("Closed organism details pane.")

    def org_rep_controls_enabled(self):
        """
        Determines if all organism reproduction controls are enabled.

        :return: True if ALL of these buttons are enabled, False otherwise.
        """
        for identifier in self.__org_rep_controls:
            if self.__org_rep_control_disabled(
                    self.get_element(identifier)) is True:

                self.log.info("Org Rep. Controls are not all enabled.")
                return False
        self.log.info("Org Rep. Controls are all enabled.")
        return True

    def org_rep_controls_disabled(self):
        """
        Determines if all organism reproduction controls are disabled.

        :return: True if ALL of these buttons are disabled, False otherwise.
        """
        for identifier in self.__org_rep_controls:
            if self.__org_rep_control_disabled(
                    self.get_element(identifier)) is False:

                self.log.info("Org. Rep. Controls are not all disabled.")
                return False

        self.log.info("Org. Rep. Controls are all disabled.")
        return True

    def has_active_org(self):
        """
        Determines if there is an organism actively being examined in the
        Organism Window.

        :return: True if there is an active organism in the 'activeOrgan' box
        in the top left of the Organism window; False otherwise.
        """
        active_org = self.get_element(self.__active_org_xpath, "xpath")
        has_active = (active_org is not None)
        self.log.info("Is there an active org. in Organism Window? "
                      + str(has_active))
        return has_active

    def get_cycle(self):
        """
        Gets the current cycle number for the active organism.

        :return: Integer value of the the current cycle.
        """
        elem = self.get_element(self.__current_cycle_xpath, "xpath")
        cyc_num = int(self.get_attr_value(attr=self.__cycle_val,
                                          element=elem))
        self.log.info("Curent Org. cycle number is: " + str(cyc_num))
        return cyc_num

    def __org_rep_control_disabled(self, element):
        """
        Determines if an organism reproduction control (e.g Reset) is disabled.

        :param element: The org. rep. control WebElement that is to be checked.

        :return: True if element is disabled, false otherwise.
        """
        disabled = self.element_has_attr(element=element,
                                         attr_name=self.__org_rep_disabled)
        self.log.info("Is Organism Reproduction control button disabled? "
                      + str(disabled))
        return disabled
