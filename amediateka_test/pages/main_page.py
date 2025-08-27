from selene import be, have, browser, by

class MainPage:
    def browser_open(self):
        browser.open("https://www.dns-shop.ru/")

    def search_product(self, value):
        browser.element("[name='q']").type(value).press_enter()

    def open_product_card(self):
        browser.element("[class='catalog-product__name']").click()

    def add_product_in_favorites(self):
        browser.element("[class='button-ui button-ui_grey button-ui_md button-ui_icon wishlist-btn wishlist-btn_empty']").click()\
        