from ui.pages.base_page import BasePage
from ui.locators import basic_locators
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/$'

    def go_to_help_page(self):
        self.logger.debug("Starting authorization")
        help_btn = basic_locators.MainPageLocators.TO_HELP_PAGE_LOCATOR
        self.click(help_btn)
        