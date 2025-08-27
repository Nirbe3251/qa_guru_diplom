import allure

from amediateka_test.pages.login_page import LoginPage

def test_login():
    login_page = LoginPage()

    with allure.step('Открыть браузер'):
        login_page.browser_open()
        login_page.click_login_button()

    with allure.step('Заполнить поле почты'):
        login_page.fill_email('daniil.efimow@mail.ru')
        login_page.click_login_button()

    with allure.step('Заполнить поле пароль'):
        login_page.fill_password('dandris2003')
        login_page.click_login_button()

def test_login_without_email():
    login_page = LoginPage()

    with allure.step('Открыть браузер'):
        login_page.browser_open()
        login_page.click_login_button()

    with allure.step('Не вводить почту'):
        login_page.fill_email('')
        login_page.click_login_button()

    with allure.step('Проверка ошибки ввода почты'):
        login_page.error_email()

def test_not_valid_email():
    login_page = LoginPage()

    with allure.step('Открыть браузер'):
        login_page.browser_open()
        login_page.click_login_button()

    with allure.step('Ввести почту без знака "@"'):
        login_page.fill_email('daniil.efimowmail.ru')
        login_page.click_login_button()

    with allure.step('Проверка ошибки ввода почты'):
        login_page.error_email()

def test_login_without_password():
    login_page = LoginPage()

    with allure.step('Открыть браузер'):
        login_page.browser_open()
        login_page.click_login_button()

    with allure.step('Заполнить поле почты'):
        login_page.fill_email("daniil.efimow@mail.ru")
        login_page.click_login_button()

    with allure.step('Не вводить пароль'):
        login_page.fill_password('')
        login_page.click_login_button()

    with allure.step('Проверка ошибки ввода пароля'):
        login_page.error_password()

def test_login_with_not_valid_password():
    login_page = LoginPage()

    with allure.step('Открыть браузер'):
        login_page.browser_open()
        login_page.click_login_button()

    with allure.step('Заполнить поле почты'):
        login_page.fill_email("daniil.efimow@mail.ru")
        login_page.click_login_button()

    with allure.step('Ввести невалидный пароль'):
        login_page.fill_password('123456')
        login_page.click_login_button()
    with allure.step('Проверка ошибки при вводе неправильного пароля'):
        login_page.error_valid_password()
