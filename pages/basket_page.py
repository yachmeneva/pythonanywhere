from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.IS_EMPTY_MSG), "There are no message 'Basket is empty'. "

    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty, it contains product(s). "
