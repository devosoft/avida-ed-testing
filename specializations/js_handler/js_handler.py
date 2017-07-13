import logging

from base.base_page import BasePage
from utilities.util_methods import UtilityMethods
from utilities.custom_logger import create_custom_logger


class JSHandler(BasePage):
    """
    Specialization of the BasePage that is specialized to tasks that require
    executing Javscript code on the webpage.
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

    def get_current_update(self):
        """
        Gets the current update from av.grd.updateNum.

        :return: Integer value of current update.
        """
        return self.execute_script("return av.grd.updateNum")

    def __get_num_orgs_list(self):
        """
        Gets the list of the current amount of organisms for each update from
        av.pch.

        :return: List of integers with number of organisms in dish at each
        update.
        """
        return self.execute_script("return av.pch.aveNum")

    def get_curr_num_orgs(self):
        """
        Gets the current number of organisms from av.pch.

        :return: Integer value of current number of organisms.
        """
        return self.__get_num_orgs_list()[-1]

    def __get_num_via_orgs_list(self):
        """
        Gets the list of the current amount of viable organisms for each update
        from av.pch.

        :return: List of integers that are the number of viable organisms
        for each update.
        """

    def __get_avg_fitness_list(self):
        """
        Gets the list of average fitnesses for each update in experiment.

        :return: List of average fitnesses (floats).
        """
        return self.execute_script("return av.pch.aveFit")

    def get_curr_avg_fit(self):
        """
        Gets the current average fitness from av.pch.

        :return: Float value of average fitness.
        """
        return self.__get_avg_fitness_list()[-1]

    def __get_avg_rate(self):
        """
        Gets list of average energy acquisition rates for each update in exp.

        :return: List of average rates.
        """
        return self.execute_script("return av.pch.aveEar")

    def get_curr_avg_rate(self):
        """
        Gets the current average energy acquisition rate from av.pch.

        :return: Float value of average energy acquisition rate.
        """
        return self.__get_avg_rate()[-1]

    def __get_avg_cost(self):
        """
        Gets list of average offspring cost for each update in experiment.

        :return: List of average offspring cost.
        """
        return self.execute_script("return av.pch.aveCst")

    def get_curr_avg_cost(self):
        """
        Gets the current average offspring cost from av.pch.

        :return: Float value of average offspring cost.
        """
        return self.__get_avg_cost()[-1]

