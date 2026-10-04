from playwright.sync_api import Page

from components.authentication.login_form_component import LoginFormComponent
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_view = LoginFormComponent(page)
