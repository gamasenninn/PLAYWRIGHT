from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.yahoo.co.jp/
    page.goto("https://auctions.yahoo.co.jp")


    # Click [placeholder="何をお探しですか？"]
    page.click("[placeholder=\"何をお探しですか？\"]")

    # Fill [placeholder="何をお探しですか？"]
    page.fill("[placeholder=\"何をお探しですか？\"]", "トラクター")

    # Click text=オークション
    page.click("text=オークション")


    for i in range(20):
        # Click text=次へ
        html = page.content()
        #html = page.innerText("list used_list")
        #print(html)
        with open(f'{i}.html',mode='w') as f:
            f.write(html)

        page.click("text=次へ")

 
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)