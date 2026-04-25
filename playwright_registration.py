from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
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

    context.storage_state(path="browser-state.json")

    dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text("Dashboard")

    page.wait_for_timeout(5000)

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    context = chromium.new_context(storage_state="browser-state.json")
    page = context.new_page()
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses"
    )

    courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    results = page.get_by_test_id("courses-list-empty-view-title-text")
    expect(results).to_be_visible()
    expect(results).to_have_text("There is no results")

    results_empty_icon = page.get_by_test_id("courses-list-empty-view-icon")
    expect(results_empty_icon).to_be_visible()

    results_description = page.get_by_test_id(
        "courses-list-empty-view-description-text"
    )
    expect(results_description).to_be_visible()
    expect(results_description).to_have_text(
        "Results from the load test pipeline will be displayed here"
    )

    page.wait_for_timeout(5000)
