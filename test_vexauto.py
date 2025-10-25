from playwright.sync_api import Playwright
import time

def test_pageone(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://api.vex.com/zh-CN/exp/home/python/Drivetrain.html")


    page.wait_for_selector(".sidebar-secondary-item a")


    links = page.locator(".sidebar-secondary-item a")
    count = links.count()
    print(f"Found {count} links in sidebar.\n")


    for i in range(count):
        links = page.locator(".sidebar-secondary-item a")
        link = links.nth(i)
        text = link.inner_text().strip()
        link.click()
        time.sleep(2)
        page.wait_for_load_state("load")  
        print(page.url)
        

    page.wait_for_timeout(3000)
    context.close()
    browser.close()
