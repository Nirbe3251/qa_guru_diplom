from selene import be, have, browser, by

class LoginPage:
    def browser_open(self):
        browser.open("https://www.dns-shop.ru/")

    def click_login_button(self):
        browser.element()