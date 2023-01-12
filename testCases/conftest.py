import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print('Launching chrome browser......')
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print('Launching firefox browser......')
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser): #this will get the value from CLI/hook
    parser.addoption('--browser')

@pytest.fixture
def browser(request): # this will return pytest value to 'setup' method
    return request.config.getoption("--browser")

############## pytest HTML Reports ##############

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'vijay'


# It is hook for delete/Modify Environment info to HTML Reports
# Test without this (by commenting it out) to find how it works
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)
    metadata.pop("Platform", None)