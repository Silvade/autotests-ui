from playwright.sync_api import Page

from components.authentication.registration_form_component import (
    RegistrationFormComponent,
)
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_view = RegistrationFormComponent(page)
