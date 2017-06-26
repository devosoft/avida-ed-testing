import json
import os

class Configuration:
    """
    Class that interfaces with the main configuration file, which contains file
    names and other configurable variables for this project.
    """

    _config_file_path = r"config_files\config.json"

    _default_config_dict = {
        "ui_path": r"C:\avida_ed_ui",
        "ff_loc": r'C:\Program Files (x86)\Mozilla Firefox\Firefox.exe',
        "av_url": r'https://avida-ed.beacon-center.org/appTest/AvidaED.html'
    }

    def __init__(self):
        """
        Initializes the Configuration object.
        """

        # Create config file if it doesn't exist.
        if not os.path.exists(self._config_file_path):
            self._create_config_file()
        self.config = self._get_config()

        # Checks for invalid config file.
        config_valid = ("ui_path" in self.config
                           and "ff_path" in self.config
                           and "av_url" in self.config)

        # If config invalid, re-do it.
        if not config_valid:
            self._create_config_file()
            self.config = self._get_config()


    def _get_config(self):
        """
        Gets the configuration from the config file.

        :return: a Python dict containing config info.
        """

        with open(self._config_file_path) as json_data_file:
            return json.load(json_data_file)

    def _create_config_file(self):
        """
        Creates a JSON file containing the default configuration information for
        the project.

        :return: None.
        """

        with open(self._config_file_path, "w") as file:
            json.dump(self._default_config_dict, file)

    def set_ui_path(self, path):
        """
        Sets the path to the Avida-ED UI installation.

        :param path: The path where the the web server should be created from so
        that the local Avida-ED copy runs as intended.

        :return: None.
        """
        modified_config_dict = self._default_config_dict
        modified_config_dict["ui_path"] = path
        with open(self._config_file_path, "w") as file:
            json.dump(modified_config_dict, file)
        self.config = self._get_config()

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

    def set_ff_path(self, path):
        """
        Sets the path to the Firefox binary.

        :param path: The path where the the FF binary should be looked for.

        :return: None.
        """
        modified_config_dict = self._default_config_dict
        modified_config_dict["ff_path"] = path
        with open(self._config_file_path, "w") as file:
            json.dump(modified_config_dict, file)
        self.config = self._get_config()

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

    def set_av_url(self, url):
        """
        Sets the URL for the Avida-ED website in the config.json file.

        :param url: The URL that will be placed in the config file.

        :return: None.
        """
        modified_config_dict = self._default_config_dict
        modified_config_dict["av_url"] = url
        with open(self._config_file_path, "w") as file:
            json.dump(modified_config_dict, file)
        self.config = self._get_config()

    def get_av_url(self):
        """
        Gets the URL for the online-hosted Avida-ED app.

        :return: Raw string literal containing URL to Avida-ED website.
        """
        url = self.config["av_url"]
        if url is not None:
            return url
        return r""