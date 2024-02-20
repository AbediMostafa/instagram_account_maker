from playwright.sync_api import Playwright, sync_playwright, expect
import random
import json


class PlaywrightBase:
    page = None
    browser = None
    context = None
    session = None
    playwright = None

    def __init__(self, session):
        self.session = session
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False,)
        self.set_storage_state()
        self.page = self.context.new_page()

    def stop_playwright(self):
        self.playwright.stop()

    def set_storage_state(self):
        self.context = self.browser.new_context(
            storage_state=self.session) if self.session else self.browser.new_context()

    def go_to(self, url):
        self.page.goto(url)

    def click_button(self, name, exact=False, timeout=4000):
        try:
            self.page.get_by_role("button", name=name, exact=exact).click(timeout=timeout)

        except:
            pass

    def click_link(self, name, timeout=4000):
        try:
            self.page.get_by_role("link", name=name).click(timeout=timeout)

        except:
            pass

    def click_locator(self, locator, timeout=4000):
        try:
            self.page.locator(locator).click(timeout=timeout)

        except:
            pass

    def text_is_visible(self, text):
        return self.page.get_by_text(text).is_visible()

    def tiny_pause(self):
        self.page.wait_for_timeout(random.randint(1500, 2500))

    def small_pause(self):
        self.page.wait_for_timeout(random.randint(2500, 4000))

    def medium_pause(self):
        self.page.wait_for_timeout(random.randint(4000, 6000))

    def large_pause(self):
        self.page.wait_for_timeout(random.randint(6000, 9000))

    def x_large_pause(self):
        self.page.wait_for_timeout(random.randint(9000, 12000))

    def xx_large_pause(self):
        self.page.wait_for_timeout(random.randint(20000, 25000))
