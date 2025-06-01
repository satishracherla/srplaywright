from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.backpack_add_to_cart = page.locator("#add-to-cart-sauce-labs-backpack")
        self.bike_light_add_to_cart = page.locator("#add-to-cart-sauce-labs-bike-light")
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_items_to_cart(self):
        self.backpack_add_to_cart.click()
        self.bike_light_add_to_cart.click()
        self.cart_icon.click()
