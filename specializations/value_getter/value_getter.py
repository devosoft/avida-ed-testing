import logging

from base.base_page import BasePage
from utilities.util_methods import UtilityMethods
from utilities.custom_logger import create_custom_logger


class ValueGetter(BasePage):
    """
    Specialization of the BasePage that is specialized to getting values from
    within Avida-ED (as opposed to getting the UI text).
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
        Gets the current update from av.grd.PopStatsMsg.

        This is the main storage for this value as opposed to the info stored in
        the Plotly graph.

        :return: Integer value of current update.
        """
        return self.execute_script("return av.grd.popStatsMsg.update")

    def get_num_orgs(self):
        """
        Gets the current number of organisms from av.grd.PopStatsMsg.

        This is the main storage for this value as opposed to the info stored in
        the Plotly graph.

        :return: Integer value of current count of all organisms in dish.
        """
        return self.execute_script("return av.grd.popStatsMsg.organisms")

    def get_avg_fit(self):
        """
        Gets the current average organism fitness from av.grd.PopStatsMsg.

        This is the main storage for this value as opposed to the info stored in
        the Plotly graph.

        :return: Float value of the average fitness.
        """
        return self.execute_script("return av.grd.popStatsMsg.ave_fitness")

    def get_avg_age(self):
        """
        Gets the current average organism age from av.grd.PopStatsMsg.

        :return: Float value of the average age.
        """
        return self.execute_script("return av.grd.popStatsMsg.ave_age")

    def get_avg_offspring_cost(self):
        """
        Gets the current average offspring cost from av.grd.PopStatsMsg.

        This is the main storage for this value as opposed to the info stored in
        the Plotly graph.

        :return: Integer value of current update.
        """
        return self.execute_script("return av.grd.popStatsMsg.ave_gestation_time")

    def get_avg_energy_rate(self):
        """
        Gets the current avg. energy acquisition rate from av.grd.PopStatsMsg.

        This is the main storage for this value as opposed to the info stored in
        the Plotly graph.

        :return: Integer value of avg. energy acquisition rate.
        """
        return self.execute_script("return av.grd.popStatsMsg.ave_metabolic_rate")

    def get_num_performing_not(self):
        """
        Gets the current number of organisms that can take advantage of notose
        resource.

        :return: Number of orgs that can perform 'not'.
        """
        return self.execute_script("return av.grd.popStatsMsg.not")

    def get_num_performing_nan(self):
        """
        Gets the current number of organisms that can take advantage of nanose
        resource.

        :return: Number of orgs that can perform 'nan'.
        """
        return self.execute_script("return av.grd.popStatsMsg.nand")

    def get_num_performing_and(self):
        """
        Gets the current number of organisms that can take advantage of andose
        resource.

        :return: Number of orgs that can perform 'and'.
        """
        return self.execute_script("return av.grd.popStatsMsg.and")

    def get_num_performing_orn(self):
        """
        Gets the current number of organisms that can take advantage of ornose
        resource.

        :return: Number of orgs that can perform 'orn'.
        """
        return self.execute_script("return av.grd.popStatsMsg.orn")

    def get_num_performing_oro(self):
        """
        Gets the current number of organisms that can take advantage of orose
        resource.

        :return: Number of orgs that can perform 'oro'.
        """
        return self.execute_script("return av.grd.popStatsMsg.or")

    def get_num_performing_ant(self):
        """
        Gets the current number of organisms that can take advantage of andnose
        resource.

        :return: Number of orgs that can perform 'ant'.
        """
        return self.execute_script("return av.grd.popStatsMsg.andn")

    def get_num_performing_nor(self):
        """
        Gets the current number of organisms that can take advantage of norose
        resource.

        :return: Number of orgs that can perform 'nor'.
        """
        return self.execute_script("return av.grd.popStatsMsg.nor")

    def get_num_performing_xor(self):
        """
        Gets the current number of organisms that can take advantage of xorose
        resource.

        :return: Number of orgs that can perform 'xor'.
        """
        return self.execute_script("return av.grd.popStatsMsg.xor")

    def get_num_performing_equ(self):
        """
        Gets the current number of organisms that can take advantage of equose
        resource.

        :return: Number of orgs that can perform 'equ'.
        """
        return self.execute_script("return av.grd.popStatsMsg.equ")

    def gr_get_current_update(self):
        """
        Gets the current update from av.grd.updateNum.

        Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: Integer value of the current update.
        """
        return self.execute_script("return av.grd.updateNum")

    def __gr_get_num_orgs_list(self):
        """
        Gets the list of the current amount of organisms for each update from
        av.pch.

         Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: List of integers with number of organisms in dish at each
        update.
        """
        return self.execute_script("return av.pch.aveNum")

    def gr_get_curr_num_orgs(self):
        """
        Gets the current number of organisms from av.pch.

        :return: Integer value of current number of organisms.
        """
        return self.__gr_get_num_orgs_list()[-1]

    def __gr_get_avg_fitness_list(self):
        """
        Gets the list of average fitnesses for each update in experiment.

        :return: List of average fitnesses (floats).
        """
        return self.execute_script("return av.pch.aveFit")

    def gr_get_curr_avg_fit(self):
        """
        Gets the current average fitness from av.pch.

        Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: Float value of average fitness.
        """
        return self.__gr_get_avg_fitness_list()[-1]

    def __gr_get_avg_rate(self):
        """
        Gets list of average energy acquisition rates for each update in exp.

        Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: List of average rates.
        """
        return self.execute_script("return av.pch.aveEar")

    def gr_get_curr_avg_rate(self):
        """
        Gets the current average energy acquisition rate from av.pch.

        Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: Float value of average energy acquisition rate.
        """
        return self.__gr_get_avg_rate()[-1]

    def __gr_get_avg_cost(self):
        """
        Gets list of average offspring cost for each update in experiment.

        :return: List of average offspring cost.
        """
        return self.execute_script("return av.pch.aveCst")

    def gr_get_curr_avg_cost(self):
        """
        Gets the current average offspring cost from av.pch.

        Note: This gets a number from the Plotly graph, not the underlying
        message from Avida.

        :return: Float value of average offspring cost.
        """
        return self.__gr_get_avg_cost()[-1]

    def get_cols(self):
        """
        Gets the current number of columns in the dish grid.

        :return: Integer value of columns in dish.
        """
        return self.execute_script("return av.grd.cols")

    def get_rows(self):
        """
        Gets the current number of columns in the dish grid.

        :return: Integer value of rows in dish.
        """
        return self.execute_script("return av.grd.rows")
