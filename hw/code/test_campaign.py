from base import BaseCase
from ui.pages.campaign_page import CampaignPage

class TestCampaign(BaseCase):

    def test_create_campaign(self):
        campaign_page = CampaignPage(self.driver)

        create_campaign_page = campaign_page.create_campaign()
        assert create_campaign_page.is_opened()

        create_group_page = create_campaign_page.configure_company_settings()
        assert create_group_page.is_opened()

        create_group_page.configure_group_settings('Москва')

