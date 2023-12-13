import os
from ui.pages.settings_page import SettingsPage
import allure
import pytest
from ui.pages.registration_page import RegistrationPage
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from ui.pages.campaign_page import CampaignPage
from ui.pages.base_page import PageNotOpenedExeption


CLICK_RETRY = 3

class BaseCase:
    driver = None
    authorize = True
    needs_cabinet = True
    accept_cookie = False

    @allure.step("Setup")
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, credentials):
        self.driver = driver
        self.config = config
        self.logger = logger

        if self.accept_cookie:
            main_page = MainPage(self.driver)
            main_page.accept_cookie()

        if self.authorize:
            with allure.step("login"):
                login_page = LoginPage(self.driver)

                try:
                    login_page.login(*credentials)
                except PageNotOpenedExeption:
                    if 'login?&fail=1' in driver.current_url:
                        login_page.confirm_login(*credentials)
                    else:
                        raise

        if self.needs_cabinet:
            self.campaign_page = self.create_cabinet()
            self.campaign_page.close_onboarding()

        self.logger.debug('Initial setup completed')

    @allure.step("Teardown")
    @pytest.fixture(scope='function', autouse=True)
    def teardown(self):
        yield 

        if self.needs_cabinet:
            self.delete_cabinet(self.campaign_page)

        self.logger.debug('Teardown completed')

    @allure.step("creating cabinet")
    def create_cabinet(self):
        registration_page = RegistrationPage(self.driver)
        
        data = {'email': os.getenv('EMAIL_ACCOUNT')}
        campaign_page = registration_page.create_cabinet(data)
        
        return campaign_page

    def delete_cabinet(self, campaign_page):
        campaign_page.open_settings()
        settings_page = SettingsPage(self.driver)
        settings_page.delete_account()
