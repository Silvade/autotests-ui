import pytest
from playwright.sync_api import Playwright, Page, expect


@pytest.fixture()
def chromium_page(playwright: Playwright) -> Page:
    chromium = playwright.chromium.launch(headless=False)
    context = chromium.new_context()
    return context.new_page()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    chromium = playwright.chromium.launch(headless=False)
    context = chromium.new_context()
    page = context.new_page()
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )

    registration_button = page.get_by_test_id("registration-page-registration-button")
    expect(registration_button).to_be_disabled()

    email_input = page.get_by_test_id("registration-form-email-input").locator("input")
    email_input.fill("user.name@gmail.com")

    username_input = page.get_by_test_id("registration-form-username-input").locator(
        "input"
    )
    username_input.fill("username")

    password_input = page.get_by_test_id("registration-form-password-input").locator(
        "input"
    )
    password_input.fill("password")

    expect(registration_button).to_be_enabled()

    registration_button.click()
    path = "browser-state.json"
    context.storage_state(path=path)
    chromium.close()


@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    chromium = playwright.chromium.launch(headless=False)
    context = chromium.new_context(storage_state="browser-state.json")
    yield context.new_page()
    chromium.close()
