from .page_subscription import PageSubscription
from locators.locators_list_vacancies import LocatorsListVacancies
from locators.locators_item_vacancy import LocatorsItemVacancy
from selenium.webdriver.common.by import By
from config import start_words_in_title, stop_words_in_title, stop_word_item

class PageParseVacancies(PageSubscription):

    def parse_vacancies(self):
        print('~' * 30)
        print('Запуск отбора вакансий по заголовкам: ')
        print('~' * 30)

        while 1 == 1:
            print('Сбор заголовков вакансий на странице')
            all_titles_parse = self.driver.find_elements(*LocatorsListVacancies.common_title_xpath)
            all_titles = []
            for title in all_titles_parse:
                all_titles.append(title.text)
            print(f'Список вакансий на странице: \n{all_titles}')
            print('~' * 30)

            print('Отбор заголовков по старт-словам')
            valid_titles = []
            for title in all_titles:
                for start_word in start_words_in_title:
                    if start_word in title.lower() and title not in valid_titles:
                          valid_titles.append(title)
            print(f'Результат отбора по старт-словам: \n{valid_titles}')
            print('~' * 30)

            print('Отбор заголовков по стоп-словам')
            clone_valid_titles = []
            clone_valid_titles.extend(valid_titles)
            for title in clone_valid_titles:
                for stop_word in stop_words_in_title:
                    if stop_word in title.lower() and title in valid_titles:
                        valid_titles.remove(title)
                        break
            print(f'Результат отбора по стоп-словам: \n{valid_titles}')
            print('~' * 30)

            if valid_titles == []:
                print('Подходящих вакансий на странице нет')

                check_button_next_page = self.driver.find_elements(*LocatorsListVacancies.button_next_page)
                print('Проверка наличия других страниц')
                if len(check_button_next_page) != 0:
                    print('Переход на следующую страницу')
                    button_next_page = self.driver.find_element(*LocatorsListVacancies.button_next_page)
                    button_next_page.click()
                    continue
                elif len(check_button_next_page) == 0:
                    print('Страниц больше нет')
                    self.close()
                    break

            for title in valid_titles:
                print('-' * 30)
                print(f'Итерация для вакансии: {title}')
                print('-' * 30)

                self.wait()
                print('Переход в карточку вакансии')
                button_title = self.driver.find_element(By.XPATH, '//a[@data-qa="serp-item__title" and text()="' + title + '"]')
                button_title.click()
                self.driver.switch_to.window(self.driver.window_handles[1])

                if 'Смотреть отклик' in self.driver.page_source:
                    print('Вы уже откликались на эту вакансию')
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    continue

                print('Проверка наличия стоп-слов на странице')
                vacancy_experience = self.driver.find_element(*LocatorsItemVacancy.vacancy_experience).text
                vacancy_description = self.driver.find_element(*LocatorsItemVacancy.vacancy_description).text

                validation_page = []
                for word in stop_word_item:
                    if word in vacancy_experience or word in vacancy_description:
                        validation_page.append(word)
                if validation_page == []:
                    print('Стоп-слов на странице нет')
                else:
                    print(f'Стоп-слова в вакансии: {validation_page}')


                if len(validation_page) == 0:
                    print('Сбор уникальной информации для сопроводительного письма')
                    vacancy_title = self.driver.find_element(*LocatorsItemVacancy.vacancy_title).text
                    print(f'Название вакансии: {vacancy_title}')

                    vacancy_company_names = self.driver.find_elements(*LocatorsItemVacancy.vacancy_company_names)
                    vacancy_company_name = ''
                    if len(vacancy_company_names) > 1:
                        vacancy_company_name = (vacancy_company_names[1].text)
                        print(f'Название компании: {vacancy_company_name}')
                    elif len(vacancy_company_names) == 1:
                        vacancy_company_name = (vacancy_company_names[0].text)
                        print(f'Название компании: {vacancy_company_name}')

                    date_script = self.create_date_script()
                    print(f'Количество дней работы скрипта: {date_script}')

                    print('Нажатие на кнопку "Откликнуться"')
                    buttons_respond = self.driver.find_elements(*LocatorsItemVacancy.buttons_respond)
                    button_respond = buttons_respond[0]
                    button_respond.click()

                    print('Открытие формы для ввода сопроводительного письма')
                    self.wait()
                    button_open_motivation = self.driver.find_element(*LocatorsItemVacancy.button_open_motivation)
                    button_open_motivation.click()

                    print('Ввод сопроводительного письма: ')
                    self.wait()
                    field_text_motivation = self.driver.find_element(*LocatorsItemVacancy.field_motivation)
                    field_text_motivation.clear()
                    field_text_motivation.send_keys(self.motivation_mail(date_script, vacancy_title, vacancy_company_name))
                    print('~' * 30)
                    print(self.motivation_mail(date_script, vacancy_title, vacancy_company_name))
                    print('~' * 30)

                    print('Отправка сопроводительного письма')
                    self.wait()
                    button_send_motivation = self.driver.find_element(*LocatorsItemVacancy.button_send_motivation)
                    button_send_motivation.click()

                    self.wait()
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    continue

                elif len(validation_page) > 0:
                    print('Закрытие страницы')
                    self.driver.close()
                    self.driver.switch_to.window(self.driver.window_handles[0])
                    continue

            check_button_next_page = self.driver.find_elements(*LocatorsListVacancies.button_next_page)
            print('Проверка наличия других страниц')
            if len(check_button_next_page) != 0:
                print('Переход на следующую страницу')
                button_next_page = self.driver.find_element(*LocatorsListVacancies.button_next_page)
                button_next_page.click()
                continue
            elif len(check_button_next_page) == 0:
                print('Страниц больше нет')
                self.close()
                break