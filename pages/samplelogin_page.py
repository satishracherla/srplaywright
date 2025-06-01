from playwright.sync_api import Page

class SampleLoginPage:
    def __init__(self, page: Page):
        self.page = page
        #username_input = page.get_by_label("Username")
        self.email_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("input#Login")

    def navigate(self):
        self.page.goto("https://login.salesforce.com")

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def is_logged_in(self) -> bool:
      #  home_link = self.page.get_by_role("link", name="Home")
        return self.page.locator("a[href='/lightning/page/home']").is_visible()

    # Create a locator.
#get_started = page.get_by_role("link", name="Get started")

# Click it.
#get_started.click()
