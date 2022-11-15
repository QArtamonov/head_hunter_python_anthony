from selenium.webdriver.common.by import By

class LocatorsItemVacancy:

    vacancy_experience = (By.XPATH, '//span[@data-qa="vacancy-experience"]')

    vacancy_description = (By.XPATH, '//div[@data-qa="vacancy-description"]')

    vacancy_title = (By.XPATH, '//h1[@data-qa="vacancy-title"]')

    vacancy_company_names = (By.XPATH, '//a[@data-qa="vacancy-company-name"]/span/span')

    mark_favorites_vacancy = (By.XPATH, '//button[@data-qa="vacancy-body-mark-favorite_false"]')

    buttons_respond = (By.XPATH, '//a[@data-qa="vacancy-response-link-top"]')

    button_open_motivation = (By.XPATH, '//button[@data-qa="vacancy-response-letter-toggle"]')

    field_motivation = (By.XPATH, '//textarea[@placeholder="Напишите, почему именно ваша кандидатура должна заинтересовать работодателя"]')

    button_send_motivation = (By.XPATH, '//button[@data-qa="vacancy-response-letter-submit"]')

