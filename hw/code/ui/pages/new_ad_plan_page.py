from ui.pages.base_page import BasePageAuthorized
from selenium.webdriver.common.keys import Keys
from ui.locators import basic_locators
from ui.pages.new_ad_group_page import NewAdGroupPage

class NewAdPlanPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/new_create\/ad_plan.*$'

    locators = basic_locators.NewAdPlanPageLocators

    def configure_company_settings(self):
        self.click(self.locators.SITE_LOCATOR)

        input = self.click(self.locators.URL_INPUT_LOCATOR)
        input.send_keys('https://sub-me.ru')
        input.send_keys(Keys.ENTER)

        input = self.click(self.locators.BUDGET_INPUT_LOCATOR)
        input.send_keys('100')
        input.send_keys(Keys.ENTER)

        cnt = 5
        while self.is_opened() and cnt > 0:
            self.click(self.locators.NEXT_PAGE)
            cnt -= 1
        
        return NewAdGroupPage(self.driver)



