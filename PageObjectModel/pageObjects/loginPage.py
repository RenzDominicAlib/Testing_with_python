from selenium.webdriver.common.by import By

from PageObjectModel.utils.commonUtils import CommonUtils


class LoginPage(CommonUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.input_username = (By.ID, "username")
        self.input_password = (By.ID, "password")
        self.chkbox_terms = (By.ID, "terms")
        self.btn_sign_in = (By.ID, "signInBtn")


    def login(self, username, password):
        self.driver.find_element(*self.input_username).send_keys(username)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.chkbox_terms).click()
        self.driver.find_element(*self.btn_sign_in).click()