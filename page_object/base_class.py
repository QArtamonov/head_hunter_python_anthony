from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from config import base_url
import time
import re
from datetime import date

class BaseClass:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def wait(self, secs = 2):
        print(f'Ожидание {secs} сек...')
        time.sleep(secs)

    def open(self):
        print('=' * 30)
        print('Открытие браузера')
        print('=' * 30)
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.wait()

    def close(self):
        self.wait()
        print('=' * 30)
        print('Закрытие браузера')
        print('=' * 30)
        self.driver.close()

    def create_date_script(self):
        print('Подсчёт дней жизни скрипта')

        date_difference = date.today() - date(2022, 11, 13)
        date_parse = ''.join(re.findall(r'^\d+', str(date_difference)))

        day_not_even = ['1', '21', '31']
        day_even = ['2', '3', '4', '22', '23', '24']
        day = [' день', ' дня', ' дней']

        if date_parse in day_not_even:
            date_with_day = date_parse + day[0]
            print('Время жизни скрипта: ', date_with_day)
            return date_with_day
        elif date_parse in day_even:
            date_with_day = date_parse + day[1]
            print('Время жизни скрипта: ', date_with_day)
            return date_with_day
        else:
            date_with_day = date_parse + day[2]
            print('Время жизни скрипта: ', date_with_day)
            return date_with_day

    def motivation_mail(self, date_created_script, title_vacancy, name_company):
        motivation = f'Приветствую! Меня зовут Питон Антон. \
\nЯ автоматизированный скрипт, созданный {date_created_script} назад для одной единственной задачи... Дело в том, что я помогаю своему хозяину найти работу :) \
\nКаждый день я отбираю на HeadHunter релевантные вакансии и откликаюсь на лучшие из них. После хитрых вычислений и строгого отбора мой алгоритм показал, что вакансия {title_vacancy} компании {name_company} идеально подходит для отклика. \
\nНемного о нас! \
\nМоего создателя зовут Артамонов Антон. Уже более года он занимается ручным и автоматизированным тестированием в нескольких проектах. Сейчас Антон проживает на Шри-Ланке и занимается свои любимым делом — тестированием. Антон принесёт пользу вашей команде и продукту. Он сможет разгрузить своих старших коллег, чтобы они сфокусировались на более важных задачах для бизнеса, так и самостоятельно брать на себя непростые задачи. И в этом ему помогу я, ручной Python :) \
\nКстати, в резюме Антона вы найдёте ссылку на публичный репозиторий в GitHub, где вы сможете посмотреть на логику этого скрипта. Даже если вы не очень разбираетесь в коде, не переживайте, для вас там будет видео с демонстрацией его работы. \
\nWelcome and check it! Было бы круто поработать вместе :) \
\n\
\nС уважением, Питон Антон.'
        return motivation



