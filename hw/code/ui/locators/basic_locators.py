from selenium.webdriver.common.by import By

class LoginPageLocators():
    TRIGGER_LOGIN_LOCATOR = (By.XPATH, "//a[contains(@class, 'ButtonCabinet')]")
    OAUTH_MAIL_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'oAuthService_mail_ru')]")

    EMAIL_LOCATOR = (By.NAME, "username")
    ENTER_PASSWORD_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'next-button')]")
    PASSWORD_LOCATOR = (By.NAME, "password")
    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'submit-button')]")

    RECAPTCHA_BTN_LOCATOR = (By.XPATH, "//button[contains(@data-test-id, 'recaptcha-inter-next')]")


class CampaignPageLocators():
    SETTINGS_PAGE_LOCATOR = (By.XPATH, "//*[@id='root']/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/div/section[2]/div[1]/a")
    ONBOARDING = (By.XPATH, "//*[@id='_modal_18']/div/div/div[3]")
    TRIGGER_CREATE_CAMPAIGN_LOCATOR = (By.XPATH, "//*[@id='adPlan']/div/div[2]/div/div[1]/div/div[1]/a")
    CAMPAIGN_NAME = (By.XPATH, '//*[@id="adPlan"]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div/div/div[3]/div/div[1]/div/button')

class NewAdPlanPageLocators():
    SITE_LOCATOR = (By.XPATH, "//*[@id='new_ad_create']/div/div/div/div/section[2]/div[1]/div/section/div/div/div/div[1]")
    URL_INPUT_LOCATOR = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/section[3]/div[1]/form/div/div/div/div[1]/span/input')
    BUDGET_INPUT_LOCATOR = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div/section[3]/div[1]/form/div/div[7]/div/span[1]/input')
    NEXT_PAGE = (By.XPATH, '//*[@id="footer"]/div/div/div[2]/button')

class NewAdPageLocators():
    TITLE_LOCATOR = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div[1]/div/fieldset/div/div[1]/div[2]/div/span/input')
    SUMMARY_LOCATOR = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div[1]/div/fieldset/div/div[1]/div[3]/div/span/textarea')
    AD_IMAGE_LOCATOR = (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div[1]/div/fieldset/div/div[1]/div[9]/div[1]/div[1]/div/label/span[1]/span/input')
    NEXT_PAGE = (By.XPATH, '//*[@id="footer"]/div/div/div[2]/button')
    CHOOSE_IMAGE_LOCATOR = (By.XPATH, '//*[@id="media-library-image"]/div/div/div[3]')
    LOGO_BUTTON_LOCATOR= (By.XPATH, '//*[@id="new_ad_create"]/div/div/div/div[1]/div/fieldset/div/div[1]/div[1]/div/button')

class NewAdGroupPageLocators():
    REGION_INPUT_LOCATOR = (By.XPATH, '//*[@id="react-collapsed-panel-1"]/fieldset/div/div/div[2]/div/div/div/div/label/input')
    REGION_RUSSIA_LOCATOR = (By.XPATH, '//*[@id="react-collapsed-panel-1"]/fieldset/div/div/div[1]/div[2]/button[1]/span[1]')
    REGION_MOSCOW_LOCATOR = (By.XPATH, '//*[@id="react-collapsed-panel-1"]/fieldset/div/div/div[1]/div[2]/button[2]')
    REGION_PETERSBURG_LOCATOR = (By.XPATH, '//*[@id="react-collapsed-panel-1"]/fieldset/div/div/div[1]/div[2]/button[3]')
    CHECKBOX_LOCATOR = (By.XPATH, '//*[@id="floating-ui-5"]/div/div/div[1]/div/div/div/label/div[2]/svg')
    NEXT_PAGE = (By.XPATH, '//*[@id="footer"]/div/div/div[2]/button')

class RegistrationPageLocators():
    SWITCH_ACCOUNT_LOCATOR = (By.XPATH, "//div[contains(@class, 'AccountSwitch_changeAccountName')]")
    CREATE_CABINET_LOCATOR = (By.ID, "click-createNewButton")
    EMAIL_LOCATOR = (By.NAME, "email")
    SUBMIT_LOCATOR = (By.XPATH, "//button[contains(@data-testid, 'create-button')]")
   
class BasePageAuthorizedLocators():
    pass

class SettingsLocators():
    DELETE_ACCOUNT_LOCATOR = (By.XPATH, "//button[contains(@class, 'DeleteAccount_button')]")
    MODAL_ACTIONS_DELETE_ACCOUNT = (By.XPATH, "//div[contains(@class, 'DeleteAccountConfirmModal_actions')]")
    CONFIRM_DELETE_ACCOUNT = (By.XPATH,
                              "//button[contains(@class, 'vkuiButton--mode-primary') and contains(@class, 'vkuiButton--appearance-negative')]")

class MainPageLocators():
    TO_HELP_PAGE_LOCATOR = (By.XPATH, "/html/body/section/div[1]/div/header/div[1]/div[2]/div/div[2]/div/div/a")

class HelpPageLocators():
    AUTH_LOCATOR = (By.XPATH, "/html/body/section/div[2]/div[2]/div[2]/a[1]")
    ADS_LOCATOR = (By.XPATH, "/html/body/section/div[2]/div[2]/div[2]/a[2]")
    ADS_TOOLS_LOCATOR = (By.XPATH, "/html/body/section/div[2]/div[2]/div[2]/a[3]")
    STATISTIC_LOCATOR = (By.XPATH, "/html/body/section/div[2]/div[2]/div[2]/a[4]")
    DOCS_LOCATOR = (By.XPATH, "/html/body/section/div[2]/div[2]/div[2]/a[5]")
    MINIMIZE_CABINET_LOCATOR = (By.XPATH, "/html/body/section/div[2]/div[2]/div[2]/a[6]")
    FAQ_LOCATOR = (By.XPATH, "/html/body/section/div[2]/div[2]/div[2]/a[7]")
    PARTNER_LOCATOR = (By.XPATH, "/html/body/section/div[2]/div[2]/div[2]/a[8]")
