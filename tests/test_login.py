from time import sleep

from pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("satish.r177@agentforce.com", "Agentforce@2025")
    sleep(10)
    # Verify that the login was successful
    assert login_page.is_logged_in()
