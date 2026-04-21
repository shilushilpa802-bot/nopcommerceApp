from selenium.webdriver.common.by import By

class Login:

    # Locators (tuple format)
    textbox_username = (By.ID, "Email")
    textbox_password = (By.ID, "Password")
    button_login = (By.XPATH, "//button[normalize-space()='Log in']")
    link_logout = (By.LINK_TEXT, "Logout")

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Actions
    def setUserName(self, username):
        self.driver.find_element(*self.textbox_username).clear()
        self.driver.find_element(*self.textbox_username).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*self.textbox_password).clear()
        self.driver.find_element(*self.textbox_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*self.button_login).click()

    def clickLogout(self):
        self.driver.find_element(*self.link_logout).click()

   #approach 2

from selenium.webdriver.common.by import By

#
# class Login:
#     # Locators
#     textbox_username_id = "Email"
#     textbox_password_id = "Password"
#     button_login_xpath = "//input[@class='button-1 login-button']"
#     link_logout_linktext = "Logout"
#
#     # Constructor
#     def __init__(self, driver):
#         self.driver = driver
#
#     # Actions
#     def setUserName(self, username):
#         self.driver.find_element(By.ID, self.textbox_username_id).clear()
#         self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)
#
#     def setPassword(self, password):
#         self.driver.find_element(By.ID, self.textbox_password_id).clear()
#         self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
#
#     def clickLogin(self):
#         self.driver.find_element(By.XPATH, self.button_login_xpath).click()
#
#     def clickLogout(self):
#         self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()