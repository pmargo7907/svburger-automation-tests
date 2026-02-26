from playwright.sync_api import sync_playwright

class BrowserFactory:
    def __init__(self,headless=False):
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(channel = "chrome",
                                                       headless=self.headless,  slow_mo=300)
        self.page = self.browser.new_page()
        return self.page

    def stop(self):
        self.browser.close()
        self.playwright.stop()