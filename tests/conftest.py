import pytest
from base.webdriver_factory import WebDriverFactory


@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser):
    print("One time setup begins here.")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("\nOne time teardown begins here.")


def pytest_addoption(parser):
    parser.addoption("--browser",
                     help="Name of internet browser used for testing.")
    parser.addoption("--osType",
                     help="Type of operating system the tests will run on.")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")