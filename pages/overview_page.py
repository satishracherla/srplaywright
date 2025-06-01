from playwright.sync_api import Page

class OverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.locator("#finish")

    def complete_order(self):
        self.finish_button.click()
