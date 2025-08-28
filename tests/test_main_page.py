import allure

from amediateka_test.pages.main_page import MainPage

def test_search_series():
    main_page = MainPage()

    main_page.browser_open()
    main_page.click_search_button()
    main_page.search_series('Ходячие мертвецы')

def test_search_film():
    main_page = MainPage()

    main_page.browser_open()
    main_page.click_search_button()
    main_page.search_film('Амстердам')

def test_search_genre():
    main_page = MainPage()

    main_page.browser_open()
    main_page.click_search_button()
    main_page.search_genre('Детектив')

def test_choice_genre_on_the_main_page():
    main_page = MainPage()

    main_page.browser_open()
    main_page.choice_genre_on_the_main_page('Сериал')

