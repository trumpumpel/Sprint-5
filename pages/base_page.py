from selenium.webdriver.common.by import By
from locators import email_log, password_log, enter, name_reg, email_reg, password_reg, enter_by_button_at_main, \
    personal_account, enter_by_personal_account, constructor, stellar_burger, log_out_of_your_account, bread, sauces, \
    filling


class BasePage:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

    def __init__(self, driver, path):
        self.driver = driver
        self.path = path
        self.base_url = self.BASE_URL + self.path

    def open(self):
        self.driver.get(self.base_url)

    def login(self, email, password):
        self.__switch_between_login_and_register_page('login')
        email_element = self.driver.find_element(By.CSS_SELECTOR, email_log)
        password_element = self.driver.find_element(By.CSS_SELECTOR, password_log)
        email_element.send_keys(email)
        password_element.send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, enter).click()

    def register(self, name, email, password):
        self.__switch_between_login_and_register_page('register')
        name_element = self.driver.find_element(By.XPATH, name_reg)
        email_element = self.driver.find_element(By.XPATH, email_reg)
        password_element = self.driver.find_element(By.CSS_SELECTOR, password_reg)
        name_element.send_keys(name)
        email_element.send_keys(email)
        password_element.send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, enter).click()

    def __switch_between_login_and_register_page(self, target_path):
        if self.path != target_path:
            self.base_url = self.BASE_URL + target_path
            self.open()

    def enter_by_button_at_main(self):
        self.driver.find_element(By.XPATH, enter_by_button_at_main).click()

    def enter_by_personal_account(self):
        self.driver.find_element(By.XPATH, personal_account).click()

    def enter_form_registration(self):
        self.driver.find_element(By.XPATH, enter_by_personal_account).click()

    def enter_by_forgot_password_page(self):
        self.driver.find_element(By.XPATH, enter_by_personal_account).click()

    def transfer_to_your_personal_account_by_push_button(self):
        self.driver.find_element(By.XPATH, personal_account).click()

    def click_to_constructor(self):
        self.driver.find_element(By.XPATH, constructor).click()

    def click_to_stellar_burgers(self):
        self.driver.find_element(By.XPATH, stellar_burger).click()

    def log_out_of_personal_account(self):
        self.driver.find_element(By.XPATH, log_out_of_your_account).click()

    def transition_to_bread(self):
        self.driver.find_element(By.XPATH, bread).click()

    def transition_to_sauces(self):
        self.driver.find_element(By.XPATH, sauces).click()

    def transition_to_filling(self):
        self.driver.find_element(By.XPATH, filling).click()
