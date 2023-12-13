from ui.pages.base_page import BasePageAuthorized
from selenium.webdriver.common.keys import Keys
from ui.locators import basic_locators

class NewAdGroupPage(BasePageAuthorized):
    url = r'^https:\/\/ads\.vk\.com\/hq\/new_create\/ad_plan\/\d+\/ad_group\/\d+.*$'

    locators = basic_locators.NewAdGroupPageLocators

    def configure_group_settings(self, region):
        if region == 'Москва':
            self.click(self.locators.REGION_MOSCOW_LOCATOR)
        elif region == 'Санкт-Петербург':
            self.click(self.locators.REGION_PETERSBURG_LOCATOR)
        elif region == 'Россия':
            self.click(self.locators.REGION_RUSSIA_LOCATOR)
        else:
            input = self.click(self.locators.REGION_INPUT_LOCATOR)

            input.send_keys(region)
            input.send_keys(Keys.ENTER)

            self.click(self.locators.CHECKBOX_LOCATOR)
            
        return 






