class LoginPage:
    def __init__(self,page):
        self.page = page
        self.email_input = "input[placeholder='Enter your email']"
        self.password_input  = "input[placeholder='Enter your password']"
        self.submit_button = "text=Sign in"
        self.invalid_password = "text=Forgot Password"
        self.forgot_button = "#forgotId'"
        self.logout_button = "text=Log out"

    def is_opened(self):
        return self.page.locator(self.email_input).is_visible()

    def login(self,email,password):
        self.page.click(self.email_input)
        self.page.fill(self.email_input, email)
        self.page.click(self.password_input)
        self.page.fill(self.password_input, password)
        self.page.click(self.submit_button)

    def click_forgot_password(self):
        self.page.click(self.forgot_button)

    def is_profile_opened(self):
        return self.page.locator(self.logout_button).is_visible()