from playwright.sync_api import sync_playwright
import time


LOGIN_URL = "http://quotes.toscrape.com/login"  # THIS IS THE CORRECTED URL
USERNAME = "admin"
PASSWORD = "admin"


def demonstrate_login():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        page = browser.new_page()

        page.goto(LOGIN_URL)

        page.locator("#username").fill(USERNAME)

        page.locator("#password").fill(PASSWORD)

        page.locator('input[type="submit"]').click()

        logout_link = page.locator('a[href="/logout"]')
        logout_link.wait_for(timeout=5000)

        page.screenshot(path="authenticated_page.png")

        time.sleep(5)
        browser.close()


demonstrate_login()
