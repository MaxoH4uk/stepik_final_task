from selenium.webdriver.common.by import By


class BasePageLocators():
    EMPTY_BASKET_TEXT = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3 a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/p")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-4 h3 a")


class LoginPageLocators():
    EMAIL_FIELD = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/div[1]/div/input")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    RE_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")


class MainPageLocators():
    BASKET_LINK = (By.XPATH, "//header/div/div/div[2]/span/a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")