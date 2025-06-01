from time import sleep

from pages.samplelogin_page import LoginPage

def test_valid_login(page):
    samplelogin_page = LoginPage(page)
    samplelogin_page.navigate()
    samplelogin_page.login("satish.r177@agentforce.com", "Agentforce@2025")
    sleep(10)
    # Verify that the login was successful
    assert samplelogin_page.is_logged_in()
