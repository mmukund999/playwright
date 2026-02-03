from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from playwright.sync_api import Page, expect


@dataclass(frozen=True)
class PageSpec:
    name: str
    path: str
    heading: str
    primary_action: str
    has_realtime_widget: bool = True


class BasePage:
    def __init__(self, page: Page, base_url: str, spec: PageSpec) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.spec = spec

    @property
    def url(self) -> str:
        return f"{self.base_url}{self.spec.path}"

    def open(self) -> None:
        self.page.goto(self.url)

    def expect_heading(self) -> None:
        expect(self.page.get_by_role("heading", name=self.spec.heading)).to_be_visible()

    def expect_primary_action_enabled(self) -> None:
        expect(self.page.get_by_role("button", name=self.spec.primary_action)).to_be_enabled()

    def expect_primary_action_disabled(self) -> None:
        expect(self.page.get_by_role("button", name=self.spec.primary_action)).to_be_disabled()

    def expect_realtime_widget(self) -> None:
        if self.spec.has_realtime_widget:
            expect(self.page.get_by_test_id("realtime-widget")).to_be_visible()

    def open_with_query(self, params: Iterable[tuple[str, str]]) -> None:
        query = "&".join(f"{key}={value}" for key, value in params)
        self.page.goto(f"{self.url}?{query}")
