import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities import XLUtls


class Test_002_DDT_Login:
    baseURL = Readconfig.getApplicationURL()
    path = ".//TestData/logindata.xlsx"

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):   # same as above regarding fixture setup()
        self.logger.info("**************** Test_002_DDT_Login ****************")
        self.logger.info("**************** Verifying Login DDT Test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtls.getRowCount(self.path,"Sheet1")
        print("no of rows in an Excel :", self.rows)

        lst_status = []      # empty list variable

        for r in range(2, self.rows + 1):
            self.user = XLUtls.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtls.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtls.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            # time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=="fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp == "fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")

        if 'Fail' not in lst_status:
            self.logger.info("*** Login DDT test Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Login DDT test Failed ***")
            self.driver.close()
            assert False

        self.logger.info("*** End of login DDT test ***")
        self.logger.info("*** Completed Test_002_DDT_Login ***")


'''to avoid creating driver for each test case we have created fixture called setup '''