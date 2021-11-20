from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    #browser = p.chromium.launch(headless=False)
    browser = p.chromium.launch(devtools=True)
    context = browser.new_context()

    page = context.new_page()
    # Go to https://www.yahoo.co.jp/
    page.goto("https://www.yahoo.co.jp/")


    page.pause()

    page.goto("https://www.yahoo.co.jp/")



