import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()

    logger=LogGen.loggen()

    # def test_homePageTitle(self): # before adding method setup() from conftest.py file
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("****************Test_001_Login****************")
        self.logger.info("****************Verifying Homepage Title****************")
        # self.driver = webdriver.Chrome() # before adding method setup() from conftest.py file
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****************Homepage Title Test is passed****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("****************Homepage Title Test is failed****************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):   # same as above regarding fixture setup()
        self.logger.info("****************Verifying Login Test****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("****************Login Test is passed****************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("****************Login Test is failed****************")
            assert False

'''to avoid creating driver for each test case we have created fixture called setup '''