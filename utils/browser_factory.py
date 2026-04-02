from playwright.sync_api import sync_playwright
import os

class BrowserFactory:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()
        headless = os.getenv("CI") == "true"
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.page = self.browser.new_page()
        return self.page

    def close(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()


