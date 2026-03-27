from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils.browser_factory import BrowserFactory
from pages.products_page import ProductsPage
import time
def test_user_can_reserve_one_product():
    factory = BrowserFactory(headless=False)
    page = factory.start()
    try:
       home = HomePage(page)
       home.open()
       assert home.is_loaded()

       home.click_sign_up()

       registration = RegistrationPage(page)
       assert registration.is_opened()
       email = f"anna{int(time.time())}@gmail.com"
       registration.register(
           first_name="Anna",
           last_name="Ivanova",
           email= email,
           password="123456",
           confirm_password="123456"
       )
       print("URL after register:", page.url)
       page.wait_for_selector(registration.logout_button)
       assert registration.is_profile_opened()

       page.wait_for_selector(".productsMain", timeout=10000)

       menu = ProductsPage(page)
       assert menu.is_opened()
       page.wait_for_timeout(10000)

       count = menu.get_products_count()
       print("Products in Menu:", count)
       assert count > 0

       menu.click_product_by_index(0)
       menu.click_reserve_btn()
       page.wait_for_selector("text=SVBurger Summary", timeout=10000)

       assert menu.is_order_popup_opened()
       assert menu.is_summary_visible()

    finally:
       factory.stop()

    """


    for i in range(count):
        menu.click_product_by_index(i)
        menu.click_reserve_btn()

        page.wait_for_selector("text=SVBurger Summary", timeout=10000)

    assert menu.is_order_popup_opened()
    assert menu.is_summary_visible()"""
print("Test update")
