import time
import pytest

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import Readconfig



class Test_SearchCustomerByName_005:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByName_005(self,setup):
        self.logger.info('*************** SearchCustomerByName_005 ***************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login Successful ****************")

        self.logger.info("**************** Starting searchCustomer By Name ****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("**************** Searching Customer By Name ****************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName('Victoria')
        searchcust.setLasttName('Terces')
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName('Victoria Terces')
        assert True == status
        self.logger.info('*************** TC_SearchCustomerByName_005 Finished ***************')
