import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("**************** Test_003_AddCustomer ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**************** Login Successful ****************")

        self.logger.info("**************** Starting addCustomer test ****************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddNew()

        self.logger.info("**************** Providing Customer Info ****************")

        self.email = random_generator() + '@gmail.com'
        self.addcust.setEmail(self.email)
        self.addcust.setPasswod('test123')
        self.addcust.setCustomersRoles('Guests')
        self.addcust.setManagerOfVendor('Vendor 2')
        self.addcust.setGender('Male')
        self.addcust.setFirstName('vijay')
        self.addcust.setLastName('Dhote')
        self.addcust.setDob('5/10/1989')
        self.addcust.setCompanyName('busyQA')
        self.addcust.setAdminContent('This is for testing.......')
        self.addcust.clickOnSave()

        self.logger.info("**************** Saving Customer Info ****************")

        self.logger.info("**************** Add customer Validation Started ****************")

        self.msg = self.driver.find_element(By.TAG_NAME,'body').text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("**************** Add customer test passed ****************")
        else :
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_addcustomer_scr.png')
            self.logger.info("**************** Add customer test failed ****************")
            assert True == False

        self.logger.info("**************** Ending Home Page Title Test ****************")


def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))




