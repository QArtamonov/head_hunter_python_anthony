from page_object.page_parse_vacancies import PageParseVacancies

def main():

    hh = PageParseVacancies()

    hh.open()

    hh.login()

    hh.check_subscription()

    hh.parse_vacancies()


if __name__ == '__main__':
    print('Запуск программы')
    main()