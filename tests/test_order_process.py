from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils.browser_factory import BrowserFactory
from pages.products_page import ProductsPage

def test_user_can_make_order():
    factory = BrowserFactory(headless=False)
    page = factory.start()

    home = HomePage(page)
    home.open()
    assert home.is_loaded()

    home.click_sign_up()

    registration = RegistrationPage(page)
    assert registration.is_opened()

    registration.register(
        first_name="Anna",
        last_name="Ivanova",
        email="11test@mail.com",
        password="123456",
        confirm_password="123456"
    )
    print("URL after register:", page.url)
    assert registration.is_profile_opened()
    page.wait_for_selector(".productsMain", timeout=10000)

    menu = ProductsPage(page)
    assert menu.is_opened()

    menu.click_first_product()

    menu.click_reserve_btn()
    page.wait_for_selector("text=SVBurger Summary", timeout=10000)

    assert menu.is_order_popup_opened()
    assert menu.is_summary_visible()

    #factory.stop()
