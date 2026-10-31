from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.link import Link
from elements.text import Text


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, "login-form-email-input", "Email")
        self.password_input = Input(page, "login-form-password-input", "Password")
        self.login_button = Button(page, "login-page-login-button", "Login")
        self.registration_link = Link(
            page, "login-page-registration-link", "Registration"
        )
        self.wrong_email_or_password_alert = Text(
            page, "login-page-wrong-email-or-password-alert", "Wrong email or password"
        )

    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()

    def check_visible(self, email: str, password: str):
        if self.email_input == email and self.password_input == password:
            expect(self.wrong_email_or_password_alert).to_be_not_visible()
        else:
            self.wrong_email_or_password_alert.check_visible()
            self.wrong_email_or_password_alert.check_have_text(
                "Wrong email or password"
            )
