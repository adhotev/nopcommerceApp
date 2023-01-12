import time
import pytest

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import Readconfig


class Test_SearchCustomerByEmial_004:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByEmial_004(self,setup):
        self.logger.info('*************** SearchCustomerByEmial_004 ***************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login Successful ****************")

        self.logger.info("**************** Starting searchCustomer By Email ****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("**************** Searching Customer By Email ID ****************")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail('victoria_victoria@nopCommerce.com')
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail('victoria_victoria@nopCommerce.com')
        assert True==status
        self.logger.info('*************** TC_SearchCustomerByEmial_004 Finished ***************')




