from selenium.webdriver.common.by import By

class LocatorsCommon:

    class CommonMenu:

        button_menu_notification = (By.XPATH, '//button[@data-qa="mainmenu_notifications"]')

        button_setting_autosearch = (By.XPATH, '//a[@data-qa="notification-link" and text()="Настроить автопоиск"]')

        button_autosearch = (By.XPATH, '//div[@data-notification-template-key="new.vacancies.in.autosearch"]//a[@data-qa="notification-link"]')