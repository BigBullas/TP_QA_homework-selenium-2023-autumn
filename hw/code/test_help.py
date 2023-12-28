from base import BaseCase
from ui.pages.main_page import MainPage
from ui.pages.help_page import *

class TestHelpPage(BaseCase):
    cabinet_created = False
    authorize = False

    def test_auth_help_navigation(self):
        main_page = MainPage(self.driver)
        main_page.go_to_help_page()

        help_page = HelpPage(self.driver)
        auth_help_page = help_page.auth_redirecting()
        assert auth_help_page.is_opened()

    def test_ads_help_navigation(self):
        main_page = MainPage(self.driver)
        main_page.go_to_help_page()

        help_page = HelpPage(self.driver)
        ads_page = help_page.ads_redirecting()
        assert ads_page.is_opened()

    def test_ads_tools_help_navigation(self):
        main_page = MainPage(self.driver)
        main_page.go_to_help_page()

        help_page = HelpPage(self.driver)
        ads_tools_page = help_page.ads_tools_redirecting()
        assert ads_tools_page.is_opened()

    def test_statistic_help_navigation(self):
        main_page = MainPage(self.driver)
        main_page.go_to_help_page()

        help_page = HelpPage(self.driver)
        statistic_page = help_page.statistic_redirecting()
        assert statistic_page.is_opened()

    def test_docs_help_navigation(self):
        main_page = MainPage(self.driver)
        main_page.go_to_help_page()

        help_page = HelpPage(self.driver)
        docs_page = help_page.docs_redirecting()
        assert docs_page.is_opened()

    def test_min_cab_help_navigation(self):
        main_page = MainPage(self.driver)
        main_page.go_to_help_page()

        help_page = HelpPage(self.driver)
        min_cab_page = help_page.min_cab_redirecting()
        assert min_cab_page.is_opened()

    def test_faq_help_navigation(self):
        main_page = MainPage(self.driver)
        main_page.go_to_help_page()

        help_page = HelpPage(self.driver)
        faq_page = help_page.faq_redirecting()
        assert faq_page.is_opened()

    def test_partner_help_navigation(self):
        main_page = MainPage(self.driver)
        main_page.go_to_help_page()

        help_page = HelpPage(self.driver)
        partner_page = help_page.partner_redirecting()
        assert partner_page.is_opened()
