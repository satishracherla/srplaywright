from playwright.sync_api import Page, expect

class CompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.confirmation_text = page.locator(".complete-header")

    def verify_order_complete(self):
        expect(self.confirmation_text).to_have_text("Thank you for your order!")
