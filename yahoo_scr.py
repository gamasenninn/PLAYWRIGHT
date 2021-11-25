from playwright.sync_api import Playwright, sync_playwright
import math

HEADLESS = False
CATEGORY = '2084244599'  #トラクター車体
PERPAGE = 100


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=HEADLESS)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.yahoo.co.jp/
    page.goto(f"https://auctions.yahoo.co.jp/search/search?auccat={CATEGORY}&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&fr=auc_top&fixed=2&x=0&y=0")

    loc = page.locator('.Tab__subText')
    l_list = loc.all_text_contents()
    max_page = math.ceil(int(l_list[1].replace(',','').replace('件',''))/PERPAGE)
    print("max page:", max_page)
    for i in range(max_page):
        b= PERPAGE*i +1
        print(b,PERPAGE)
        with page.expect_navigation():
            page.goto(f"https://auctions.yahoo.co.jp/search/search?auccat={CATEGORY}&fixed=2&exflg=1&b={b}&n={PERPAGE}")
        html = page.content()
        with open(f'yahoo_data/{i+1}.html',mode='w',encoding='utf-8') as f:
            f.write(html)
        #page.screenshot(path=f"yahoo_data/{i+1}.png")

    # Close page
    print("Loop end.....")

    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
