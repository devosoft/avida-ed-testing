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

    def avida_ed_dropdown_expanded(self):
        """
        Determines whether the "Avida-ED" dropdown at the top of the page is
        expanded.

        :return: True if the dropdown is expanded, false otherwise.
        """
        if self.menu_dropdown_expanded("mnAvidaEd"):
            return True
        return False

    def open_avida_ed_dropdown(self):
        """
        Expands the Avida-ED dropdown menu at the top of the page.

        :return: None.
        """
        if not self.avida_ed_dropdown_expanded():
            self.click_element("mnAvidaEd")

    def close_avida_ed_dropdown(self):
        """
        Closes the Avida-ED dropdown menu at the top of the page.

        :return: None.
        """
        if self.avida_ed_dropdown_expanded():
            self.click_element("mnAvidaEd")

    def file_dropdown_expanded(self):
        """
        Determines whether the "File" dropdown at the top of the website has
        been expanded.

        :return: True if the dropdown is expanded, false otherwise.
        """
        if self.menu_dropdown_expanded("mnFile"):
            return True
        return False

    def open_file_dropdown(self):
        """
        Expands the "File" dropdown at the top of the website.

        :return: None.
        """
        if not self.file_dropdown_expanded():
            self.click_element("mnFile")

    def close_file_dropdown(self):
        """
        Closes the "File" dropdown at the top of the website.

        :return: None.
        """
        if self.file_dropdown_expanded():
            self.click_element("mnFile")
