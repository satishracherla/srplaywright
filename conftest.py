from typing import Any, Generator

import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext

@pytest.fixture(scope="session")
def browser() -> Generator[Browser, Any, None]:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def context(browser: Browser) -> Generator[BrowserContext, Any, None]:
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context: BrowserContext) -> Generator[Page, Any, None]:
    page = context.new_page()
    yield page
    page.close()
