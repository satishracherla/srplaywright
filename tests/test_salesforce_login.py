

def test_launch_salesforce_login_page(page):
    # Launches Chromium by default via the 'page' fixture
    page.goto("https://login.salesforce.com")

    # Optional: Assertion to verify page title
    assert "Login" in page.title()

    # Optional: Wait just to observe in headed mode
    page.wait_for_timeout(5000)
