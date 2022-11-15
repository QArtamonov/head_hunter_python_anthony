from selenium.webdriver.common.by import By

class LocatorsLogin:

    button_start_auth = (By.XPATH, '//a[@data-qa="login"]')

    field_user_mail = (By.XPATH, '//input[@name="login"]')

    button_send_mail = (By.XPATH, '//button/span[text()="Продолжить"]')

    field_otp_code = (By.XPATH, '//input[@name="otp-code-input"]')

    button_send_otp = (By.XPATH, '//button/span[text()="Подтвердить"]')