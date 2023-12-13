from time import sleep

import allure
from ui.pages.base_page import BasePage, NoNavbarSection
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    url = r'^https:\/\/ads\.vk\.com\/$'