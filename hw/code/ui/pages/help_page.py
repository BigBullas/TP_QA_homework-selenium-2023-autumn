from selenium.webdriver.support import expected_conditions as EC
from ui.pages.ads_page import AdsPage
from ui.pages.ads_tools_page import AdsToolsPage
from ui.pages.auth_help_page import AuthHelpPage
from ui.pages.docs_page import DocsPage
from ui.pages.faq_page import FAQPage
from ui.pages.min_cab_page import MinCabPage
from ui.pages.partner_page import PartnerPage
from ui.pages.statistic_page import StatisticPage
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class HelpPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/help.*$'

    locators = basic_locators.HelpPageLocators

    def auth_redirecting(self):
        self.click(self.locators.AUTH_LOCATOR)
        return AuthHelpPage(self.driver)
    
    def ads_redirecting(self):
        self.click(self.locators.ADS_LOCATOR)
        return AdsPage(self.driver)
    
    def ads_tools_redirecting(self):
        self.click(self.locators.ADS_TOOLS_LOCATOR)
        return AdsToolsPage(self.driver)
    
    def statistic_redirecting(self):
        self.click(self.locators.STATISTIC_LOCATOR)
        return StatisticPage(self.driver)

    def docs_redirecting(self):
        self.click(self.locators.DOCS_LOCATOR)
        return DocsPage(self.driver)
    
    def min_cab_redirecting(self):
        self.click(self.locators.MINIMIZE_CABINET_LOCATOR)
        return MinCabPage(self.driver)
    
    def faq_redirecting(self):
        self.click(self.locators.FAQ_LOCATOR)
        return FAQPage(self.driver)
    
    def partner_redirecting(self):
        self.click(self.locators.PARTNER_LOCATOR)
        return PartnerPage(self.driver)
