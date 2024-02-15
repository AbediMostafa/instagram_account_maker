from playwright_class import PlaywrightClass
from models import Accounts


class Humanator:
    playwright = None
    account = None

    def do_humanation(self):
        while True:
            # try:
                self.account = Accounts.pick_one()
                self.playwright = PlaywrightClass(self.account)

                (self.playwright
                 .pass_first_prompts()
                 .login())

            # except Exception as e:
            #     print(e)
