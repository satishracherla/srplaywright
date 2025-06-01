from playwright.sync_api import Page
from pages.sdlogin_page import SdLoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.overview_page import OverviewPage
from pages.complete_page import CompletePage

def test_complete_order_placement(page: Page):
    page.goto("https://www.saucedemo.com/")

    login = SdLoginPage(page)
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(page)
    products.add_items_to_cart()

    cart = CartPage(page)
    cart.proceed_to_checkout()

    checkout = CheckoutInfoPage(page)
    checkout.enter_customer_info("John", "Doe", "12345")

    overview = OverviewPage(page)
    overview.complete_order()

    complete = CompletePage(page)
    complete.verify_order_complete()
