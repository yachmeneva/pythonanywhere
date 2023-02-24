from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_TEXT = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_ADDED_MSG = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    BASKET_PRICE_MSG = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong")
