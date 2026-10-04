from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.courses.cource_view_menu_component import CourseViewMenuComponent


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.course_title = page.get_by_test_id("course-widget-title-text")
        self.course_image = page.get_by_test_id("course-preview-image")
        self.course_max_score_text = page.get_by_test_id(
            "course-max-score-info-row-view-text"
        )
        self.course_min_score_text = page.get_by_test_id(
            "course-min-score-info-row-view-text"
        )
        self.course_estimated_time_text = page.get_by_test_id(
            "course-estimated-time-info-row-view-text"
        )

    def check_visible(
        self,
        index: int,
        title: str,
        max_score_text: str,
        min_score_text: str,
        estimated_time_text: str,
    ):
        expect(self.course_image.nth(index)).to_be_visible()

        expect(self.course_title.nth(index)).to_be_visible()
        expect(self.course_title.nth(index)).to_have_text(title)

        expect(self.course_max_score_text.nth(index)).to_be_visible()
        expect(self.course_max_score_text.nth(index)).to_have_text(
            f"Max score: {max_score_text}"
        )

        expect(self.course_min_score_text.nth(index)).to_be_visible()
        expect(self.course_min_score_text.nth(index)).to_have_text(
            f"Min score: {min_score_text}"
        )

        expect(self.course_estimated_time_text.nth(index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(index)).to_have_text(
            f"Estimated time: {estimated_time_text}"
        )
