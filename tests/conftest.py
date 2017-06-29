import pytest
from base.webdriver_factory import WebDriverFactory


@pytest.yield_fixture(scope="class")
def one_time_setup(request, browser, local, setuipath, setffpath, seturl):
    print("One time setup begins here.\n")
    wdf = WebDriverFactory(browser, local, setuipath, setffpath, seturl)
    driver = wdf.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    wdf.clean_webdriver_instance()
    driver.quit()
    print("\nOne time teardown begins here.")


def pytest_addoption(parser):
    parser.addoption("--browser",
                     help="Name of internet browser used for testing.")
    parser.addoption("--local",
                     help="True if a local copy of Avida-ED should be run.")
    parser.addoption("--setuipath",
                     help="Path for folder containing local Avida-ED files.")
    parser.addoption("--setffpath",
                     help="Path for Firefox binary.")
    parser.addoption("--seturl",
                     help="URL for web-hosted Avida-ED.")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def local(request):
    return request.config.getoption("--local")


@pytest.fixture(scope="session")
def setuipath(request):
    return request.config.getoption("--setuipath")


@pytest.fixture(scope="session")
def setffpath(request):
    return request.config.getoption("--setffpath")

@pytest.fixture(scope="session")
def seturl(request):
    return request.config.getoption("--seturl")