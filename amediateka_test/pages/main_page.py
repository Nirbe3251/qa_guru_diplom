from selene import be, have, browser, by

class MainPage:
    def browser_open(self):
        browser.open("https://www.amediateka.ru/")

    def click_search_button(self):
        browser.element('[aria-label="search"]').click()

    def search_series(self, value):
        browser.element('.SearchInput_input__OVDm6').type(value)

    def search_film(self, value):
        browser.element('.SearchInput_input__OVDm6').type(value)

    def search_genre(self, value):
        browser.element('.SearchInput_input__OVDm6').type(value)

    def click_the_genre(self):
        browser.element('.visually-hidden').click()

    def choice_genre_on_the_main_page(self, value):
        browser.element(by.text(value)).click()

    def open_series(self):
        browser.element()


        