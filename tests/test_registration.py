from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utils.browser_factory import BrowserFactory
import time

def test_user_can_register_successfully():
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
            first_name = "Anna",
            last_name = "Ivanova",
            email = email,
            password = "123456",
            confirm_password = "123456"
        )
        print("URL after register:", page.url)
        page.wait_for_selector(registration.logout_button)
        assert registration.is_profile_opened()
        page.wait_for_timeout(10000)
    finally:
        factory.stop()

def test_user_register_with_invalid_email():
    factory = BrowserFactory(headless=False)
    page = factory.start()

    try:
        home = HomePage(page)
        home.open()
        assert home.is_loaded()

        home.click_sign_up()

        registration = RegistrationPage(page)
        assert registration.is_opened()

        registration.register(
            first_name = "Anna",
            last_name = "Ivanova",
            email = "invalid-email",
            password = "123456",
            confirm_password = "123456"
        )
        email_field = page.locator(registration.email_input)

        validation_message = email_field.evaluate("el => el.validationMessage")

        print(validation_message)
        print("URL after register:", page.url)

        assert validation_message != ""

        page.wait_for_timeout(10000)

    finally:
        factory.stop()

def test_user_register_with_empty_email():
    factory = BrowserFactory(headless=False)
    page = factory.start()

    try:
        home = HomePage(page)
        home.open()
        assert home.is_loaded()

        home.click_sign_up()

        registration = RegistrationPage(page)
        assert registration.is_opened()

        registration.register(
            first_name = "Anna",
            last_name = "Ivanova",
            email = "",
            password = "123456",
            confirm_password = "123456"
        )
        email_field = page.locator(registration.email_input)

        validation_message = email_field.evaluate("el => el.validationMessage")

        print(validation_message)
        print("URL after register:", page.url)

        assert validation_message != "Please fill out this field"

        page.wait_for_timeout(10000)

    finally:
        factory.stop()
def test_user_register_password_mismatch():
    factory = BrowserFactory(headless=False)
    page = factory.start()
    try:
        home = HomePage(page)
        home.open()
        assert home.is_loaded()
        home.click_sign_up()

        email = f"anna{int(time.time())}@gmail.com"
        registration = RegistrationPage(page)
        assert registration.is_opened()
        registration.register(
            first_name = "Anna",
            last_name = "Ivanova",
            email = email,
            password = "123456",
            confirm_password = "654321"
            )
        print("URL after register:", page.url)
        assert page.url == "https://svburger1.co.il/#/SignUp"
        assert not registration.is_profile_opened()
        page.wait_for_timeout(10000)

    finally:
        factory.stop()

def test_user_register_email_already_exists():
    factory = BrowserFactory(headless=False)
    page = factory.start()

    dialog_message = None

    def handle_dialog(dialog):
        nonlocal dialog_message
        dialog_message = dialog.message
        page.wait_for_timeout(3000)
        dialog.accept()

    page.on("dialog", handle_dialog)

    try:
        email = f"anna{int(time.time())}@gmail.com"

        home = HomePage(page)
        home.open()
        assert home.is_loaded()
        home.click_sign_up()

        registration = RegistrationPage(page)
        assert registration.is_opened()

        registration.register(
            first_name = "Anna",
            last_name = "Ivanova",
            email =  email,
            password = "123456",
            confirm_password = "123456"
        )
        page.wait_for_selector(registration.logout_button)
        print("URL after first register:", page.url)
        assert registration.is_profile_opened()

        page.click(registration.logout_button)

        home.click_sign_up()

        registration = RegistrationPage(page)

        registration.register(
            first_name = "Anna",
            last_name = "Ivanova",
            email = email,
            password = "123456",
            confirm_password = "123456"
        )

        page.wait_for_timeout(10000)
        print("URL after second register:", page.url)
        print("Dialog message repr:", repr(dialog_message))
        assert dialog_message is not None
        assert "already in use" in dialog_message
        page.wait_for_timeout(10000)

    finally:
        factory.stop()
