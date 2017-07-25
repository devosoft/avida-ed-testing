import pytest
from base.webdriver_factory import WebDriverFactory
from base.base_page import BasePage
from specializations.value_getter.value_getter import ValueGetter
from specializations.population.population_page import PopulationPage
from specializations.organism.organism_page import OrganismPage
from specializations.analysis.analysis_page import AnalysisPage


@pytest.yield_fixture(scope="class")
def driver_setup(request, browser, local, setuipath, setffpath, seturl):
    print("One time setup begins here.\n")
    wdf = WebDriverFactory(browser, local, setuipath, setffpath, seturl)
    driver = wdf.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    wdf.clean_webdriver_instance()
    driver.quit()
    print("\nOne time teardown begins here.")


@pytest.yield_fixture(scope="class")
def bp_setup(request, driver_setup):
    bp = BasePage(driver_setup)

    if request.cls is not None:
        request.cls.bp = bp
        request.cls.vg = ValueGetter(driver_setup)
        request.cls.pp = PopulationPage(driver_setup)
        request.cls.ap = AnalysisPage(driver_setup)

    yield bp

    assert not bp.crash_report_displayed()


@pytest.fixture(scope="class")
def pp_setup(request, driver_setup):
    pp = PopulationPage(driver_setup)
    if request.cls is not None:
        request.cls.pp = pp
    return pp


@pytest.fixture(scope="class")
def op_setup(request, driver_setup):
    op = OrganismPage(driver_setup)
    if request.cls is not None:
        request.cls.op = op
    return op


@pytest.fixture(scope="class")
def ap_setup(request, driver_setup) -> AnalysisPage:
    ap = AnalysisPage(driver_setup)
    if request.cls is not None:
        request.cls.ap = ap
    return ap

@pytest.fixture(scope="class")
def vg_setup(request, driver_setup):
    vg = ValueGetter(driver_setup)
    if request.cls is not None:
        request.cls.vg = vg
    return vg


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