from playwright.sync_api import sync_playwright
import os

class BrowserFactory:
    def __init__(self, headless=False):
        self.playwright = None
        self.browser = None
        self.page = None
        self.headless = headless

    def start(self):
        self.playwright = sync_playwright().start()

        run_headless = self.headless
        if os.getenv("CI") == "true":
            run_headless = True

        self.browser = self.playwright.chromium.launch(
            headless=run_headless
        )

        self.page = self.browser.new_page()
        return self.page

    def close(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()


