from humanator import Humanator
humanator = Humanator()
humanator.do_humanation()

# from models import Accounts
#
# account = Accounts.pick_one()
#
#Enter your email
# send a confirmation code to this email
# def run(playwright: Playwright) -> None:
# Turn on Notifications
# Know right away when people follow
# Turn On
# Not Now
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.instagram.com")
#     page.get_by_role("button", name="Avvisa alla").click()
#     page.get_by_role("button", name="Allow all cookies").click()
#     page.get_by_label("Phone number, username, or email").click()
#     page.get_by_label("Phone number, username, or email").fill("sam238629")
#     page.get_by_label("Password").click()
#     page.get_by_label("Password").fill("far895tile620")
#     page.get_by_role("button", name="Log in", exact=True).click()
#     page.goto("https://www.instagram.com/accounts/onetap/?next=%2F")
#     page.get_by_role("button", name="Save info").click()
#     page.get_by_role("button", name="Turn On").click()
#     page.get_by_role("button", name="Follow").first.click()
#     page.get_by_role("button", name="Follow").nth(1).click()
#     page.get_by_role("button", name="Follow").nth(1).click()
#     page.get_by_text("Try Again Later").click()
#     page.locator("div:nth-child(41) > div > div > .x1uvtmcs").click(click_count=3)
#     page.get_by_text("Try Again Later").click()
#     page.get_by_text("Try Again Later").click()
#     page.get_by_text("Try Again Later").click(click_count=3)
#     page.locator("div:nth-child(41) > div > div > .x1uvtmcs").press("Control+c")
#     page.get_by_text("We restrict certain activity to protect our community.").click()
#     page.get_by_role("button", name="OK").click()
#     page.get_by_role("article").filter(
#         has_text="pavaraghii_tv2•18hOriginal audioMore optionsSorry, we're having trouble playing ").get_by_role(
#         "button", name="Like").click()
#     page.get_by_role("article").filter(
#         has_text="asrar_ir•19hOriginal audioMore optionsSorry, we're having trouble playing this v").get_by_role(
#         "button", name="Like").click()
#     page.get_by_role("article").filter(
#         has_text="moallatv3 and banifatemeh•17hOriginal audioMore optionsSorry, we're having troub").get_by_role(
#         "button", name="Like").click()
#     page.get_by_role("article").filter(
#         has_text="imamreza_8.ir•18hMore optionsSorry, we're having trouble playing this video.Lear").get_by_role(
#         "button", name="Like").click()
#     page.get_by_role("article").filter(
#         has_text="resane_amin•1dOriginal audioMore optionsSorry, we're having trouble playing this").get_by_role(
#         "button", name="Like").click()
#     page.get_by_role("article").filter(
#         has_text="imamreza_8.ir•22hبین الحرمین کربلاMore optionsSorry, we're having trouble playin").get_by_role(
#         "button", name="Like").click()
#     page.get_by_role("link", name="Notifications Notifications").click()
#     page.locator("div").filter(has_text=re.compile(r"^asheghan_zohur started following you\. 18hFollow$")).get_by_role(
#         "button", name="Follow").click()
#     page.get_by_role("button", name="OK").click()
#     page.get_by_role("link", name="Explore").click()
#     page.get_by_role("link",
#                      name="پیج قرآن را حتما فالو کنید و به اشتراک بگذارید تا در ثواب جاریه شریک باشید جزاکم الله Reel 2,528 265").click()
#     page.get_by_role("button", name="Close").click()
#     page.get_by_role("link",
#                      name="قیافه شوهرش دیدن داره🤣🤣\n.\n🎥 by : I’m sorry, I don’t know who made the video i just translate your beautiful video into persian 🌹\n“ All rights belong to their respective owners” for credit issues or removal please direct us and we answer as soon as possible 🙏🌹 بقیه ویدیوهای پیجمون🥰👇\n@idea__baanoo Reel 4,870 47").click()
#     page.get_by_role("button", name="Close").click()
#     page.get_by_role("link", name="Reels Reels").click()
#     page.locator("div").filter(has_text=re.compile(r"^Like24\.6K$")).get_by_role("button", name="Like").click()
#     page.locator("div").filter(has_text=re.compile(r"^Like75K$")).get_by_role("button", name="Like").click()
#     page.locator("div").filter(has_text=re.compile(r"^Like631K$")).get_by_role("button", name="Like").click()
#     page.get_by_role("link", name="Home Home").click()
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)
