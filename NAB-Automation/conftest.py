import allure
import pytest
from selenium.common.exceptions import UnexpectedAlertPresentException, WebDriverException
from pom.environment import *
from pom.PageMain import PageMain


# Session scope

# Class scope
@pytest.fixture(scope='class')
def init_environment(request):
    try:
        domain = request.config.getoption("--domain").upper()
        driver = WebDriver(request.config.getoption("--browser"), DIR_WEBDRIVERS)
        driver.setDownloadPath(DIR_TEMP)
        OW_PF.storeEngine('driver', driver)
        OW_PF.switchEngine(driver)
        OW_PF.switchEnv(OW_PF.get(domain))

        OW_PF.addPage('pageMain', PageMain)

        request.cls.environment = OW_PF.environment
        request.cls.driver = OW_PF.engine
        request.cls.timeout = 30

    except AttributeError:
        raise AttributeError('No domain! Call pytest with option "--domain" to set environment')


@pytest.fixture(scope='class')
def launch(request):
    for i in range(0, 5):
        try:
            OW_PF.engine.launch(request.config.getoption("--headless"))
            break
        except WebDriverException as e:
            if 'unable to discover open pages' in e.msg:
                continue
    with open(f'{DIR_TEMP}\\webdriver.log', 'w') as file:
        print(OW_PF.engine.capabilities, file=file)
    yield
    OW_PF.engine.quit()


# Function scope
@pytest.fixture(scope='function', autouse=True)
def handle_failed(request):
    failed_before = request.session.testsfailed
    yield
    if request.session.testsfailed != failed_before:
        for val in request.cls.__dict__.values():
            if isinstance(val, WebDriver):
                try:
                    allure.attach(val.driver.get_screenshot_as_png(),
                                  name=request.node.name,
                                  attachment_type=allure.attachment_type.PNG)
                except UnexpectedAlertPresentException as e:
                    print('Failed to capture screenshot. Skipped...')
                break


# Handle pytest configuration
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="Run test with desired browser")
    parser.addoption("--headless", action="store_true", help="Run test with headless browser")
    parser.addoption("--domain", action="store", help="Run test with desired domain name")


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers", "api: api test run")
    config.addinivalue_line("markers", "web: web test run")
    config.addinivalue_line("markers", "environment(name): test environment")


def pytest_collection_modifyitems(items):
    for item in items:
        if "TestWeb_" in item.nodeid:
            item.add_marker(pytest.mark.web)
        if "TestAPI_" in item.nodeid:
            item.add_marker(pytest.mark.api)
