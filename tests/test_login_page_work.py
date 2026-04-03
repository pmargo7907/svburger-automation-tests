from pages.home_page import HomePage
from utils.browser_factory import BrowserFactory
from pages.login_page import LoginPage

def test_login_page_works():
    factory = BrowserFactory(headless=False)
    page = factory.start()

    try:
        home = HomePage(page)
        home.open()

        home.click_sign_in()

        login = LoginPage(page)
        assert login.is_opened()

        login.login("mail@gmail.com", "a123456")

        print("URL after Sign In:", page.url)
        page.wait_for_selector(login.logout_button, timeout=10000)
        assert login.is_profile_opened()
        page.wait_for_timeout(10000)


    finally:
        factory.close()