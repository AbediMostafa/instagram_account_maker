from playwright_base import PlaywrightBase
from pathlib import Path
from locators import *
from helpers import *
from utils import *
import json
import os


class PlaywrightClass:
    playwright = None
    account = None

    def __init__(self, account):
        self.account = account
        self.playwright = PlaywrightBase(account.dict_session())
        self.playwright.go_to("https://www.instagram.com")

    def stop_playwright(self):
        self.playwright.stop_playwright()
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
        self.account.save_session(json.dumps(self.playwright.context.storage_state()))
        return self

    def after_login_process(self):
        print('After login process ...')
        self.playwright.tiny_pause()

        if self.playwright.text_is_visible('Allow the use of cookies by Instagram'):
            self.allow_cookies()
            self.playwright.small_pause()

        if self.playwright.text_is_visible('Save info'):
            print('Save info is visible, clicking on it ...')
            self.playwright.click_button('Save info', timeout=5000)
            self.playwright.medium_pause()

        if self.playwright.text_is_visible('Turn on Notifications'):
            print('Turn on notification is visible, clicking on it ...')
            self.playwright.click_button('Turn On', timeout=5000)
            self.playwright.medium_pause()

        if self.playwright.text_is_visible('Allow the use of cookies by Instagram'):
            self.allow_cookies()
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

    def after_login_errors(self):
        print('before password was incorrect ...')
        if self.playwright.text_is_visible('your password was incorrect'):
            self.account.make_challenging('your password was incorrect')
            raise_exception('Username or password is incorrect')
        print('after password was incorrect ...')

        print('before Enter your email ...')
        if self.playwright.text_is_visible('Enter your email') or self.playwright.text_is_visible(
                'send a confirmation code to this email'):
            self.account.make_challenging('Enter your email')
            raise_exception('Enter your email')
        print('after Enter your email ...')

        print('before Help us confirm its you...')
        if self.playwright.text_is_visible("Help us confirm it's you") or \
                self.playwright.text_is_visible('We detected that you’re logging in from an unknown browser') or \
                self.playwright.text_is_visible('follow the next steps to log into your account'):
            self.account.make_challenging("Help us confirm it's you")
            raise_exception("Help us confirm it's you")
        print('after Help us confirm its you ...')

    def login(self):

        if self.is_not_logged_in():
            print('User is not logged in, trying to log in ... ')
            self.fill_username().fill_password()
            self.playwright.tiny_pause()
            self.playwright.click_button("Log in", exact=True)
            self.playwright.large_pause()

        self.after_login_errors()
        self.playwright.large_pause()
        self.after_login_process()
        self.save_session()

        return self

    def follow_suggested(self):
        self.playwright.small_pause()
        print('Following suggested users ...')

        for follow_button in self.playwright.page.locator(locator_follow_1).all():

            try:
                if one_three_chance():
                    follow_button.click()
                    print('User followed')
                    self.playwright.small_pause()
                    if self.has_follow_errors():
                        break
            except:
                break

        return self

    def do_scroll(self):
        for i in range(scroll_count):
            self.playwright.page.mouse.wheel(0, scroll_height)
            self.playwright.small_pause()

        self.playwright.page.keyboard.down('Home')

    def scroll_and_like(self):
        print('Starting scroll and like ...')
        self.do_scroll()

        counter = 0
        for like_locator in self.playwright.page.locator(locator_like_1).all():
            try:
                counter += 1
                print(f'Scroll for the {counter} time')
                if one_two_chance():
                    like_locator.click()
                    self.playwright.small_pause()
                    if self.like_has_error():
                        break
            except:
                break

        return self

    def like_has_error(self):
        return False

    def has_follow_errors(self):
        print('Checking follow errors ...')
        if self.playwright.text_is_visible("You Can't Follow Accounts Right Now") \
                or self.playwright.text_is_visible("We restrict certain activity to protect our community") \
                or self.playwright.text_is_visible("Try Again Later"):
            print('Follow error appeared')
            self.playwright.click_button('OK')
            return True

        return False

    def check_post_image_errors(self):

        if self.playwright.text_is_visible("We restrict certain activity to protect our community") \
                or self.playwright.text_is_visible("We restrict certain activity to protect our community") \
                or self.playwright.text_is_visible("Try Again Later"):
            print('Post error appeared')
            self.playwright.click_button('Try Again Later')
            self.playwright.click_button('OK')

    def post_photo(self):
        self.playwright.click_link("New post Create")
        print('new post create')
        self.playwright.tiny_pause()

        self.playwright.page.locator(locator_post_input).set_input_files(self.select_random_post_image())
        print('image added')
        self.playwright.medium_pause()
        self.check_post_image_errors()

        self.playwright.tiny_pause()
        self.playwright.page.get_by_text("Crop", exact=True).click()
        print('corp clicked')
        self.playwright.tiny_pause()
        self.playwright.click_button("Next")
        print('first next clicked')
        self.playwright.tiny_pause()
        self.playwright.click_button("Next")
        print('second next clicked')
        self.playwright.tiny_pause()
        self.playwright.page.get_by_role("paragraph").click()
        self.playwright.page.get_by_role("textbox", name="Write a caption...").fill("Agree?")
        print('caption wrote')
        self.playwright.tiny_pause()
        self.playwright.page.get_by_role("button", name="Share").click()
        self.playwright.xx_large_pause()

        if self.playwright.text_is_visible("Your post has been shared"):
            self.playwright.click_locator(locator_close_sign)

        print('image shared')
        return self


    def set_profile_info(self):
        self.playwright.click_locator()

    def select_random_post_image(self):
        file_name = random.choice(os.listdir("posts"))
        Path(__file__).parent
        return f'{Path(__file__).parent}/posts/{file_name}'


