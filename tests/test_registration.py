from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils.browser_factory import BrowserFactory

def test_user_can_register():
    factory = BrowserFactory(headless=False)
    page = factory.start()

    home = HomePage(page)
    home.open()
    assert home.is_loaded()

    home.click_sign_up()

    registration = RegistrationPage(page)
    assert registration.is_opened()

    registration.register(
        first_name ="Anna",
        last_name="Ivanova",
        email="15test@mail.com",
        password="123456",
        confirm_password ="123456"
    )
    print("URL after register:", page.url)
    assert registration.is_profile_opened()
    page.wait_for_timeout(10000)
    factory.stop()
