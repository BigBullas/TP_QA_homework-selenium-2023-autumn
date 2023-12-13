import allure
from ui.locators import basic_locators
from ui.pages.registration_page import RegistrationPage
from ui.pages.main_page import MainPage


class LoginPage(MainPage):
    locators = basic_locators.LoginPageLocators

    @allure.step("Login")
    def login(self, email, password):
        self.logger.debug("Starting authorization")

        self.click(self.locators.TRIGGER_LOGIN_LOCATOR)
        self.click(self.locators.OAUTH_MAIL_LOCATOR, timeout=30)
        self.fill_field(self.locators.EMAIL_LOCATOR, email)
        self.click(self.locators.ENTER_PASSWORD_LOCATOR)
        self.fill_field(self.locators.PASSWORD_LOCATOR, password)
        self.click(self.locators.SUBMIT_LOCATOR)

        self.logger.debug("Authorization data has been successfully entered")

        return RegistrationPage(self.driver)

    @allure.step("Confirm login")
    def confirm_login(self, _, password):
        self.logger.debug("Starting confirming login")

        self.click(self.locators.RECAPTCHA_BTN_LOCATOR)
        self.fill_field(self.locators.PASSWORD_LOCATOR, password)

        self.logger.debug("Entering captcha")
        self.wait_for_openning(RegistrationPage.convert_regexp_url())

        return RegistrationPage(self.driver)
