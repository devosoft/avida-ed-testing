import json
import os

class Configuration:
    """
    Class that interfaces with the main configuration file, which contains file
    names and other configurable variables for this project.
    """

    _config_file_path = r"config_files\config.json"

    def __init__(self):
        """
        Initializes the Configuration object.
        """
        if not os.path.exists(self._config_file_path):
            self._create_config_file()

        with open(self._config_file_path) as json_data_file:
            self.config = json.load(json_data_file)

    def _create_config_file(self):
        """
        Creates a JSON file containing the default configuration information for
        the project.

        :return: None.
        """
        default_config_dict = {
            "ui_path":r"C:\avida_ed_ui",
            "ff_loc": r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe'
        }

        with open(self._config_file_path, "w") as file:
            json.dump(default_config_dict, file)

    def get_ui_path(self):
        """
        Gets the path to the Avida-ED UI installation (which is used for running
        the app locally).

        :return: Raw string literal containing the path to the Avida-ED UI
         install.
        """
        path = self.config["ui_path"]
        if path is not None:
            return path
        return r""

    def get_ff_loc(self):
        """
        Gets the path to the Firefox binary (which is needed when running with
        FF).

        :return: Raw string literal containing path to the Avida-ED UI install.
        """
        path = self.config["ff_loc"]
        if path is not None:
            return path
        return r""