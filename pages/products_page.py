class ProductsPage:
    URL = "https://svburger1.co.il/#/"

    def __init__(self, page):
        self.page = page
        self.products_container = ".productsMain"
        self.product_cards = ".productsMain .card"
        self.reserve_btn = "text=Reserve"
        self.popup = ".popup"
        self.summary_title = "text=SVBurger Summary"

    def is_opened(self):
        return self.page.url.startswith(self.URL) and self.page.locator(self.products_container).is_visible()

    def click_first_product(self):
        self.page.locator(self.product_cards).first.click()

    def click_reserve_btn(self):
        self.page.locator(self.reserve_btn).click()

    def is_order_popup_opened(self):
        return self.page.locator(self.popup).count() == 1

    def is_summary_visible(self):
        return self.page.locator(self.summary_title).count() == 1