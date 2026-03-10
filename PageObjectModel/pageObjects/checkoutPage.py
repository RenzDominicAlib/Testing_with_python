from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel.utils.commonUtils import CommonUtils


class CheckoutPage(CommonUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.btn_checkout = (By.XPATH, "//button[@class='btn btn-success']")

        self.input_country = (By.ID, "country")
        self.lnk_india = (By.LINK_TEXT, "India")
        self.chkbox_accept = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.btn_submit = (By.CSS_SELECTOR, "[type='submit']")

        self.view_success_alert = (By.CLASS_NAME, "alert-success")


    def checkout(self):
        self.driver.find_element(*self.btn_checkout).click()

    def enter_delivery_details(self, search_text):
        self.driver.find_element(*self.input_country).send_keys(search_text)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.lnk_india))
        self.driver.find_element(*self.lnk_india).click()
        self.driver.find_element(*self.chkbox_accept).click()
        self.driver.find_element(*self.btn_submit).click()

    def validate_order(self):
        successText = self.driver.find_element(*self.view_success_alert).text
        assert "Success! Thank you!" in successText
        print(successText)