from playwright_base import PlaywrightBase
from models import InstagramStatus
import json


class PlaywrightClass:
    playwright = None
    account = None

    def __init__(self, account):
        self.account = account
        self.playwright = PlaywrightBase(account.dict_session())
        self.playwright.go_to("https://www.instagram.com")

    def set_account(self, account):
        self.account = account

        return self

    def allow_cookies(self):
        self.playwright.click_button("Allow all cookies")

    def fill_username(self):
        self.playwright.page.get_by_label("Phone number, username, or email").fill(self.account.username)
        return self

    def fill_password(self):
        self.playwright.page.get_by_label("Password").fill(self.account.password)
        return self

    def save_session(self):
        print('Save user session ...')
        self.account.session = self.playwright.context.storage_state()
        self.account.save()
        return self

    def after_login_process(self):
        print('After login process ...')
        if self.playwright.text_is_visible('Save info'):
            print('Save info is visible, clicking on it ...')
            self.playwright.click_button('Save info', timeout=5000)
            self.playwright.small_pause()

        if self.playwright.text_is_visible('Turn on Notifications'):
            print('Turn on notification is visible, clicking on it ...')
            self.playwright.click_button('Turn On', timeout=5000)
            self.playwright.small_pause()

    def pass_first_prompts(self):
        """
        Pass first prompts like allow cookies, save info etc.
        """
        self.allow_cookies()
        self.playwright.medium_pause()

        return self

    def is_not_logged_in(self):
        return self.playwright.text_is_visible('Log in with Facebook') or self.playwright.text_is_visible(
            "Don't have an account")

    def raise_exception(self, msg):
        print(msg)
        raise Exception(msg)

    def after_login_errors(self):

        if self.playwright.text_is_visible('your password was incorrect'):
            self.account.make_challenging('your password was incorrect')
            self.raise_exception('Username or password is incorrect')

        if self.playwright.text_is_visible('Enter your email') or self.playwright.text_is_visible(
                'send a confirmation code to this email'):
            self.account.make_challenging('Enter your email')
            self.raise_exception('Enter your email')

    def login(self):

        if self.is_not_logged_in():
            print('User is not logged in, trying to log in ... ')
            self.fill_username().fill_password()
            self.playwright.small_pause()
            self.playwright.click_button("Log in", exact=True)

            self.after_login_errors()
            self.playwright.large_pause()

        self.after_login_process()
        self.save_session()
        self.playwright.page.wait_for_timeout(800000)
        #     page.get_by_label("Phone number, username, or email").fill("sam238629")
        #     page.get_by_label("Password").click()
        #     page.get_by_label("Password").fill("far895tile620")
        #     page.get_by_role("button", name="Log in", exact=True).click()
