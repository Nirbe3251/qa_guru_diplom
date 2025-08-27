from selene import be, have, browser, by

class LoginPage:
    def browser_open(self):
        browser.open("https://www.amediateka.ru/")

    def click_login_button(self):
        browser.element('.Button_button__6pObN').click()

    def fill_email(self, value):
        browser.element('#checking-email-input').type(value)

    def fill_password(self, value):
        browser.element('#signin-password-input').type(value)

    def error_email(self):
        browser.element('.Auth_formError__J3vpb').should(have.text('E-mail введен некорректно'))

    def error_password(self):
        browser.element('.Auth_formError__J3vpb').should(have.text('Пароль введен некорректно. Пароль должен состоять минимум из 6 символов'))

    def error_valid_password(self):
        browser.element('.Auth_formError__J3vpb').should(have.text('Неправильный пароль'))