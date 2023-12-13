from base import BaseCase
from ui.fixtures import *
from ui.pages.login_page import LoginPage

class TestLogin(BaseCase):
    authorize = False
    cabinet_created = False

    user_data = {
        "name": "Юзер",
        "surname": "Юзеров",
    }

    def test_login(self, credentials):
        login_page = LoginPage(self.driver)
        email, password = credentials

        registration_page = login_page.login(email, password)
        assert registration_page.is_opened()
        assert registration_page.get_user_data() == '{} {}'.format(self.user_data["name"], self.user_data["surname"])

