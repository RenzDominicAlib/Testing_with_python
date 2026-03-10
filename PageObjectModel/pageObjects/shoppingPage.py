from selenium.webdriver.common.by import By

from PageObjectModel.utils.commonUtils import CommonUtils


class ShoppingPage(CommonUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.link_shop_link = (By.CSS_SELECTOR, " a[href*='shop']")
        self.view_product_card = (By.XPATH, "//div[@class='card h-100']")
        self.link_cart_icon = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_to_cart(self, item):
        self.driver.find_element(*self.link_shop_link).click()
        products = self.driver.find_elements(*self.view_product_card)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == item:
                product.find_element(By.XPATH, "div/button").click()

    def go_to_cart(self):

        self.driver.find_element(*self.link_cart_icon).click()