from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.yahoo.co.jp/
    page.goto("https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&fr=auc_top&p=%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC&x=0&y=0")


    # Click text=前へ 1 2 3 4 5 6 7 8 9 10 … 次へ >> a
    #page.click("text=前へ 1 2 3 4 5 6 7 8 9 10 … 次へ >> a")

    # 0× click
    #page.click("text=前へ 1 2 3 4 5 6 7 8 9 10 … 次へ >> a")
    # assert page.url == "https://auctions.yahoo.co.jp/search/search?p=%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC&va=%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC&exflg=1&b=51&n=50"

    # Click text=前へ
    # with page.expect_navigation(url="https://auctions.yahoo.co.jp/search/search?p=%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC&va=%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC&exflg=1&b=1&n=50"):
    #with page.expect_navigation():
    #    page.click("text=前へ")

    for i in range(5):
    # Click text=次へ
    # with page.expect_navigation(url="https://auctions.yahoo.co.jp/search/search?p=%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC&va=%E3%83%88%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC&exflg=1&b=101&n=50"):
        with page.expect_navigation():
            html = page.content()
            with open(f'{i}.html',mode='w',encoding='utf-8') as f:
                f.write(html)

            page.click("text=次へ")


    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
