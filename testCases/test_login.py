import time

import self
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.coustomLogger import LogGen
from pageObjects.LoginPage import Login
import time
from Utilities.readProperties import ReadConfig


class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.logger.info("**** Home page title test passed ****")
        assert self.driver.title == "nopCommerce demo store. Login"

        self.logger.error("**** Home page title test failed****")
        self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")

    def test_login(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)  #POM object to acess pom

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        WebDriverWait(self.driver, 20).until(
            # lambda driver: "Dashboard" in driver.title
            EC.title_contains("Dashboard")
        )
        self.logger.info("****Login test passed ****")
        assert self.driver.title == "Dashboard / nopCommerce administration"
        self.logger.error("****Login test failed ****")
        self.driver.save_screenshot(".\\Screenshots\\testlogin.png")
