from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils.browser_factory import BrowserFactory
import time
def test_open_successfully():
    factory = BrowserFactory(headless=False)
    page = factory.start()
    home = HomePage(page)
    home.open()
    assert home.is_loaded()
    factory.close()
def test_click_sign_up_successfully():
    factory = BrowserFactory(headless=False)
    page = factory.start()
    home = HomePage(page)
    home.open()
    assert home.is_loaded()
    home.click_sign_up()
    registration = RegistrationPage(page)
    assert registration.is_opened()
    time.sleep(5)
    factory.close()


