#
# import pytest
# from selenium import webdriver
#
#
# def pytest_addoption(parser):  # This will get the value from CLI / hooks
#     parser.addoption("--browser", default="chrome", help="Browser to run tests: chrome | firefox | ie")
#
#
# @pytest.fixture()
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("Launching Chrome browser.........")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#         print("Launching Firefox browser.........")
#     elif browser == 'ie':
#         driver = webdriver.Ie()
#         print("Launching IE browser.........")
#     else:
#         raise ValueError(f"Browser '{browser}' is not supported. Use chrome | firefox | ie")
#
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#
#     yield driver  # <-- Hands driver to the test
#
#     driver.close()  # <-- Runs after every test automatically
#
#
#
# ########### Pytest HTML Report ################
#
# # Add Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata = getattr(config, "_metadata", {})
#     config._metadata["Project Name"] = "nop Commerce"
#     config._metadata["Module Name"] = "Customers"
#     config._metadata["Tester"] = "Shilpa"
#
#
# # Modify/Delete Environment info
# @pytest.hookimpl(optionalhook=True)
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions


# ============================================================
# pytest_addoption: Adds custom command line argument --browser
# Usage: pytest test_login.py --browser=chrome
# ============================================================
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser to run tests: chrome | firefox | ie")


# ============================================================
# browser fixture: Reads --browser value from command line
# and passes it to setup fixture
# ============================================================
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# ============================================================
# setup fixture: Launches browser based on --browser value
# yield hands driver to test
# driver.close() runs automatically after every test
# ============================================================
@pytest.fixture()
def setup(browser):

    # =================== CHROME ===================
    # Run: pytest testCases/test_login.py --browser=chrome
    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")  # Hides bot detection
        options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Removes 'Chrome is controlled by automation' bar
        options.add_experimental_option("useAutomationExtension", False)  # Disables automation extension
        options.add_argument("--disable-notifications")   # Blocks browser notifications popup
        options.add_argument("--disable-popup-blocking")  # Allows all popups
        driver = webdriver.Chrome(options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")  # Hides webdriver property from website
        print("Launching Chrome browser.........")

    # =================== FIREFOX ===================
    # Run: pytest testCases/test_login.py --browser=firefox
    elif browser == 'firefox':
        options = FirefoxOptions()
        options.set_preference("dom.webdriver.enabled", False)              # Hides webdriver flag
        options.set_preference("useAutomationExtension", False)             # Disables automation extension
        options.set_preference("permissions.default.desktop-notification", 1)  # Allows notifications
        driver = webdriver.Firefox(options=options)
        print("Launching Firefox browser.........")

    # =================== IE ===================
    # Run: pytest testCases/test_login.py --browser=ie
    elif browser == 'ie':
        options = IEOptions()
        options.ignore_protected_mode_settings = True  # Ignores protected mode differences across zones
        options.ensure_clean_session = True            # Clears cache and cookies before launching
        options.native_events = False                  # Uses simulated events for better compatibility
        driver = webdriver.Ie(options=options)
        print("Launching IE browser.........")

    # =================== INVALID ===================
    # If wrong browser name is passed, stops test immediately with clear message
    # Example: pytest testCases/test_login.py --browser=safari → raises error
    else:
        raise ValueError(f"Browser '{browser}' is not supported. Use chrome | firefox | ie")

    # =================== COMMON SETTINGS ===================
    # These apply to ALL browsers
    driver.maximize_window()    # Opens browser in full screen
    driver.implicitly_wait(10)  # Waits up to 10 sec for elements to appear

    yield driver        # <-- Passes driver to test, pauses here while test runs

    driver.close()      # <-- Runs automatically after every test (pass or fail)


########### Pytest HTML Report ################

# ============================================================
# pytest_configure: Adds project info to HTML report
# Runs at the very start before any test is collected
# Run: pytest testCases/ --html=reports/report.html --self-contained-html
# ============================================================
def pytest_configure(config):
    config._metadata = getattr(config, "_metadata", {})  # Safely gets or creates metadata dict
    config._metadata["Project Name"] = "nop Commerce"    # Shows in Environment table of HTML report
    config._metadata["Module Name"]  = "Customers"       # Shows which module is being tested
    config._metadata["Tester"]       = "Shilpa"          # Shows who ran the test


# ============================================================
# pytest_metadata: Removes unwanted info from HTML report
# optionalhook=True means won't crash if pytest-metadata not installed
# ============================================================
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)  # Removes JAVA_HOME — not relevant for Python projects
    metadata.pop("Plugins", None)    # Removes Plugins list — clutters the report