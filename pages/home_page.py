class HomePage:
    URL = "https://svburger1.co.il#/HomePage"

    def __init__(self, page):
        self.page = page
        self.title_text = "text=Lets start your way to our best burger"
        self.submit_button = "text=Sign Up"
        self.sign_in_button = "a[href='#/SignIn'] button"
        self.product_cards = ".productsMain.card"

    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_timeout(3000)

    def is_loaded(self):
        return self.page.locator(self.title_text).count() == 1

    def click_sign_up(self):
        self.page.click(self.submit_button)
        print("URL after sign_up:", self.page.url)

    def click_sign_in(self):
        self.page.click(self.sign_in_button)
        print("URL after sign_in:", self.page.url)
