import time

import pytest
import string
import random
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from pageObjects.AddcustomerPage import AddCustomer
from Utilities.readProperties import ReadConfig
from Utilities.coustomLogger import LogGen


class Test_003_AddCustomer:
    baseURL  = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger   = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver = setup
        time.sleep(3)
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.driver.maximize_window()

        # Login acessfrom pom login page
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login Successful **********")

        # Navigate to Add Customer
        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver) #acess or create object for AddCustomer class in pom page to acess class object
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddnew()

        # Fill Customer Info
        self.logger.info("************* Providing Customer Info **********")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Female")
        self.addcust.setFirstName("Shilpa")
        self.addcust.setLastName("Srinivas")
        self.addcust.setDob("08/05/1999")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()
        self.logger.info("************* Customer Info Saved **********")

        # Validation
        self.logger.info("********* Add Customer Validation Started *****************")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            self.logger.info("********* Add Customer Test Passed *********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_addCustomer_scr.png")
            self.logger.error("********* Add Customer Test Failed ************")
            assert False

        self.logger.info("******* Ending Add Customer Test **********")


# ✅ random_generator defined at the end
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))