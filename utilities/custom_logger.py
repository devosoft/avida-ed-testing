import inspect
import logging
import os


def create_custom_logger(log_level=logging.DEBUG):
    """
    Creates a custom logger to provide a log of activities performed by our
    driver.
    
    :param log_level: The lowest-priority log statements that should be put into
    our log.
    
    :return: A logger object that is ready for use.
    """

    log_path = "output/log/"
    log_name = "avida_ed_testing.log"

    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    os.makedirs(log_path, exist_ok=True)
    file_handler = logging.FileHandler(log_path + log_name,
                                       mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s: %(message)s ',
        datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
