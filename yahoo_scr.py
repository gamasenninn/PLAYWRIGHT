from playwright.sync_api import Playwright, sync_playwright
import math

HEADLESS = True


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=HEADLESS)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.yahoo.co.jp/
    page.goto("https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&fr=auc_top&p=トラクター+馬力&fixed=2&x=0&y=0")

    loc = page.locator('.Tab__subText')
    l_list = loc.all_text_contents()
    n= 100
    max_page = math.ceil(int(l_list[1].replace(',','').replace('件',''))/100)
    print("max page:", max_page)
    for i in range(max_page):
        b= n*i +1
        print(b,n)
        with page.expect_navigation():
            html = page.content()
            with open(f'yahoo_data/{i}.html',mode='w',encoding='utf-8') as f:
                f.write(html)
            #if i <= max_page -1 : 
            page.screenshot(path=f"yahoo_data/{i}.png")
            page.goto(f"https://auctions.yahoo.co.jp/search/search?p=トラクター+馬力&fixed=2&exflg=1&b={b}&n={n}")

    # Close page
    print("Loop end.....")

    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
