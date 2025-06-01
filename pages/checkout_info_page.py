from playwright.sync_api import Page

class CheckoutInfoPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.zip_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")

    def enter_customer_info(self, first_name: str, last_name: str, zip_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.zip_code_input.fill(zip_code)
        self.continue_button.click()
