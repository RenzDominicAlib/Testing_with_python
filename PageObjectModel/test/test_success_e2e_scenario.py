import json

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjectModel.pageObjects.checkoutPage import CheckoutPage
from PageObjectModel.pageObjects.loginPage import LoginPage
from PageObjectModel.pageObjects.shoppingPage import ShoppingPage
test_data_path = '../testData/test_success_e2e_scenario.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.regression
def test_success_end_to_end(browser_instance):

    driver = browser_instance

    login_page = LoginPage(driver)
    print(login_page.get_page_title())
    login_page.login(test_list[0]["username"], test_list[0]["password"])

    shopping_page = ShoppingPage(driver)
    print(shopping_page.get_page_title())
    shopping_page.add_to_cart("product")
    shopping_page.go_to_cart()

    checking_out_page = CheckoutPage(driver)
    print(checking_out_page.get_page_title())
    checking_out_page.checkout()
    checking_out_page.enter_delivery_details("ind")
    checking_out_page.validate_order()

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_data", test_list)
def test_success_end_to_end_with_pytest_parametrize(browser_instance, test_list_data):

    driver = browser_instance

    login_page = LoginPage(driver)
    print(login_page.get_page_title())
    login_page.login(test_list_data["username"], test_list_data["password"])

    shopping_page = ShoppingPage(driver)
    print(shopping_page.get_page_title())
    shopping_page.add_to_cart("product")
    shopping_page.go_to_cart()

    checking_out_page = CheckoutPage(driver)
    print(checking_out_page.get_page_title())
    checking_out_page.checkout()
    checking_out_page.enter_delivery_details("ind")
    checking_out_page.validate_order()





















