from .page import Page
from appium.webdriver.common.appiumby import AppiumBy


class LoginPage(Page):

    # Base page
    HELLO_LOGIN_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/authHelloLogin")

    # Login page
    EMAIL_FIELD = (AppiumBy.ID, "com.ajaxsystems:id/authLoginEmail")
    PASSWORD_FIELD = (AppiumBy.ID, "com.ajaxsystems:id/authLoginPassword")
    LOGIN_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/authLogin")
    LOGIN_WRONG = (AppiumBy.CLASS_NAME, "android.widget.LinearLayout")

    # Hub menu
    MENU_DRAWER = (AppiumBy.ID, "com.ajaxsystems:id/menuDrawer")

    def press_login_base_button(self):
        # костиль щоб проходити першу сторінку
        try:
            self.click_element(self.HELLO_LOGIN_BUTTON)
        except:
            return


    def login(self, username, password):
        self.enter_text(self.EMAIL_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)


    def find_menu_drawer(self):
        # Можна переробити на try и якщо F, в тесті чекати чи є Linear з помилкою і корекний чи віна
        return self.find_element(self.MENU_DRAWER)

    def find_login_wrong(self):
        return self.find_element(self.LOGIN_WRONG)