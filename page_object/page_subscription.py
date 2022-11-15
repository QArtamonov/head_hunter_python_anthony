from .page_login import PageLogin
from locators.locators_common import LocatorsCommon
from locators.locators_subscription import LocatorsSubscription

class PageSubscription(PageLogin):

    def check_subscription(self):
        print('-' * 30)
        print('Выбор вакансий для отклика:')
        print('-' * 30)

        print('Нажатие на колокольчик в меню')
        button_menu_notification = self.driver.find_element(*LocatorsCommon.CommonMenu.button_menu_notification)
        button_menu_notification.click()

        print('Нажатие на кнопку автопоиска')
        button_setting_autosearch = self.driver.find_elements(*LocatorsCommon.CommonMenu.button_setting_autosearch)
        button_autosearch = self.driver.find_elements(*LocatorsCommon.CommonMenu.button_autosearch)
        if button_setting_autosearch != []:
            button_setting_autosearch[0].click()
        else:
            button_autosearch[0].click()

        print('Сбор информации о вакансиях')
        new_vacancy = self.driver.find_elements(*LocatorsSubscription.new_vacancies)
        total_vacancy = self.driver.find_elements(*LocatorsSubscription.total_vacancies)

        if len(new_vacancy) == 1:
            print(f'Запуск итерации для новых вакансий: {new_vacancy[0].text}')
            button_new_vacancies = self.driver.find_element(*LocatorsSubscription.new_vacancies)
            button_new_vacancies.click()
        elif len(new_vacancy) == 0:
            print('~' * 30)
            print('Новых вакансий нет. Выберите дальнейшее действие: ')
            print('1. Выйти из программы')
            print(f'2. Запуск итераций для всех вакансий: {total_vacancy[0].text}')
            print('~' * 30)
            choice_vacancies = input('==> Выберите номер с действием: ')
            if choice_vacancies == '2':
                print('Запуск итерации для всех вакансий')
                button_total_vacancies = self.driver.find_element(*LocatorsSubscription.total_vacancies)
                button_total_vacancies.click()
            elif choice_vacancies == '1':
                print('Выход из программы')
                self.driver.close()
            else:
                print('Что-то пошло не так... Принудительный выход из программы')
                self.driver.close()









