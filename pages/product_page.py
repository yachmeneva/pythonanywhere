import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket button is not presented."

    def add_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TEXT).text
        print(f"\n Book: {product_name}")
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_TEXT).text
        print(f"Price: {product_price}")
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_btn.click()
        self.solve_quiz_and_get_code()
        time.sleep(10)
        success_msg = self.browser.find_element(*ProductPageLocators.SUCCESS_ADDED_MSG).text
        print(success_msg)
        basket_price_msg = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MSG).text
        print(basket_price_msg)
        assert product_name == success_msg, "Product name != product name in success message. "
        assert product_price == basket_price_msg, "Product price != basket price. "

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADDED_MSG), \
            "Success message is presented, but should not be. "

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADDED_MSG), \
            "Success message is presented, but should disappeared. "
