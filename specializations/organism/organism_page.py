import logging

from base.base_page import BasePage
from utilities.custom_logger import create_custom_logger

from selenium.webdriver.support.ui import WebDriverWait


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
    __org_settings_mut_rate_xpath = ".//*/div[@id='widget_orMuteInput']/div/" \
                                    "input[@type='hidden']"
    __org_settings_exp_rep = "OrganExperimentRadio"
    __org_settings_demo_rep = "OrganDemoRadio"

    # String for 'value' attribute.
    __value = "value"

    # Locators for Organism Details
    __org_details_pane = "rightDetail"
    __org_details_btn = "OrgDetailsButton"
    __org_not = "notPerf"
    __org_nan = "nanPerf"
    __org_and = "andPerf"
    __org_orn = "ornPerf"
    __org_oro = "oroPerf"
    __org_ant = "antPerf"
    __org_nor = "norPerf"
    __org_xor = "xorPerf"
    __org_equ = "equPerf"

    # Locators for Active Organism
    __active_org_xpath = "//*/div[@id='activeOrgan']/div"

    # Locator for current cycle number
    __current_cycle_xpath = "//*/input[@name='cycle']"

    # Locators/identifiers/class names for Org. Reproduction control buttons
    __org_rep_disabled = "disabled"
    __org_rep_controls = ["orgReset",
                          "orgBack",
                          "orgRun",
                          "orgForward",
                          "orgEnd"]
    __org_run_text = "Run"
    __org_stop_text = "Stop"

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
            if self.wait_until_visible(self.__org_settings_dlg):
                self.log.info("Opened Organism Settings dialog.")
            else:
                self.log.warning("Failed to open Organism Settings dialog.")

    def close_org_settings(self):
        """
        Closes the "Organism Settings" popup if it is open.

        :return: None.
        """
        if self.org_settings_displayed():
            self.click_element(self.__org_settings_close)
            if self.wait_until_invisible(self.__org_settings_dlg):
                self.log.info("Closed Organism Settings dialog.")
            else:
                self.log.warning("Failed to close Organism Settings dialog.")

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
            if self.wait_until_visible(self.__org_details_pane):
                self.log.info("Opened organism details pane.")
            else:
                self.log.warning("Failed to open organism details pane.")

    def close_org_details(self):
        """
        Hides the Details panel within the Organism window if it is currently
        displayed.
        
        :return: None. 
        """
        self.go_to_organism()
        if self.org_details_displayed():
            self.click_element(self.__org_details_btn)
            if self.wait_until_invisible(self.__org_details_pane):
                self.log.info("Closed organism details pane.")
            else:
                self.log.warning("Failed to close organism details pane.")

    def org_rep_controls_enabled(self, driver=None):
        """
        Determines if all organism reproduction controls are enabled.

        :param driver: Useless parameter that is supplied by wait.until;
        must be kept here, DO NOT REMOVE.

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

    def wait_until_org_controls_enabled(self):
        """
        Use WebdriverWait to wait until the reproduction controls are enabled.

        Times out after 30 seconds.

        :return: None.
        """
        WebDriverWait(self.driver, 30) \
            .until(self.org_rep_controls_enabled)

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
        cyc_num = int(self.get_attr_value(attr=self.__value,
                                          element=elem))
        self.log.info("Current Org. cycle number is: " + str(cyc_num))
        return cyc_num

    def reset_org_rep(self):
        """
        Clicks on the 'Reset' button for organism reproduction.

        :return: None.
        """
        if self.org_rep_controls_enabled():
            self.click_element(self.__org_rep_controls[0])
            self.log.info("Clicked on 'Reset' for organism reproduction.")
            WebDriverWait(self.driver, 10).until(self.__cycle_is_zero)
        else:
            self.log.info("Tried to click on 'Reset' for organism reproduction"
                          " but found button to be disabled.")

    def back_org_rep(self):
        """
        Clicks on the 'Back' button for organism reproduction.

        :return: None.
        """
        if self.org_rep_controls_enabled():
            self.click_element(self.__org_rep_controls[1])
            self.log.info("Clicked on 'Back' for organism reproduction.")
            self.util.sleep(0.25, "Waiting for Back to take effect.")
        else:
            self.log.info("Tried to click on 'Back' for organism reproduction"
                          " but found button to be disabled.")

    def run_org_rep(self):
        """
        Clicks on the 'Run' button for organism reproduction.

        :return: None.
        """
        btn = self.get_element(self.__org_rep_controls[2])
        if (self.org_rep_controls_enabled()
                and self.get_text(element=btn) == self.__org_run_text):

            self.click_element(element=btn)
            self.log.info("Clicked on 'Run' for organism reproduction.")
            self.util.sleep(0.25, "Waiting for 'Run' to take effect.")
        else:
            self.log.info("Tried to click on 'Run' for organism reproduction "
                          "but found button to be disabled or already running.")

    def stop_org_rep(self):
        """
        Clicks on the 'Stop' button for organism reproduction.

        :return: None.
        """
        btn = self.get_element(self.__org_rep_controls[2])
        if (self.org_rep_controls_enabled()
                and self.get_text(element=btn) == self.__org_stop_text):

            self.click_element(element=btn)
            self.log.info("Clicked on 'Pause' for organism reproduction.")
            self.util.sleep(0.25, "Waiting for 'Stop' to take effect.")
        else:
            self.log.info("Tried to click on 'Pause' for organism reproduction"
                          " but found button to be disabled or already"
                          " running.")

    def forward_org_rep(self):
        """
        Clicks on the 'Forward' button for organism reproduction.

        :return: None.
        """
        if self.org_rep_controls_enabled():
            self.click_element(self.__org_rep_controls[3])
            self.log.info("Clicked on 'Forward' for organism reproduction.")
            self.util.sleep(0.25, "Waiting for 'Forward' to take effect.")
        else:
            self.log.info("Tried to click on 'Forward' for organism"
                          " reproduction but found button to be disabled.")

    def end_org_rep(self):
        """
        Clicks on the 'End' button for organism reproduction.

        :return: None.
        """
        if self.org_rep_controls_enabled():
            self.click_element(self.__org_rep_controls[4])
            self.log.info("Clicked on 'End' for organism reproduction.")
            self.util.sleep(0.25, "Waiting for 'End' to take effect.")
        else:
            self.log.info("Tried to click on 'End' for organism reproduction"
                          "but found button to be disabled.")

    def get_org_mut_rate(self):
        """
        Gets the current mutation rate for the active organism in Org. view.

        :return: Integer value of the the current mutation rate.
        """
        elem = self.get_element(self.__org_settings_mut_rate_xpath, "xpath")
        mut_rate = float(self.get_attr_value(attr=self.__value,
                                           element=elem))
        self.log.info("Current Org. cycle number is: " + str(mut_rate))
        return mut_rate

    def repeatability_is_exp(self):
        """
        Determines whether the organism is in 'experimental Repeatability Mode',
        meaning that reproduction will be different each time the organism
        reproduction is started.

        :return: True if experimental Repeatability mode is on; False otherwise.
        """
        exp_radio = self.get_element(self.__org_settings_exp_rep)
        is_exp = exp_radio.is_selected()
        self.log.info("Is Repeatability set to Experimental mode? "
                      + str(is_exp))
        return is_exp

    def repeatability_is_demo(self):
        """
        Determines whether the organism is in ' demo Repeatability Mode',
        meaning that reproduction will go exactly the same every time rather
        than having random mutations.

        :return: True if demo Repeatability mode is on; False otherwise.
        """
        demo_radio = self.get_element(self.__org_settings_demo_rep)
        is_demo = demo_radio.is_selected()
        self.log.info("Is Repeatability set to Demo mode? " + str(is_demo))
        return is_demo

    def set_repeatability_to_exp(self):
        """
        Changes repeatability mode to 'Experimental'.

        :return: None.
        """
        if not self.repeatability_is_exp():
            self.click_element(self.__org_settings_exp_rep)
            self.log.info("Settings repeatability mode to 'Experimental' in Org"
                          " Settings.")

    def set_repeatability_to_demo(self):
        """
        Changes repeatability mode to 'Demo'.

        :return: None.
        """
        if not self.repeatability_is_demo():
            self.click_element(self.__org_settings_demo_rep)
            self.log.info("Settings repeatability mode to 'Demo' in Org "
                          "Settings.")

    def get_org_num_not_performed(self):
        """
        Gets the number of NOT functions performed by the reproducing organism
        in Organism View.

        :return: The integer value of NOT functions performed by the organism.
        """
        return int(self.get_text(self.__org_not))

    def get_org_num_nan_performed(self):
        """
        Gets the number of NAN functions performed by the reproducing organism
        in Organism View.

        :return: The integer value of NAN functions performed by the organism.
        """
        return int(self.get_text(self.__org_nan))

    def get_org_num_and_performed(self):
        """
        Gets the number of AND functions performed by the reproducing organism
        in Organism View.

        :return: The integer value of AND functions performed by the organism.
        """
        return int(self.get_text(self.__org_and))

    def get_org_num_orn_performed(self):
        """
        Gets the number of ORN functions performed by the reproducing organism
        in Organism View.

        :return: The integer value of ORN functions performed by the organism.
        """
        return int(self.get_text(self.__org_orn))

    def get_org_num_oro_performed(self):
        """
        Gets the number of ORO functions performed by the reproducing organism
        in Organism View.

        :return: The integer value of ORO functions performed by the organism.
        """
        return int(self.get_text(self.__org_oro))

    def get_org_num_ant_performed(self):
        """
        Gets the number of ANT functions performed by the reproducing organism
        in Organism View.

        :return: The integer value of ANT functions performed by the organism.
        """
        return int(self.get_text(self.__org_ant))

    def get_org_num_nor_performed(self):
        """
        Gets the number of NOR functions performed by the reproducing organism
        in Organism View.

        :return: The integer value of NOR functions performed by the organism.
        """
        return int(self.get_text(self.__org_nor))

    def get_org_num_xor_performed(self):
        """
        Gets the number of XOR functions performed by the reproducing organism
        in Organism View.

        :return: The integer value of XOR functions performed by the organism.
        """
        return int(self.get_text(self.__org_xor))

    def get_org_num_equ_performed(self):
        """
        Gets the number of EQU functions performed by the reproducing organism
        in Organism View.

        :return: The integer value of EQU functions performed by the organism.
        """
        return int(self.get_text(self.__org_equ))

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

    def __cycle_is_zero(self, driver=None):
        """
        Determines if the current organism reproduction cycle is 0.

        :param driver: Unused parameter that is automatically provided by
        wait.until. Please DO NOT REMOVE.

        :return: True if cycle is 0, False otherwise.
        """
        return self.get_cycle() == 0
