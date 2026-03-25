class RegistrationPage:
    def __init__(self,page):
        self.page = page
        self.first_name_input = "input[placeholder='Type your first name']"
        self.last_name_input = "input[placeholder='Type your last name']"
        self.email_input = "input[placeholder='Enter your email']"
        self.password_input  = "input[placeholder='Create Password']"
        self.confirm_password_input = "input[placeholder='Confirm Password']"
        self.submit_button = "text=Sign Up"
        self.profile_email = "text=Email:"
        self.logout_button = "text=Log out"
        self.invalid_email_error = "text=Invalid Email"
        self.email_exists_error = "text=Email already exists"

    def is_opened(self):
        return self.page.locator(self.first_name_input).is_visible()

    def register(self,first_name, last_name, email, password,confirm_password):
        self.page.click(self.first_name_input)
        self.page.fill(self.first_name_input, first_name)
        self.page.click(self.last_name_input)
        self.page.fill(self.last_name_input, last_name)
        self.page.click(self.email_input)
        self.page.fill(self.email_input, email)
        self.page.click(self.password_input)
        self.page.fill(self.password_input, password)
        self.page.click(self.confirm_password_input)
        self.page.fill(self.confirm_password_input, confirm_password)
        self.page.click(self.submit_button)


    def is_invalid_email_error_visible(self):
        self.page.wait_for_selector(self.invalid_email_error)
        return self.page.locator(self.invalid_email_error).is_visible()

    def is_email_already_exists(self):
        return self.page.locator(self.email_exists_error).is_visible()

    def is_profile_opened(self):
        return self.page.locator(self.logout_button).is_visible()

