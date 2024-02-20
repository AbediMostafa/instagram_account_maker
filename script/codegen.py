from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("about:blank")
    page.goto("https://www.instagram.com/")
    page.get_by_role("button", name="Allow all cookies").click()
    page.get_by_label("Phone number, username, or email").click(modifiers=["Control"])
    page.get_by_label("Phone number, username, or email").fill("sadru1838")
    page.get_by_label("Phone number, username, or email").press("Tab")
    page.get_by_label("Password").fill("far895tile620")
    page.get_by_role("button", name="Log in", exact=True).click()
    page.get_by_label("Phone number, username, or email").click()
    page.get_by_label("Phone number, username, or email").click()
    page.get_by_label("Phone number, username, or email").fill("sadr.a7871")
    page.get_by_role("button", name="Log in", exact=True).click()
    page.goto("https://www.instagram.com/accounts/onetap/?next=%2F")
    page.get_by_role("button", name="Save info").click()
    page.locator(".wbloks_1 > div:nth-child(3) > div > div").first.press("Control+Shift+C")
    page.locator(".wbloks_1 > div:nth-child(3) > div > div").first.press("Control+Shift+C")
    page.get_by_role("button", name="Allow all cookies").click()
    page.get_by_role("link", name="New post Create").click()
    page.get_by_role("button", name="Select from computer").click()
    page.get_by_role("button", name="Select from computer").press("Control+Shift+C")
    page.get_by_role("button", name="Select from computer").press("F12")
    page.get_by_role("button", name="Select from computer").click(button="right")
    page.get_by_role("button", name="Select from computer").click()
    page.get_by_role("button", name="Select from computer").set_input_files("WIN_20220215_16_47_14_Pro.jpg")
    page.get_by_role("button", name="Back").click()
    page.get_by_role("button", name="Discard").click()
    page.get_by_role("button", name="Select from computer").click()
    page.get_by_role("button", name="Select from computer").set_input_files("Screenshot 2023-12-22 141754.png")
    page.get_by_text("Crop", exact=True).click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("paragraph").click()
    page.get_by_role("textbox", name="Write a caption...").fill("Agree?")
    page.get_by_role("button", name="Share").click()
    page.get_by_role("button", name="Try again").click()
    page.get_by_text("Your post could not be shared. Please try again.").click(click_count=3)
    page.locator("div:nth-child(43) > div > div > .x1uvtmcs").press("Control+c")
    page.get_by_role("button", name="Close").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
