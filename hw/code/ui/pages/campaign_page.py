import allure_commons
import allure
from ui.pages.new_ad_plan_page import NewAdPlanPage
from ui.pages.base_page import BasePageAuthorized
from ui.locators import basic_locators

class CampaignPage(BasePageAuthorized):
    url = 'https://ads.vk.com/hq/dashboard/ad_plans'

    locators = basic_locators.CampaignPageLocators

    def create_campaign(self):
        self.logger.debug("Starting authorization")
        self.click(self.locators.TRIGGER_CREATE_CAMPAIGN_LOCATOR)
        return NewAdPlanPage(self.driver)
    
    def close_onboarding(self):
        self.click(self.locators.ONBOARDING)

    def open_settings(self):
        self.click(self.locators.SETTINGS_PAGE_LOCATOR)

