from selenium.webdriver.common.by import By

class LocatorsSubscription:

    total_vacancies = (By.XPATH, '//a[@data-qa="autosearch__results-counter_total"]')

    new_vacancies = (By.XPATH, '//a[@data-qa="autosearch__results-counter_new"]')

