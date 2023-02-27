from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PWD = (By.ID, "id_registration-password1")
    REPEAT_PWD = (By.ID, "id_registration-password2")
    REGISTRATION_BTN = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_TEXT = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_ADDED_MSG = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    BASKET_PRICE_MSG = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner strong")


class BasketPageLocators():
    IS_EMPTY_MSG = (By.XPATH, "//p[contains(text(), 'empty')]")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")

