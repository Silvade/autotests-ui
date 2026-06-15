import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page) -> None:
    page = chromium_page_with_state
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
