class ProductsPage:
    URL = "https://svburger1.co.il/#/"

    def __init__(self, page):
        self.page = page
        self.products_container = ".productsMain"
        self.product_cards = ".productsMain .card"
        self.reserve_btn = "text=Reserve"
        self.popup = ".popup"
        self.close_popup_btn = "text=Back to Menu"
        self.summary_title = "text=SVBurger Summary"

    def is_opened(self):
        return self.page.url.startswith(self.URL) and self.page.locator(self.products_container).is_visible()

    def click_product_by_index(self, index: int):
        cards=self.page.locator(self.product_cards)
        cards.nth(index).click()

    def get_products_count(self):
        return self.page.locator(self.product_cards).count()

    def click_reserve_btn(self):
        reserve = self.page.locator(self.reserve_btn)
        reserve.wait_for(state="visible", timeout=10000)
        reserve.click()

    def is_order_popup_opened(self):
        return self.page.locator(self.popup).count() == 1

    def close_popup(self):
        self.page.locator(self.close_popup_btn).click()
        self.page.wait_for_selector(self.popup, state="hidden", timeout=5000)

    def is_summary_visible(self):
        return self.page.locator(self.summary_title, timeout=10000)