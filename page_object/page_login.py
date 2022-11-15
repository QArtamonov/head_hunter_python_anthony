from locators.locators_login import LocatorsLogin
from .base_class import BaseClass
from config import user_mail, valid_title_login

class PageLogin(BaseClass):

    def login(self):
        print('-' * 30)
        print('Авторизация:')
        print('-' * 30)

        print('Нажатие на кнопку "Войти"')
        button_start_auth = self.driver.find_element(*LocatorsLogin.button_start_auth)
        button_start_auth.click()

        print(f'Ввод почты пользователя: {user_mail}')
        field_user_mail = self.driver.find_element(*LocatorsLogin.field_user_mail)
        field_user_mail.clear()
        field_user_mail.send_keys(user_mail)

        print('Отправка почты')
        button_send_mail = self.driver.find_element(*LocatorsLogin.button_send_mail)
        button_send_mail.click()

        print(f'На почту {user_mail} отправлен код.')
        otp_code = input('==> Введите код из письма: ')

        print(f'Ввод кода {otp_code}')
        field_otp_code = self.driver.find_element(*LocatorsLogin.field_otp_code)
        field_otp_code.clear()
        field_otp_code.send_keys(otp_code)

        print('Отправка кода')
        button_send_otp = self.driver.find_element(*LocatorsLogin.button_send_otp)
        button_send_otp.click()

        print('Проверка перехода на внутреннюю страницу сайта')
        self.wait(4)
        # Поменять правую сторону на корректное значение
        print('Заголовок страницы: ', self.driver.title)
        assert self.driver.title == valid_title_login
        print('Авторизация прошла успешна')
